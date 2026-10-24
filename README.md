# HeckerOS coral build integration

Coral-first local manifest for HeckerOS Android 17 targeting Google Pixel 4 XL (`coral`). The `feat/about-phone-official` branch carries the current About Phone, branding and build fixes. Pixel 4 (`flame`) support follows coral hardware testing.

The manifest pins the dedicated HeckerOS device, vendor and kernel imports, Motion Sense/3D Face Unlock plugins, Settings/framework baselines, launcher and HeckerOS integration. UI pages live directly in native Settings; supporting feature services remain system components.

## Sync and build

```bash
repo init -u https://github.com/its-hecker/HeckerOS -b main --git-lfs
git clone https://github.com/its-hecker/HeckerOs-localmanifest .repo/local_manifests
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags
bash .repo/local_manifests/build.sh
```

Run these commands in a fresh Android source directory with the normal AOSP build prerequisites, Git LFS, Python 3, Pillow and numpy. The script prepares original APKs, theme assets and guarded source adapters, then builds `hecker_coral-hecker_suite-userdebug` with `m heckeros`. It does not sign or publish a release.

## Upgrade an existing feature-branch checkout

OmniJaws has been removed. Its old checkout contains local source adaptations,
so move it aside before Repo removes the project:

```bash
cd ~/heckeros-coral
git -C .repo/local_manifests pull --ff-only
python3 .repo/local_manifests/tools/retire_omnijaws.py
repo sync -c -j2 --fail-fast --no-clone-bundle --no-tags vendor/hecker/floral/suite
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

The retirement helper preserves its files under `out/retired-projects/` and is
safe to rerun. The build helper clears staged app files with `installclean` only
when necessary, keeping compiled intermediates. Launcher weather retains the
separate Google feed when available. On ServerHive, use the initialized Byobu
build session and retain the provider's RBE environment.

Source/host checks pass. A complete Settings APK/Soong build, ROM boot and coral hardware tests remain required. This is a source integration checkpoint, not a tested flashable release.

Maintainer: Hecker

[HeckerOS sources](https://github.com/its-hecker/HeckerOS) · [Channel](https://t.me/pixel4seriesupdates) · [Support](https://t.me/Pixel4Roms)

The current pins select the native Hecker 25-cell pose-grid renderer and the Axion-derived
PIF, game profile, keybox import and TrickyStore integration in native Settings.
Photos retains PixelOS's existing implementation. Open Settings > Hecker's Suite >
Play Integrity to configure profiles, targets and your keybox; restart the phone
after changing them. No keybox is bundled. Actual enrollment and attestation
verdict testing remain required. Four platform projects use owned HeckerOS forks;
the other 87 stay at their existing upstream repositories with exact source pins.
Bulk repository migration is optional and does not block this build.


### Infinity Launcher and compact Game Space upgrade

The feature branch pins Infinity-X Android 17 from its official Gitea repository.
Before syncing an existing RisingOS-based checkout, preserve its local adapters:

```bash
cd ~/heckeros-coral
git -C .repo/local_manifests pull --ff-only
python3 .repo/local_manifests/tools/retire_launcher.py
python3 .repo/local_manifests/tools/retire_omnijaws.py
repo sync -c -j2 --fail-fast --no-clone-bundle --no-tags --force-sync vendor/hecker/floral/suite packages/apps/Launcher3 packages/apps/Settings
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

The migration helper keeps source files, untracked edits and a binary diff under
`out/retired-projects/`; rerunning it after the switch leaves Infinity-X intact.
The existing ServerHive RBE environment and product target remain in use.

Development builds also enable USB debugging and accept every connected PC
without an authorization prompt. For the final image, use
`HECKER_DEV_USB_ADB=false HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh`
to restore PC authorization, then flash the rebuilt ROM. The output verifier
checks that this flag reached the installed product properties. An existing
saved USB-debugging choice can survive a dirty flash; enable it in Settings if
needed for the test build.

The same update selects the enrollment grid on both Pixel 4 preview paths, themes
Compose Wi-Fi and cellular icons, fades the compact QS tray during expansion, and
shrinks the face-unlock feedback window. These changes need a new ROM build and
phone validation; syncing source does not update the running phone.

The follow-up phone fixes keep vertical brightness from moving into a horizontal
drag mirror, expose the lyrics page directly, observe saved theme changes in
SystemUI and separate the infrared camera buttons. Launcher selection stages a
choice while keeping the current HOME and Recents active. Use **Restart phone**
on Suite's Launcher page to change HOME and the highest-priority Recents overlay
together, with rollback on failure. The restart prompt checks Android's effective
Recents component too, so an enabled overlay at a lower priority can be repaired.

Bundled lock-screen clock providers are explicitly trusted by SystemUI's
production plugin policy. Dark boots fall back to the normal branded product
animation, whose installed size and hash are checked after building. Brightness
vector icons load as drawables instead of going through ImageDecoder.

## Game Booster reference dashboard

`feat/game-booster-reference` pins the Game Booster-style Suite and its matching
Floral kernel charging inhibitor. See the [implementation and build notes](https://github.com/its-hecker/HeckerOS/blob/feat/game-booster-reference/docs/game-booster.md).
Both `vendor/hecker/floral/suite` and `kernel/google/msm-4.14` must be synced before
running `build.sh`. These changes require a new ROM build and phone validation.

## Gaming SELinux fix and terminal boot animation

The Suite pin includes migration of the obsolete `hecker_game` / `activity_service`
mapping. Build preparation backs up the affected source files and removes that
fallback, retaining the dedicated `hecker_game_service` label and its access rules.
It also assembles Hecker's supplied terminal boot ZIP byte for byte from locked
binary chunks, validates all 210 PNG frames, and selects it for the product image.
CI validates the asset without restoring the retired animation.

For an existing `feat/game-booster-reference` checkout, run from the Android source root:

```bash
git -C .repo/local_manifests pull --ff-only origin feat/game-booster-reference
repo sync -c -j2 --fail-fast --no-clone-bundle --no-tags vendor/hecker/floral/suite
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

The existing build output can be reused. This update does not require a clean build.
