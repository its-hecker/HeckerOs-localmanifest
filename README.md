# HeckerOS coral build integration

Coral-first local manifest for HeckerOS Android 17 targeting Google Pixel 4 XL (`coral`). This `feat/settings-depth-lockscreen-20261028` experiment builds on the complete Coral root-privacy/astronaut test and adds the reference Settings homepage, animated word clock and imported-layer depth clock. Pixel 4 (`flame`) support follows successful Coral hardware testing.

The manifest pins the dedicated HeckerOS device, vendor and kernel imports, Motion Sense/3D Face Unlock plugins, Settings/framework baselines and HeckerOS integration. Hecker Launcher supplies HOME customizations; Pixel Launcher supplies Recents. UI pages live directly in native Settings; supporting feature services remain system components.

## Reference Settings and depth clock — 28 October 2026

The Suite is pinned to `2d531ce0c9c58bf46c80cf895064a8b493e6c880`. Settings retains the HeckerOS card and native controllers,
with grouped charcoal panels, coloured icons and a floating native Search pill.
Lockscreen controls add an English word clock with a melting smiley and rotating
starbursts, plus a large tall clock and a 750 ms depth reveal on wake.
Depth currently requires a prepared matching background and transparent foreground;
automatic subject extraction is not included. Existing device/framework/kernel,
Face Unlock, Soli, root-privacy and launcher/Recents dependencies are retained.

