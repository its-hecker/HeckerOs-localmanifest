# HeckerOS Coral build integration

This `fix/device-ui-feedback-20261101` branch selects the reviewed November 1
Suite fixes, based on the existing Living Flow polish configuration. It retains
the low-brightness protection, FaceID, root-privacy, Motion Sense, NetLab, Game
Space and October upstream changes. This update is Coral only.

The source changes repair Launcher search/icon scope, custom clock application,
shared lyrics and status rows, Settings/Suite layout, media transitions and
Motion Sense animation. Automatic depth extraction uses pinned inputs prepared
by the build helper before Soong. The four binary dependencies are fetched to
the build machine and verified against the reviewed SHA-256 hashes. No model
download happens on the phone. `build.sh --offline` requires valid cached inputs.
Full ROM compilation and Coral phone testing remain pending.

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

## Display double-tap to sleep

The existing Settings → Display switch now controls sleep from the collapsed
status bar and native lockscreen, with live foreground-user preference updates.
Native AOD wake and lockscreen state handling remain in place. See
[the cause, implementation and phone checks](https://github.com/its-hecker/HeckerOS/blob/feat/living-flow-polish-20261030/docs/double-tap-sleep.md).

## Reference About phone

The compact About home follows the supplied reference with a rounded HeckerOS
brand card, device name, Android/processor tiles, joined information rows and
Credits & legal. The card shares the media player’s blue/lavender glow geometry,
colours and absolute-time 7.2-second cycle. Native rename, detail pages, legal,
search and build-number handling remain available. The current Hecker Suite UI
is retained. See
[implementation, preview and phone checks](https://github.com/its-hecker/HeckerOS/blob/feat/living-flow-polish-20261030/docs/about-phone-reference.md).

The production glow lifecycle, prepared native navigation, source/translation
checks and 136 host tests pass. Full ROM and Coral phone validation are pending.

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

## Build commands after publication

These commands select the reviewed UI and additional pill/sensor-recovery
changes in both repositories. Suite is pinned to published source commit
`6e192a1c57dcc5f1cd52cdb59632e811f3ee1adf`.

## Complete build from mkdir

Use a fresh directory in the provider's initialized Byobu/Tmux/RBE shell, with
Android 17 build dependencies, Repo, Git LFS, Python, Pillow and numpy installed.
Copy the whole block; `&&` stops it at the first failure.

```bash
mkdir -p ~/heckeros-coral &&
cd ~/heckeros-coral &&
git lfs install &&
repo init -u https://github.com/its-hecker/HeckerOS.git -b fix/device-ui-feedback-20261101 --git-lfs &&
git clone --branch fix/device-ui-feedback-20261101 --single-branch https://github.com/its-hecker/HeckerOs-localmanifest.git .repo/local_manifests &&
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags &&
HECKER_DEVICE=coral HECKER_BUILD_VARIANT=userdebug HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

## Existing Coral checkout

From the Android source root:

```bash
repo init -u https://github.com/its-hecker/HeckerOS -b fix/device-ui-feedback-20261101 --git-lfs &&
git -C .repo/local_manifests fetch origin fix/device-ui-feedback-20261101 &&
git -C .repo/local_manifests switch --detach FETCH_HEAD &&
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags &&
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

The build helper retains the ServerHive RBE environment. Keep it in the normal
initialized build session. It uses the native Settings and Hecker Suite product
release and retires obsolete launcher/OmniJaws source with backups. Preserve
unrelated local edits; the source adapters reject unfamiliar changes.

## Validation

Current preparation: 158 Suite Python host tests, the remaining Java/C++ and
production Shell checks, complete locked SDK Java/resources/AIDL compilation,
77 Coral manifest integration tests, pin validation and build-script syntax
checks passed. The original reviewed native/Compose adapter validation remains
recorded in the Suite review. Full ROM compilation and phone tests are pending.

## Additional GameSpace and proximity recovery work

The selected source centers GameSpace floating-pill labels and values and
adds the manual root-authorized Sensor recovery page and QS tile.
The companion shell helper can be tested separately on an existing rooted
PixelOS build. It restarts an allowlisted running Sensors HAL and verifies a
changed process ID; physical near/far recovery still needs a cover/uncover
test on the affected phone. It does not reset calibration or bypass Face Unlock
proximity checks. See docs/GAME_PILL_SENSOR_RECOVERY_2026-11-01.md in Suite.

The current Suite changes pass 158 host tests, including 12 helper behavior
cases, plus complete SDK Java/resources/AIDL and independent Settings dashboard
compilation. Full ROM and affected-device testing remain pending.
