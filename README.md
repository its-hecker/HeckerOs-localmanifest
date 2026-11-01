# HeckerOS Coral build integration

## App compatibility

This branch adds a searchable full installed-app list under Hecker Suite →
App compatibility, with independent Root manager privacy, Allow app downgrade,
Hide developer options and Bootloader spoof switches. Existing privacy choices
are retained. Suite `6963155a0d449cf6a163c391c14c18fafd4cbd41` and framework `cc977dce02b883f8440c240c79996167210a13a1` are selected together.

The matching framework and Suite branches are published on GitHub and pinned
by this manifest. Full ROM/SELinux compilation and phone tests remain pending. The controls do not lock the bootloader or alter
hardware-backed attestation; UBL compatibility remains unproven.

Source validation for this work: 158 Suite host tests, 1,296 production installer
and Settings assertions, package/privacy and native-rule checks, complete Suite
Java/resources/AIDL and independent Settings dashboard compilation.

See [feature scope and acceptance](https://github.com/its-hecker/HeckerOS/blob/feat/app-compatibility-20261101/docs/app-compatibility.md).


This `feat/app-compatibility-20261101` branch selects the reviewed November 1
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

These commands select the reviewed UI, centered GameSpace pill, root-free sensor
recovery and Russian custom UI translations in both repositories. Suite is pinned to published source commit
`6963155a0d449cf6a163c391c14c18fafd4cbd41`.

## Complete build from mkdir

Use a fresh directory in the provider's initialized Byobu/Tmux/RBE shell, with
Android 17 build dependencies, Repo, Git LFS, Python, Pillow and numpy installed.
Copy the whole block; `&&` stops it at the first failure.

```bash
mkdir -p ~/heckeros-coral &&
cd ~/heckeros-coral &&
git lfs install &&
repo init -u https://github.com/its-hecker/HeckerOS.git -b feat/app-compatibility-20261101 --git-lfs &&
git clone --branch feat/app-compatibility-20261101 --single-branch https://github.com/its-hecker/HeckerOs-localmanifest.git .repo/local_manifests &&
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags &&
HECKER_DEVICE=coral HECKER_BUILD_VARIANT=userdebug HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

## Existing Coral checkout

From the Android source root:

```bash
repo init -u https://github.com/its-hecker/HeckerOS -b feat/app-compatibility-20261101 --git-lfs &&
git -C .repo/local_manifests fetch origin feat/app-compatibility-20261101 &&
git -C .repo/local_manifests switch --detach FETCH_HEAD &&
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags &&
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

The build helper retains the ServerHive RBE environment. Keep it in the normal
initialized build session. It uses the native Settings and Hecker Suite product
release and retires obsolete launcher/OmniJaws source with backups. Preserve
unrelated local edits; the source adapters reject unfamiliar changes.

## Validation

Inherited November 1 preparation: 158 Suite Python host tests, 452 production sensor-broker
assertions, complete locked SDK Java/resources/AIDL compilation and independent
Settings dashboard compilation passed. All ten Russian resource groups compile;
1,120 custom resources retain matching formatting arguments and array structure.
127 immutable native inputs pass fresh application, upgrade, repeat and revert
checks, including both Binder-service fuzzer bindings. Coral integration tests,
pin validation and build-script syntax checks passed. Full ROM/SELinux compilation
and phone tests are pending.

## Additional GameSpace, proximity recovery and Russian work

The selected source centers GameSpace floating-pill labels and values and
adds the manual Sensor recovery page and QS tile without requiring user root
access or a KernelSU grant. A platform-authenticated Binder broker requests
fixed init actions and verifies a changed running Sensors HAL process through
private init receipts. The app never runs su or a shell command. Recovery is
manual, limited to an awake, unlocked foreground user with no active call,
and has a cooldown.

Build and flash the matching updated ROM to obtain the broker, init rules and
SELinux policy; an APK update or an older stock/PixelOS image cannot provide
this service. The helper is now a root-free cmd client with no root fallback.
Physical near/far recovery still needs a cover/uncover test on the affected
phone. It does not reset calibration or bypass Face Unlock proximity checks.
See docs/GAME_PILL_SENSOR_RECOVERY_2026-11-01.md in Suite.

Russian covers 1,120 custom resources across Suite, Hecker Launcher, Settings,
SystemUI and NetLab. Select Russian in Android's system language settings.
Existing upstream Android/Google language packs remain under their own projects.
See docs/RUSSIAN_TRANSLATIONS_2026-11-01.md for coverage and typography limits.