Validation covers 117 Suite host tests, 81 integration tests, owned app Java/resources/AIDL,
Settings adapters, SystemUI Compose and native source upgrade/revert checks. Full ROM
build, on-phone appearance, depth wake performance and Coral hardware tests remain pending.
The intermittent navigation freeze is **not claimed fixed**. The Suite adds a read-only
frozen/recovered diagnostics helper. See [feature details, artwork previews and gesture diagnostics](https://github.com/its-hecker/HeckerOS/blob/2d531ce0c9c58bf46c80cf895064a8b493e6c880/docs/settings-depth-lockscreen.md).

This branch changes the Suite selection only. Use its fresh-checkout recipe below;
the historical sections describe earlier work.

## Root privacy baseline correction — 27 October 2026

The initial root privacy test used the older Coral `main` pins. That was a baseline selection mistake. This branch now merges Suite Polish manifest `b09a85d3401a0f568f2e6568a370cc81d722ff63`, Suite `a51eacc198efe0a79a1f5e5e455c422064206e95`, kernel `48d6881fb8537f62811209927022e467d37e3a98` and framework `854e6dbf73ae1cd61095085a9655c8d9136104eb`. It retains the matching Settings/vendor pins, Pakistan IMS configuration, NetLab, Spoofing Hub and current build helpers. The exact corrected test pins are in `floral.xml` and `source-revisions.json`.

Stable branches and the Flame manifest are unchanged. All 112 Suite host tests and the Java/resources/AIDL/controller compilation checks pass, as do the framework visibility host checks. Full kernel/ROM builds, Coral boot and UBL/detector acceptance remain unverified. See the matching Suite's `docs/coral-root-privacy.md` for the test scope. Promote to Flame only after successful Coral testing.

## Simplified Network Lab device list — 26 October 2026

Network Lab now opens directly to a compact device list with Scan Wi-Fi and More.
Each device has a Manage menu for pause, upload/download speed limits, restore
and details. Multiple-device controls, traffic, network information, history,
diagnostics and advanced root controls are in More. Root identity scanning and
optional service-name discovery share the primary Scan action. Native hotspot
controls and root IPv4 controls retain their separate backends and privileges.
The existing single-session and selected-device restoration rules remain.

The same feature branch includes the reviewed launcher search spacing/gradient,
One UI charging animation and three optional right-side bolts, ambient Motion
Sense suppression, keybox certificate parsing/revocation handling and per-device
forwarding guards. Full ROM/phone acceptance is still required.

## Launcher, charging indicator and fetch follow-up — 26 October 2026

The accompanying Suite review reserves the whole below-dock search slot in native
Launcher3 grid sizing and hotseat padding. The search colours/border are muted,
with the existing wallpaper frosting retained. One UI battery animation now runs
in both the legacy status bar and Compose, including a visible full-fill shimmer.
Battery appearance provides an animation switch and optional right-side Classic,
Split or Spark bolts. Motion Sense glow is hidden during ambient/doze; no Oslo
ambient pulses are requested.

The Settings revision below normalizes downloaded certificate PEM to DER and
separates live revocation parsing errors from invalid chains. The NetLab native
helper now owns selected-peer FORWARD guards instead of refusing all sessions
when kernel forwarding is enabled. It preserves global forwarding, hotspot and
NAT configuration and supervises cleanup after relay death. NetLab still needs
an explicit KernelSU/root grant in this implementation.

These source changes require a complete Android build and device testing. The matching Settings/Suite/manifest changes are published together on
`feat/suite-polish`; ordinary repo sync resolves the pinned Settings source.

## Popup, glow, keybox and launcher follow-up — 26 October 2026

Suite `d760bfce1ca9e6c018cfaf7dcfcb6b38c1915172` removes the Android 17
SystemUI-only always-on-top launch option that rejected GameSpace popup apps.
Dashboard actions use three columns, with brightness/volume in the second control
row. The native hotseat owns the optional branded Hecker Search row. This historical change enabled Oslo ambient pulses; the later follow-up below disables ambient glow at the maintainer's request.

The matching dependencies are:

| Project | Immutable revision |
| --- | --- |
| Settings | `3831282d93ecda4d52a6894077482fe01ecea903` |
| frameworks/base | `854e6dbf73ae1cd61095085a9655c8d9136104eb` |

PIF follows current Evolution X Android 17 behavior; overlapping PixelOS certified
profile/blocking and legacy keybox call paths are removed. Manual keybox imports
have no provider allowlist and gain JCA/SEC1/BOM/Base64 compatibility and full error
details. Fetch still requires a usable certificate chain and does not guarantee an
integrity verdict. The preceding dashboard-drag and charging-ambient fixes remain.

Validation: 101 host tests plus Java regressions, 77 integration tests, 87 native
configuration/crypto checks and 76 hub checks; Android Java/resources/AIDL and
native/Kotlin adapter checks, including 102 immutable inputs and 221 reversible
operations. Full Android/Soong and Coral hardware/visual acceptance remain required.
See the [source and device checklist](https://github.com/its-hecker/HeckerOS/blob/d760bfce1ca9e6c018cfaf7dcfcb6b38c1915172/docs/dashboard-launcher-integrity-2026-10-26.md).

NetLab router-peer blocking and bandwidth enforcement still need the router/AP
model, firmware and an authorized management backend. Discovery and capability-
gated phone-hotspot pause/restore remain; no disruptive interception backend is added.

## Sync and build

```bash
mkdir -p ~/heckeros-coral-depth
cd ~/heckeros-coral-depth
repo init -u https://github.com/its-hecker/HeckerOS -b feat/settings-depth-lockscreen-20261028 --git-lfs
git clone --branch feat/settings-depth-lockscreen-20261028 https://github.com/its-hecker/HeckerOs-localmanifest .repo/local_manifests
repo sync -c -j8 --fail-fast --no-clone-bundle --no-tags
HECKER_DEV_USB_ADB=false bash .repo/local_manifests/build.sh
```

Run these commands in a fresh Android source directory with the normal AOSP build prerequisites, Git LFS, Python 3.12+, Java 21+, Pillow and numpy. The script prepares original APKs, theme assets and guarded source adapters, then builds `hecker_coral-hecker_suite-userdebug` with `m heckeros`. It does not sign or publish a release.

## Historical Suite Polish upgrade instructions

The following instructions describe the stable feature track, not the root privacy test. For this test, use the fresh source directory and matching test branches in the recipe above; do not mix the two sets of pins.

The current pins include dashboard/popup/glow/launcher fixes in Suite and
matching **Settings and frameworks/base** PIF/keybox changes.
Let a running build finish first. Remove the old Suite's guarded source adapters
before syncing the new framework; the build helper then reapplies the new adapters.
This preserves build outputs and stops if an unfamiliar source edit needs review.

```bash
cd ~/heckeros-coral
python3 vendor/hecker/floral/suite/tools/prepare.py --rom-root "$PWD" --revert
git -C .repo/local_manifests pull --ff-only origin feat/suite-polish
python3 .repo/local_manifests/tools/retire_launcher.py
python3 .repo/local_manifests/tools/retire_omnijaws.py
repo sync -c -j2 --fail-fast --no-clone-bundle --no-tags vendor/hecker/floral/suite packages/apps/Settings frameworks/base
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

The retirement helper preserves its files under `out/retired-projects/` and is
safe to rerun. The build helper clears staged app files with `installclean` only
when necessary, keeping compiled intermediates. On ServerHive, use the initialized Byobu
build session and retain the provider's RBE environment.
For an older checkout that still has the retired custom Launcher3 repository,
run the retirement helper before replacing that project's Repo metadata. Do not
force a checkout over local edits. Stock AOSP Launcher3 sources supply Hecker
Launcher and the build libraries used by SystemUI.

Source/host checks pass. A complete Settings APK/Soong build, ROM boot and coral hardware tests remain required. This is a source integration checkpoint, not a tested flashable release.

Maintainer: Hecker

[HeckerOS sources](https://github.com/its-hecker/HeckerOS) · [Channel](https://t.me/pixel4seriesupdates) · [Support](https://t.me/Pixel4Roms)

The current pins select the native Hecker 25-cell pose-grid renderer and the Axion-derived
PIF, game profile, keybox import and TrickyStore integration in native Settings.
Photos retains PixelOS's existing implementation. Open Settings > Hecker's Suite >
Spoofing hub to configure profiles, targets and your keybox; restart affected
apps after changing them. No keybox is bundled. Actual enrollment and attestation
verdict testing remain required. Four platform projects use owned HeckerOS forks;
the other 87 stay at their existing upstream repositories with exact source pins.
Bulk repository migration is optional and does not block this build.

The hub adapts the latest verified Evolution X Android 17 `cnb` screens with
TrickyStore/PIF masters, Canary fingerprint fetch, certificate checks, target
search and Auto/Leaf/Cert/Skip modes, plus an original Lottie animation.
Automatic refresh is opt-in and preserves manual imports. Private key material
stays in system-only atomic storage. Certificate status is not an attestation
verdict. [Source pins, adaptation and validation](https://github.com/its-hecker/HeckerOS/blob/feat/suite-polish/docs/spoofing-hub.md).

The dated development checkpoints below describe earlier changes; the upgrade
commands above select the current build.


Development builds also enable USB debugging and accept every connected PC
without an authorization prompt. For the final image, use
`HECKER_DEV_USB_ADB=false HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh`
to restore PC authorization, then flash the rebuilt ROM. The output verifier
checks that this flag reached the installed product properties. An existing
saved USB-debugging choice can survive a dirty flash; enable it in Settings if
needed for the test build.

The same update selects the enrollment grid on both Pixel 4 preview paths, themes
Compose Wi-Fi and cellular icons, fades the compact QS tray during expansion, and
centers the face-unlock feedback icon and label. These changes need a new ROM build and
phone validation; syncing source does not update the running phone.

Bundled lock-screen clock providers are explicitly trusted by SystemUI's
production plugin policy. Dark boots fall back to the normal branded product
animation, whose installed size and hash are checked after building. Brightness
vector icons load as drawables instead of going through ImageDecoder.

## Game Booster reference dashboard

`feat/suite-polish` pins the Game Booster-style Suite and its matching
Floral kernel charging inhibitor. See the [implementation and build notes](https://github.com/its-hecker/HeckerOS/blob/feat/game-booster-reference/docs/game-booster.md).
Both `vendor/hecker/floral/suite` and `kernel/google/msm-4.14` must be synced before
running `build.sh`. These changes require a new ROM build and phone validation.

## Suite polish

Includes the Game Booster reference work and its matching kernel revision. Suite
uses measured inset-safe toolbars, animated layout cards, an energy-orbit charging
effect, native App Lock prompt artwork, unified QS sliders and faster header
collapse. Duplicate Suite routes, unsupported signal/system icon packs, Moto and
Nothing charging resources, and the custom launcher are retired. Wi-Fi/battery
styles live under Status bar. Protected-window capture is opt-in under Screenshots.
The updated retirement helper preserves known custom-launcher checkouts and local
edits; the build helper checks for staged retired apps before invoking installclean.

Source PR: https://github.com/its-hecker/HeckerOS/pull/3
Settings PR: https://github.com/its-hecker/heckeros_packages_apps_Settings/pull/1

Suite source pin: `75d1cb36338610a7adefb6cefd1a2af21fb3dceb`.
Preparation composes the App Lock permission and theme broadcast edits before
writing the framework manifest, so a fresh checkout verifies after one apply.
PIN entry also falls back to the normal explicit confirm button when length
metadata is unavailable after reboot; wrong-PIN and lockout handling remain active.
Full Android/Soong compilation, dirty-upgrade Pixel HOME/Recents, visual comparison
and Coral hardware validation remain pending.

Stock AOSP Launcher3 sources remain available for SystemUI flag and TAPL build libraries. The Launcher3 APKs and Hecker Launcher remain unselected; Pixel Launcher supplies HOME and Recents.

Motion Sense retains the original Oslo glow on lockscreen/AOD and hosts it in a
trusted non-touchable window on HOME/apps while feedback is requested. The Face ID
and Unlocked pill centers its icon and measured label. The Bluetooth connection
card animates an opening case and rising earbuds. The source-built LibrePods
variant routes connected R50i/non-Apple headphones to their own page, with real
Android battery metadata and bounded R50i left/right status and firmware reads.
AirPods retain upstream controls. R50i case battery is unknown unless Android
reports it. Physical case opening is not detected by this connection animation.

The first preparation builds LibrePods from its pinned GPL source, downloading a
cached Android SDK/NDK as needed. It requires Java 21+ (the synced AOSP JDK is
selected automatically) and gives Gradle a 4 GiB heap with two workers. Later
preparations verify and reuse the APK's source recipe and content hashes.
See the [companion source/build notes](https://github.com/its-hecker/HeckerOS/blob/feat/suite-polish/prebuilts/librepods/README.md).

The Suite cache now has a tracked `out/.find-ignore` marker. It prevents the
downloaded LibrePods NDK `cpufeatures` makefile from being scanned as an Android
module, preserving the SDK/APK cache and compiled ROM outputs. To recover from
the duplicate `MODULE.TARGET.STATIC_LIBRARIES.cpufeatures` error in an already
initialized ServerHive build session:

```bash
cd ~/heckeros-coral
git -C .repo/local_manifests pull --ff-only
repo sync -c -j2 --fail-fast --no-clone-bundle --no-tags vendor/hecker/floral/suite
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

This pin retains the automatic-brightness toggles for One UI and Hecker Quick
Settings and includes the native interaction features documented below.


## Native interaction features

This Suite pin adds the One UI compact/expanded volume panel with native hearing
safety dialogs, status-bar long-press shortcuts and Memory Boost. Suite has a
searchable per-app background start/task/clean task/resident policy page, with
system apps hidden by default. Pixel Launcher remains the HOME/Recents provider
and gains native empty-home double-tap sleep and frosted/liquid glass controls.
These launcher features are a native subset, not the full PixelLauncherEnhanced
Xposed module. The automatic-brightness toggles and NDK-cache isolation remain.

The current Suite pin fixes the three `getCurProcState()` errors in
`HeckerMemoryPolicy.java` during `services.core.unboosted` compilation by using
Android 17's public `getProcState()` API. Normal build preparation upgrades the
known earlier adapter; sync the Suite and rerun `build.sh` in the existing
initialized ServerHive session. Compiled outputs and the LibrePods cache can be reused.

It also registers all three new Java Binder services in Android's fuzzer-binding
map and upgrades the status popup hook into the existing touch-dispatch method,
fixing `fuzzer_bindings_test` and SystemUI's duplicate-method overload error.
Pinned-source checks exercise Android's own binding checker and compile the
prepared Java dispatch method with a Kotlin caller. Normal preparation repairs
the known earlier hook without a clean checkout or output wipe.

Source and integration checks pass; full Android/Soong compilation and Coral
hardware tests remain required. See the [feature notes](https://github.com/its-hecker/HeckerOS/blob/feat/suite-polish/docs/interaction-features.md).

## Gaming service label and terminal boot update

The Suite pin keeps `hecker_game` exclusively under the dedicated
`hecker_game_service` system_ext label. The platform adapter registers
`hecker_memory` and `hecker_launcher` and upgrades both the previous conflicting
block and one already repaired manually. Its native integration check combines
platform and Suite declarations, rejects duplicate gaming labels, and retains
all three Java service fuzzer registrations.

The same pin includes Hecker's approved terminal boot animation. Preparation
assembles the original ZIP byte for byte from checksum-pinned source chunks,
then checks all 210 PNG frames and the locked payload hash. CI validates the
asset without rendering the superseded animation.

Use the existing incremental update instructions on `feat/suite-polish` after
any running build has finished. Keep this branch for the Pixel Launcher-only
product, PIN guard, Memory Boost and other latest native interaction changes.

## 24 October UI and runtime refinement

The Suite pin includes the glass Hecker QS layout, matching vertical brightness/volume tracks, compact session-backed media with artwork, the Lunaris Dolby shortcut, adaptive OneUI battery colors and size controls, lower lock-screen/AOD lyrics, the caracal lock-screen signature, and corrected Suite/header spacing and back buttons. App Lock refreshes native protection state after its authenticated change flow. QS previews and GameSpace use bundled Lottie artwork.

The unlocked Oslo feedback surface no longer forces the native shade open. Game Booster has a smaller landscape control layout, real custom-mode FPS/render-scale fallback for games without native profiles, and more specific charging-pause diagnostics. The independent Coral kernel charge inhibitor and its fail-safe lease are retained.

Let any running build finish before syncing. In an already updated checkout, use:

```bash
cd ~/heckeros-coral
git -C .repo/local_manifests pull --ff-only origin feat/suite-polish
repo sync -c -j2 --fail-fast --no-clone-bundle --no-tags vendor/hecker/floral/suite
HECKER_BUILD_JOBS=8 bash .repo/local_manifests/build.sh
```

This pin changes the Suite adapters; the current framework, Settings and kernel source pins are retained. Existing source adaptations upgrade through the build helper. The 79 host tests, 77 integration tests, SDK/Compose compilation and 71 pinned native source roundtrips pass. A full ROM build and on-device visual, Soli, AOD and wired-charging checks remain required. Charging pause is not a guarantee of electrical battery isolation.

[Implementation and verification notes](https://github.com/its-hecker/HeckerOS/blob/8c08d3486ac7c86366075cbf6ea42eeff0b35282/docs/ui-refinement-2026-10-24.md)

## Pakistan IMS test configuration

This manifest pins the shared Suite with VoLTE/Wi-Fi Calling defaults and
dedicated IMS APNs for Jazz/Warid, Ufone, Zong and Telenor. Independent icon
switches are under Hecker Suite > Status bar > Calling indicators; icons follow
actual IMS voice registration and availability for each SIM.

Source, SDK and host checks pass. Working calls and a compatible Pakistan modem
profile remain unverified; rebuild and test the individual SIMs before marking
a carrier as supported. See the [IMS implementation and device checks](https://github.com/its-hecker/HeckerOS/blob/a51eacc198efe0a79a1f5e5e455c422064206e95/ims/README.md).

### Music Motion Island and astronaut on the Coral experiment

Only `test/coral-root-privacy-20261027` selects this experiment. Open
**Motion Island & creature** from **Hecker Suite → Motion Sense** or **Status bar**.
During music playback the compact capsule shows album art and thin blue vertical
bars. Tap it to open the same media card used on the lockscreen. Its expanded
controls stay pinned to the tapped session, including while paused.

The reference astronaut hangs from the capsule by a rope, swings in the physical
flick direction and waves for play/pause. It fades after gesture inactivity;
a pause lets the brief goodbye finish before the capsule hides. The separate
character toggle requires Motion Island. Screen off/AOD hides both; battery
saver and reduced motion keep static visuals. Ambiguous non-music sessions are
filtered conservatively. The selected Suite's `docs/motion-island.md` records
behavior, artwork provenance, host preview and acceptance checks.

The manifest pins matching immutable Suite and Motion Sense plugin revisions;
the plugin pins the rebuilt Oslo APK by commit, size, Git blob and SHA-256. The
ROM build aligns and signs that input with its platform key. Host/SDK/Compose,
controller, manifest and guarded-adapter checks pass; a full ROM build and Coral
device validation are still required.
