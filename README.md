# HeckerOS coral root-privacy test

Experimental local manifest for HeckerOS Android 17 on Google Pixel 4 XL (`coral`). All root-privacy changes are isolated on `test/coral-root-privacy-20261027`; stable branches and the Flame manifest are unchanged. Do not use this as a release build before kernel/ROM and Coral device testing.

The manifest pins the dedicated HeckerOS device, vendor and kernel imports, Motion Sense/3D Face Unlock plugins, Settings/framework baselines, launcher and HeckerOS integration. UI pages live directly in native Settings; supporting feature services remain system components.

## Sync and build

```bash
mkdir -p ~/heckeros-coral-root-test
cd ~/heckeros-coral-root-test
repo init -u https://github.com/its-hecker/HeckerOS -b test/coral-root-privacy-20261027 --git-lfs
git clone -b test/coral-root-privacy-20261027 https://github.com/its-hecker/HeckerOs-localmanifest .repo/local_manifests
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

Run these commands in a fresh Android source directory with the normal AOSP build prerequisites, Git LFS, Python 3, Pillow and numpy. The script prepares original APKs, theme assets and guarded source adapters, then builds `hecker_coral-hecker_suite-userdebug` with `m heckeros`. It does not sign or publish a release.

Suite Java/resource checks, host privacy-policy tests and real Coral kernel configuration generation passed. The local kernel object build stopped at compiler/toolchain validation. A full production kernel/ROM build, boot and Coral hardware tests remain required. UBL compatibility is not confirmed.

After a successful build, use **Hecker Suite → Root manager privacy** to select test apps. Keep their root access disabled and enable **Umount modules** in KernelSU, then close and reopen the apps. Native Detector's framework-resource warning remains expected. See the [Coral test notes](https://github.com/its-hecker/HeckerOS/blob/test/coral-root-privacy-20261027/docs/coral-root-privacy.md).

Maintainer: Hecker

[HeckerOS sources](https://github.com/its-hecker/HeckerOS) · [Channel](https://t.me/pixel4seriesupdates) · [Support](https://t.me/Pixel4Roms)

The current pins select the stock Pixel pose-grid renderer and the Axion-derived
PIF, game profile, keybox import and TrickyStore integration in native Settings.
Photos retains PixelOS's existing implementation. Open Settings > Hecker's Suite >
Play Integrity to configure profiles, targets and your keybox; restart the phone
after changing them. No keybox is bundled. Actual enrollment and attestation
verdict testing remain required. Four platform projects use owned HeckerOS forks;
the other 87 stay at their existing upstream repositories with exact source pins.
Bulk repository migration is optional and does not block this build.
