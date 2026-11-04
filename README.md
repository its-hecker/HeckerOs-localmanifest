# HeckerOS Coral build integration

## HeckerVPN feature branch — 4 November 2026

`feat/heckervpn-20261104` pins source `b7b7efa99ee8b6dc65b40915e55bfdf2a483e78b`.
It adds **HeckerLab → HeckerVPN** with a Mullvad country/server adapter, manual
WireGuard `.conf` import, per-profile app routing, connection statistics and a QS
tile. The init-owned kernel controller does not request a KSU/Magisk grant or
require the separate WireGuard app. Provider countries require each user's own
valid Mullvad account; manual imports support other compatible providers. No
server hosting or shared/free endpoint service is included.

Local Android/AIDL/resource/native-tool compilation, provider protocol fixtures,
188 existing Python tests, the complete host test script, and standalone pinned
platform SELinux smoke checks passed. Actual device policy/Soong compilation,
Mullvad account provisioning and Coral phone traffic/leak/recovery checks remain
pending. This feature is not a device-tested release.

After the source and matching manifest branches are published, an existing Coral
checkout can use the following incremental build command with **RBE and default
jobs**, preserving `out/`:

```bash
cd ~/heckeros-coral &&
git -C .repo/manifests fetch origin feat/heckervpn-20261104 &&
git -C .repo/manifests switch --detach FETCH_HEAD &&
git -C .repo/local_manifests fetch origin feat/heckervpn-20261104 &&
git -C .repo/local_manifests switch --detach FETCH_HEAD &&
repo sync -c --fail-fast --no-clone-bundle --no-tags &&
env -u HECKER_BUILD_JOBS USE_RBE=true HECKER_DEVICE=coral HECKER_BUILD_VARIANT=userdebug \
    bash .repo/local_manifests/build.sh
```

Implementation and acceptance checks are documented in the source repository at
`docs/heckervpn-2026-11-04.md`.

## Coral UI and compatibility — 2 November 2026

