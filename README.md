# HeckerOS Coral build integration

This `feat/living-flow-20261029` branch selects Suite
`65f42ab27da9ce25fde3e1bb8862879cd78814f9`. It retains the previous experimental low-brightness
framework/device pins, root-privacy kernel, Caracal v2 Home/Lock depth layers,
NetLab and Game Space work.

## Living Flow

- ColorOS 17-inspired tall, horizontal and bold lock clocks, matching monochrome
  AOD geometry and an optional matching Hecker Home clock.
- Native doze-driven wake/sleep motion, aligned depth layers and a GPU blur reveal.
- ColorOS-style Hecker QS: connectivity pills, live media, paired vertical controls,
  round tiles, translucent surfaces and spring press feedback.
- Brightness and volume percentages stay visible; One UI QS remains available.
- Shared native folder/icon settling, default Shell app/Home transitions, and tuned
  native clip/scale launch curves retaining their icon-origin geometry.

See [implementation, previews, controls and limits](https://github.com/its-hecker/HeckerOS/blob/65f42ab27da9ce25fde3e1bb8862879cd78814f9/docs/living-flow.md).
Pixel Launcher still owns Recents; its remote Recents/swipe-home animations are
not replaced. This is source implementation, not a validated ROM release.

## Existing Coral checkout

From the Android source root:

```bash
git -C .repo/local_manifests fetch origin feat/living-flow-20261029
git -C .repo/local_manifests switch feat/living-flow-20261029
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
git clone -b feat/living-flow-20261029 https://github.com/its-hecker/HeckerOs-localmanifest .repo/local_manifests
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

## Validation

Suite: 128 Python host tests, existing Java/C++ regressions and production Shell
motion checks; 81 integration tests; locked SDK Java/resources/AIDL; SystemUI
Compose; 17,496 production clock frames; native Launcher helpers/resources; pinned
source adapters, d9a1ca7 upgrades, repeat application and exact reversion.
The matching manifest's integration tests and pin validation also pass.

A full Soong build, boot and Coral phone tests remain required for font/layout
parity, AOD/lock/Home handoff, blur availability, fast reversal, frame pacing and
low-brightness behavior. This is not a claim of the complete proprietary engine,
identical animations or a guaranteed 90-fps result.

Flame uses its own manifest and remains unchanged by this Coral integration.
