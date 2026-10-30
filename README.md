# HeckerOS coral build integration

Coral local-manifest baseline for HeckerOS Android 17 on Google Pixel 4 XL (`coral`).
The commands below build this `main` baseline. For the newer Living Flow polish
and October platform update, use the [matching Coral feature build guide](https://github.com/its-hecker/HeckerOs-localmanifest/blob/feat/living-flow-polish-20261030/README.md#complete-build-from-mkdir).
Pixel 4 (`flame`) has a [separate local manifest](https://github.com/its-hecker/HeckerOs-Flame-localmanifest).

The manifest pins the dedicated HeckerOS device, vendor and kernel imports, Motion Sense/3D Face Unlock plugins, Settings/framework baselines, launcher and HeckerOS integration. UI pages live directly in native Settings; supporting feature services remain system components.

## Complete build from mkdir

```bash
mkdir -p ~/heckeros-coral &&
cd ~/heckeros-coral &&
git lfs install &&
repo init -u https://github.com/its-hecker/HeckerOS.git -b main --git-lfs &&
git clone --branch main --single-branch https://github.com/its-hecker/HeckerOs-localmanifest.git .repo/local_manifests &&
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags &&
HECKER_DEVICE=coral HECKER_BUILD_VARIANT=userdebug HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

Copy the entire block in the initialized build shell. The `&&` chain stops
at the first failure; the helper performs environment setup, target selection,
preparation and compilation. Keep ServerHive's existing RBE settings.

Run these commands in a fresh Android source directory with the normal AOSP build prerequisites, Git LFS, Python 3, Pillow and numpy. The script prepares original APKs, theme assets and guarded source adapters, then builds `hecker_coral-hecker_suite-userdebug` with `m heckeros`. It does not sign or publish a release.

Source/host checks pass. A complete Settings APK/Soong build, ROM boot and coral hardware tests remain required. This is a source integration checkpoint, not a tested flashable release.

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
