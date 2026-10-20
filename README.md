# HeckerOS coral build integration

Coral-first local manifest for HeckerOS Android 17. This repository currently has one branch (`main`) and targets Google Pixel 4 XL (`coral`). Pixel 4 (`flame`) support follows coral hardware testing.

The manifest pins the dedicated HeckerOS device, vendor and kernel imports, Motion Sense/3D Face Unlock plugins, Settings/framework baselines, launcher and HeckerOS integration. UI pages live directly in native Settings; supporting feature services remain system components.

## Sync and build

```bash
repo init -u https://github.com/its-hecker/HeckerOS -b main --git-lfs
git clone https://github.com/its-hecker/HeckerOs-localmanifest .repo/local_manifests
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags
bash .repo/local_manifests/build.sh
```

Run these commands in a fresh Android source directory with the normal AOSP build prerequisites, Git LFS, Python 3, Pillow and numpy. The script prepares original APKs, theme assets and guarded source adapters, then builds `hecker_coral-hecker_suite-userdebug` with `m heckeros`. It does not sign or publish a release.

Source/host checks pass. A complete Settings APK/Soong build, ROM boot and coral hardware tests remain required. This is a source integration checkpoint, not a tested flashable release.

Maintainer: Hecker

[HeckerOS sources](https://github.com/its-hecker/HeckerOS) · [Channel](https://t.me/pixel4seriesupdates) · [Support](https://t.me/Pixel4Roms)