**4 November Launcher build fix:** correct the unresolved wallpaper Settings
constant in native Launcher Kotlin. Existing prepared sources upgrade in place;
keep `out/` for the incremental build. Compile the actual patched wallpaper method
against the locked SDK and verify its exported handler in pinned Settings. All
188 host tests and native checks against 136 pinned files pass; full ROM build and
physical Coral validation remain pending. See [cause and rebuild](https://github.com/its-hecker/HeckerOS/blob/33237726f64cc7d5bcade4783c5529d84d8114b7/docs/coral-launcher-wallpaper-build-fix-2026-11-04.md).

**4 November HeckerLab and device feedback:** select the complete UI/media/depth
update, including consistent English word-clock AOD, stable Home depth during
app/unlock transitions, immediate workspace double-tap sleep, a working wallpaper
picker fallback and automatic lock-wallpaper extraction. Add media **Hide** and
**Close app**, common Quick/full-QS blur with an **85% default**, corrected icon
fallbacks, cold-start lyrics callbacks and automatic GameSpace shutdown/restart.
Motion Island adds the three reference characters, individual gestures, skip/resume
continuity and **26–56 dp** bar height. Visible Hecker Suite names are now **HeckerLab**;
existing package IDs and settings remain compatible. The source passed 187 host
tests, locked Suite/Settings/SystemUI/Launcher compilation and native apply/upgrade/
revert checks against 135 pinned files. Full Android/Soong and Coral phone tests
remain pending. See [changes, controls and phone checks](https://github.com/its-hecker/HeckerOS/blob/33237726f64cc7d5bcade4783c5529d84d8114b7/docs/coral-heckerlab-feedback-2026-11-04.md).

**4 November native XMorphClock:** select all 86 upstream clock presets and 47
bundled fonts in HeckerLab → Lock screen → Custom clock → XMorphClock styles.
The native SystemUI renderer supports small/large clocks, AOD and the shared depth
mask without root or Xposed. Original assets, licenses and author credit are
included. Locked library, catalog, packaging, Suite and SystemUI checks pass;
full ROM compilation and Coral phone validation remain pending. See
[implementation and phone checks](https://github.com/its-hecker/HeckerOS/blob/33237726f64cc7d5bcade4783c5529d84d8114b7/docs/xmorph-clock-native-2026-11-04.md).

**4 November stock/plugin clock depth:** select the native clock masking
adapter. Depth now follows stock and installed SystemUI plugin clocks in their
small/large native elements. Imports and depth toggles preserve the selected
clock mode. Keep Custom clock off for stock/plugin styles. Locked Java/Compose,
resource, mask geometry, extraction-selection and upgrade checks pass; full
ROM/phone validation is pending. See [implementation and use](https://github.com/its-hecker/HeckerOS/blob/fix/coral-ui-compatibility-20261102/docs/stock-clock-depth-2026-11-04.md).

**4 November Settings crash fix:** select the corrected homepage lifecycle
adapter. Divider suppression now runs after AndroidX initializes its list, and
existing prepared sources upgrade automatically. Host crash reproduction,
recreation, source-upgrade and Settings resource/adapter checks pass; the rebuilt
ROM still needs phone validation. Keep `out/` for an incremental rebuild. See
[cause and rebuild](https://github.com/its-hecker/HeckerOS/blob/fix/coral-ui-compatibility-20261102/docs/settings-home-crash-2026-11-04.md).

**3 November launcher/depth update:** select the refreshed Launcher Studio and
depth fixes: dedicated signature access to Home layers, adjustable clock/search
height and clock information position, manual subject alignment, current-lock
wallpaper extraction/retry, all built-in Hecker lock-clock styles, a visible QS
preview and explicitly scoped Home/lock controls. Remove the Caracal Dawn action
and leftover PixelOS Developer options spoof controls. Exact prepared-source
copies upgrade in place. See [changes and phone checks](https://github.com/its-hecker/HeckerOS/blob/fix/coral-ui-compatibility-20261102/docs/coral-ui-depth-feedback-2026-11-03.md).

**3 November boot fix:** select the corrected Cyrillic font adapter. The previous
adapter put `lang="und-Cyrl"` inside named font lists, causing Zygote to fail while
preloading Typeface. The exact previously prepared XML upgrades automatically;
the final built-output check verifies the installed XML and both font subsets.
Host tests with the pinned Android parsers reproduce the old crash and accept
the correction. A rebuilt ROM and phone test are pending.
See [boot cause and rebuild](https://github.com/its-hecker/HeckerOS/blob/fix/coral-ui-compatibility-20261102/docs/coral-font-boot-fix-2026-11-03.md).

**3 November build fix:** the ROM-visibility helper now fits Bionic's 2 KiB
stack-frame limit. The helper is upgraded automatically from the reviewed old
copy. ARM/ARM64 platform/APEX object checks and boundary tests pass; the resumed
ServerHive image build remains pending. Keep the existing `out/` directory.
See [cause and validation](https://github.com/its-hecker/HeckerOS/blob/fix/coral-ui-compatibility-20261102/docs/coral-bionic-stack-fix-2026-11-03.md).

This `fix/coral-ui-compatibility-20261102` branch adds independent AOD clock
sizing, adjustable lighter QS blur, native media visibility and reduced per-frame
work, single Settings card backgrounds, a colored GameSpace icon and Google Sans
Cyrillic fallback fonts under the OFL.

App compatibility retains the four existing switches and adds **Hide custom ROM**.
The reviewed VoltageOS Bionic hooks use an opt-in app flag. The build also restricts
Lineage service discovery for untrusted app domains and excludes `addon.d` from
Coral images. Removing `addon.d` disables preservation of add-on packages across
ROM updates; it does not inherently prevent their initial installation.

The Suite and framework revisions below are pinned together.

| Source | Exact revision |
| --- | --- |
| Suite | `33237726f64cc7d5bcade4783c5529d84d8114b7` |
| Framework | `4af276bc5ceea071ef0da5ea440cda4470c08df6` |

 Full Android/APEX/
SELinux compilation and phone tests remain pending. Pixel Launcher weather still
needs Smartspace diagnostics; UBL compatibility and hardware attestation are not
established as fixed. Existing hardware, kernel, camera and RBE configuration is
retained. This integration update selects Coral only.

See [changes, controls and acceptance](https://github.com/its-hecker/HeckerOS/blob/fix/coral-ui-compatibility-20261102/docs/coral-feedback-2026-11-02.md)
and [compatibility coverage and limits](https://github.com/its-hecker/HeckerOS/blob/fix/coral-ui-compatibility-20261102/docs/app-compatibility.md).

Source checks pass: 188 Suite Python tests, 83 shared integration tests, 78
Coral manifest tests, 2,590 installer/Settings policy assertions, Suite SDK/resource
compilation and native adapter/ABI checks. Full ROM and phone acceptance remain
pending. With `HECKER_BUILD_JOBS` unset, `build.sh` runs `m heckeros` and leaves
parallelism to Android; existing RBE variables are retained.

The older sections below document inherited features.

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

Separate default-off switches under HeckerLab → Status bar control synchronized
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
`33237726f64cc7d5bcade4783c5529d84d8114b7`.

## Complete build from mkdir

Use a fresh directory in the provider's initialized Byobu/Tmux/RBE shell, with
Android 17 build dependencies, Repo, Git LFS, Python, Pillow and numpy installed.
Copy the whole block; `&&` stops it at the first failure.

```bash
mkdir -p ~/heckeros-coral &&
cd ~/heckeros-coral &&
git lfs install &&
repo init -u https://github.com/its-hecker/HeckerOS.git -b fix/coral-ui-compatibility-20261102 --git-lfs &&
git clone --branch fix/coral-ui-compatibility-20261102 --single-branch https://github.com/its-hecker/HeckerOs-localmanifest.git .repo/local_manifests &&
repo sync -c --fail-fast --no-clone-bundle --no-tags &&
env -u HECKER_BUILD_JOBS USE_RBE=true HECKER_DEVICE=coral HECKER_BUILD_VARIANT=userdebug bash .repo/local_manifests/build.sh
```

## Existing Coral checkout

From the Android source root:

```bash
repo init -u https://github.com/its-hecker/HeckerOS -b fix/coral-ui-compatibility-20261102 --git-lfs &&
git -C .repo/local_manifests fetch origin fix/coral-ui-compatibility-20261102 &&
git -C .repo/local_manifests switch --detach FETCH_HEAD &&
repo sync -c --fail-fast --no-clone-bundle --no-tags &&
env -u HECKER_BUILD_JOBS USE_RBE=true HECKER_DEVICE=coral HECKER_BUILD_VARIANT=userdebug bash .repo/local_manifests/build.sh
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
