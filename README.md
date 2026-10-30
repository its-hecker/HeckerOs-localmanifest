# HeckerOS Coral build integration

This `feat/living-flow-polish-20261030` branch selects Suite
`4f2b448ce4bfde529f8987042d3ff43b1c14a89e`, the screenshot-reference Living Flow polish and the reviewed
PixelOS/Lineage October update. It retains the low-brightness protection, FaceID,
root-privacy, Motion Sense, NetLab and Game Space work. This update is Coral only.

## Living Flow polish and upstream updates

Tall translucent clock with bundled preview font, continuous doze/mask reveal,
separate Harbor Home depth layers, additional outline icons and compact search,
colour-based outlined battery, animated blue/lavender media glow and consistent
QQS/full-QS blur for Hecker and One UI layouts. The native Quick QS player now
flows into either full player using shared scene bounds. Tall lock clock digits
converge toward Home without replaying an independent Home reveal. The current
Suite UI is retained.

PixelOS framework/security/privacy, certificate trust, libmeminfo and vendor updates
are pinned alongside five Lineage kernel cgroup fixes. The Lineage device and
Muppets vendor bases are already included; their pins remain unchanged. The
platform release flag is 2026-10-01; vendor/firmware patch levels are unchanged.

See [implementation and validation](https://github.com/its-hecker/HeckerOS/blob/feat/living-flow-polish-20261030/docs/living-flow-polish.md)
[media glow and handoffs](https://github.com/its-hecker/HeckerOS/blob/feat/living-flow-polish-20261030/docs/media-glow-handoff.md),
and [upstream review](https://github.com/its-hecker/HeckerOS/blob/feat/living-flow-polish-20261030/docs/coral-upstream-review-2026-10-30.md).

## Status-bar lyrics and dual rows

Separate default-off switches under Hecker Suite → Status bar control synchronized
status lyrics and two native rows. The LRCLIB media engine/cache is shared with the
independently enabled lock screen, and remains subscribed while unlocked.
Controls include 44/52/60 dp native heights, row spacing/icon size, notification or
lyric second-row layouts, and lyric alignment/width/font/colour/fade/marquee.
Built-in signed framework overlays update app and SystemUI insets together; the
native theme service mirrors the foreground user's height into system resources.

See [implementation, controls and phone acceptance](https://github.com/its-hecker/HeckerOS/blob/feat/living-flow-polish-20261030/docs/statusbar-lyrics-dual.md).
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

## Complete build from mkdir

Use a fresh directory in the provider's initialized Byobu/Tmux/RBE shell, with
Android 17 build dependencies, Repo, Git LFS, Python, Pillow and numpy installed.
Copy the whole block; `&&` stops it at the first failure.

```bash
mkdir -p ~/heckeros-coral &&
cd ~/heckeros-coral &&
git lfs install &&
repo init -u https://github.com/its-hecker/HeckerOS.git -b feat/living-flow-polish-20261030 --git-lfs &&
git clone --branch feat/living-flow-polish-20261030 --single-branch https://github.com/its-hecker/HeckerOs-localmanifest.git .repo/local_manifests &&
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags &&
HECKER_DEVICE=coral HECKER_BUILD_VARIANT=userdebug HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

## Existing Coral checkout

From the Android source root:

```bash
repo init -u https://github.com/its-hecker/HeckerOS -b feat/living-flow-polish-20261030 --git-lfs
git -C .repo/local_manifests fetch origin feat/living-flow-polish-20261030
git -C .repo/local_manifests switch feat/living-flow-polish-20261030
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

The build helper retains the ServerHive RBE environment. Keep it in the normal
initialized build session. It uses the native Settings and Hecker Suite product
release and retires obsolete launcher/OmniJaws source with backups. Preserve
unrelated local edits; the source adapters reject unfamiliar changes.

## Validation

Suite: 135 Python host tests, existing Java/C++ regressions and production Shell
motion checks; 82 integration tests; locked SDK Java/resources/AIDL; SystemUI
Compose; 35,514 production clock frames; 72,072 media layout/reversal samples
at three font scales; native Launcher helpers/resources; pinned
source adapters, published Living Flow upgrades, repeat application and exact reversion.
The matching manifest's integration tests and pin validation also pass.

A full Soong build, boot and Coral phone tests remain required for font/layout
parity, AOD/lock/Home handoff, blur availability, fast reversal, frame pacing and
low-brightness behavior. This is not a claim of the complete proprietary engine,
identical animations or a guaranteed 90-fps result.

Flame manifests, hardware pins and product files were not advanced by this update.
