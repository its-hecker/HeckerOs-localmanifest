# SPDX-License-Identifier: Apache-2.0
"""Checks source separation of regular Coral and native-recovery non-KSU variants."""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class CoralNonKSUTests(unittest.TestCase):
    def test_kernel_manifest_is_pinned_and_never_syncs_kernelsu(self):
        projects = ET.parse(ROOT / "floral.xml").getroot()
        kernel = projects.find("project[@path='kernel/google/msm-4.14']")
        self.assertIsNotNone(kernel)
        self.assertEqual(kernel.get("name"), "its-hecker/HeckerOsfloral-Kernel-NonKsu")
        self.assertEqual(kernel.get("upstream"), "refs/heads/main")
        self.assertNotEqual(kernel.get("sync-s"), "true")
        self.assertRegex(kernel.get("revision"), r"^[0-9a-f]{40}$")

    def test_build_keeps_separate_full_rom_and_native_recovery(self):
        build = (ROOT / "build.sh").read_text()
        self.assertIn('OUT_DIR="${HECKER_NONKSU_OUT_DIR:-out}"', build)
        self.assertIn("export HECKER_RECOVERY2=0", build)
        self.assertIn("export HECKER_DEV_USB_ADB=false", build)
        self.assertIn("m heckeros", build)
        self.assertNotIn("recovery2_rom.py download", build)
        self.assertIn("check_native_nonksu.py", build)
        self.assertIn("verify_nonksu.py", build)

    def test_usb_debugging_off_and_authenticated_adb_in_product(self):
        import tempfile
        from tools.check_native_nonksu import check_usb_debugging_off

        with tempfile.TemporaryDirectory() as temporary:
            product_out = Path(temporary)
            props = product_out / "product/etc/build.prop"
            props.parent.mkdir(parents=True)
            props.write_text("ro.heckeros.dev_usb_adb=0\nro.adb.secure=1\n"
                             "persist.sys.usb.config=mtp\n")
            check_usb_debugging_off(product_out)
            props.write_text("ro.heckeros.dev_usb_adb=1\nro.adb.secure=0\n"
                             "persist.sys.usb.config=adb\n")
            with self.assertRaisesRegex(ValueError, "development USB debugging"):
                check_usb_debugging_off(product_out)
            props.write_text("ro.heckeros.dev_usb_adb=0\nro.adb.secure=1\n"
                             "persist.sys.usb.config=mtp,adb\n")
            with self.assertRaisesRegex(ValueError, "must not enable ADB"):
                check_usb_debugging_off(product_out)

    def test_boot_guard_requires_branding_and_rejects_orangefox(self):
        guard = (ROOT / "tools/check_native_nonksu.py").read_text()
        self.assertIn("bootable/recovery", guard)
        self.assertIn("hecker-recovery.cpio.zst", guard)
        self.assertIn("KernelSU", guard)
        self.assertIn("logo_image.png", guard)


if __name__ == "__main__":
    unittest.main()
