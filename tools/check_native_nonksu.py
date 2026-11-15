#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Fail closed unless the Coral non-KSU build uses Hecker-branded native recovery."""
import argparse
import gzip
from pathlib import Path
import struct
import subprocess

DENSITIES = ("mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi")


def check(root: Path, product_out: Path | None = None):
    root = root.resolve()
    kernel = root / "kernel/google/msm-4.14"
    suite = root / "vendor/hecker/floral/suite"
    no_root = (".gitmodules", "KernelSU", "drivers/kernelsu", "fs/susfs.c",
               "include/linux/susfs.h", "include/linux/susfs_def.h")
    for path in no_root:
        if (kernel / path).exists() or (kernel / path).is_symlink():
            raise ValueError("Non-KSU kernel contains root integration: " + path)
    kconfig = (kernel / "arch/arm64/configs/floral_defconfig").read_text()
    if "CONFIG_KSU" in kconfig or "CONFIG_KSU_SUSFS" in kconfig:
        raise ValueError("KernelSU is enabled in non-KSU defconfig")
    for density in DENSITIES:
        rel = f"res-{density}/images/logo_image.png"
        expected = suite / "recovery" / rel
        installed = root / "bootable/recovery" / rel
        if not installed.is_file() or installed.read_bytes() != expected.read_bytes():
            raise ValueError("Native PixelOS recovery is missing HeckerOS artwork: " + rel)
    if (root / "system/core/init/hecker_recovery_boot.cpp").exists():
        raise ValueError("OrangeFox dual-mode init is present in non-KSU source")
    make = (root / "build/make/core/Makefile").read_text()
    if ("hecker_recovery2_rom install" in make or
            "hecker-recovery2-coral.cpio.gz" in make):
        raise ValueError("OrangeFox packaging rule present in non-KSU source")
    # Run the kernel's stronger provenance/integrity/root-symbol checks too.
    subprocess.run(["python3", str(kernel / "tools/hecker/verify_nonksu.py"),
                    "--source-root", str(kernel)], check=True)
    if product_out is not None:
        boot = product_out / "boot.img"
        if not boot.is_file():
            raise ValueError("Non-KSU full ROM output is missing boot.img")
        with boot.open("rb") as img:
            header = img.read(4096)
            if header[:8] != b"ANDROID!":
                raise ValueError("Not an Android boot image")
            kernel_len, ramdisk_len = struct.unpack_from("<II", header, 8)
            page_size, header_version = struct.unpack_from("<II", header, 36)
            if page_size != 4096 or header_version != 2:
                raise ValueError("Unexpected Coral Android boot header")
            if ramdisk_len <= 0 or ramdisk_len > 60 * 1024 * 1024:
                raise ValueError("Invalid native recovery ramdisk")
            offset = page_size + ((kernel_len + page_size - 1) // page_size) * page_size
            img.seek(offset)
            compressed = img.read(ramdisk_len)
        try:
            ramdisk = gzip.decompress(compressed)
        except (OSError, EOFError) as error:
            raise ValueError("Failed to decompress Coral boot ramdisk") from error
        if (b"hecker-recovery.cpio.zst" in ramdisk or
                b"Starting OrangeFox-based Hecker Recovery" in ramdisk or
                b"twres/pages/main.xml" in ramdisk):
            raise ValueError("OrangeFox payload found in non-KSU boot.img")
    print("Coral NonKSU: no KernelSU/SUSFS, native PixelOS HeckerOS recovery only: PASS")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rom-root", type=Path, default=Path.cwd())
    parser.add_argument("--product-out", type=Path)
    args = parser.parse_args()
    try:
        check(args.rom_root, args.product_out)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        raise SystemExit("Non-KSU Coral recovery/root validation: " + str(error))
