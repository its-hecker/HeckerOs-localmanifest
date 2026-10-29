# HeckerOS Coral build integration

This `feat/statusbar-lyrics-dual-20261029` branch selects Suite
`b976e56ce5458e74db7a854a023611c92d374f50`. It retains the previous experimental low-brightness
framework/device pins, root-privacy kernel, Caracal v2 Home/Lock depth layers,
NetLab and Game Space work. Both new status-bar switches default off.

## Status-bar lyrics and dual rows

Separate default-off switches under Hecker Suite → Status bar control synchronized
status lyrics and two native rows. The LRCLIB media engine/cache is shared with the
independently enabled lock screen, and remains subscribed while unlocked.
Controls include 44/52/60 dp native heights, row spacing/icon size, notification or
lyric second-row layouts, and lyric alignment/width/font/colour/fade/marquee.
Built-in signed framework overlays update app and SystemUI insets together; the
native theme service mirrors the foreground user's height into system resources.

See [implementation, controls and phone acceptance](https://github.com/its-hecker/HeckerOS/blob/feat/statusbar-lyrics-dual-20261029/docs/statusbar-lyrics-dual.md).
SDK/Compose, provider/geometry/overlay host checks and both framework adapter
revisions pass. Full Soong builds and physical phone validation remain required.

## Living Flow

- ColorOS 17-inspired tall, horizontal and bold lock clocks, matching monochrome
  AOD geometry and an optional matching Hecker Home clock.
- Native doze-driven wake/sleep motion, aligned depth layers and a GPU blur reveal.
- ColorOS-style Hecker QS: connectivity pills, live media, paired vertical controls,
  round tiles, translucent surfaces and spring press feedback.
- Brightness and volume percentages stay visible; One UI QS remains available.
- Shared native folder/icon settling, default Shell app/Home transitions, and tuned
  native clip/scale launch curves retaining their icon-origin geometry.

See [implementation, previews, controls and limits](https://github.com/its-hecker/HeckerOS/blob/b976e56ce5458e74db7a854a023611c92d374f50/docs/living-flow.md).
Pixel Launcher still owns Recents; its remote Recents/swipe-home animations are
not replaced. This is source implementation, not a validated ROM release.

## Existing Coral checkout

From the Android source root:

```bash
git -C .repo/local_manifests fetch origin feat/statusbar-lyrics-dual-20261029
git -C .repo/local_manifests switch feat/statusbar-lyrics-dual-20261029
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

The build helper retains the ServerHive RBE environment. Keep it in the normal
initialized build session. It uses the native Settings and Hecker Suite product
release and retires obsolete launcher/OmniJaws source with backups. Preserve
unrelated local edits; the source adapters reject unfamiliar changes.

## Fresh Coral checkout

```bash
repo init -u https://github.com/its-hecker/HeckerOS -b main --git-lfs
git clone -b feat/statusbar-lyrics-dual-20261029 https://github.com/its-hecker/HeckerOs-localmanifest .repo/local_manifests
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

## Validation

Suite: 132 Python host tests, existing Java/C++ regressions and production Shell
motion checks; 81 integration tests; locked SDK Java/resources/AIDL; SystemUI
Compose; 17,496 production clock frames; native Launcher helpers/resources; pinned
source adapters, published Living Flow upgrades, repeat application and exact reversion.
The matching manifest's integration tests and pin validation also pass.

A full Soong build, boot and Coral phone tests remain required for font/layout
parity, AOD/lock/Home handoff, blur availability, fast reversal, frame pacing and
low-brightness behavior. This is not a claim of the complete proprietary engine,
identical animations or a guaranteed 90-fps result.

Flame has a [matching feature manifest](https://github.com/its-hecker/HeckerOs-Flame-localmanifest/tree/feat/statusbar-lyrics-dual-20261029), retaining its own hardware/framework/kernel pins; its optional non-KSU build has a separate matching branch.
