# Mobile applications

## Separate access layers

Identify app/package ID, version/build, OS, device/emulator, and available role.
The user may provide only a store listing, screenshots, an APK/IPA, source, or
an installed app. Record each layer and its limits. A mobile client does not
contain the hosted backend simply because it contains endpoint names.

- Public/store evidence: current listing, screenshots, release notes, support,
  privacy disclosures and subscription/feature descriptions. These are documented
  claims or recorded UI, not a complete observation of the live app.
- Android package: archive members, manifest, resources, permissions, activities,
  services, intents/deep links, bytecode and native libraries. Use compatible
  package/bytecode tools; route native modules to the desktop/artifact guide.
- iOS package: bundle metadata, entitlements, resources, frameworks and native
  binary metadata where available. Encryption, signing and tooling constraints
  can limit analysis; package possession is not proof that code is inspectable.
- Source: identify native/cross-platform boundaries, plugins and build settings
  from actual project files; use the code guide for the relevant path.
- Runtime: inspect the selected device/emulator/app using available automation
  and authorized accounts/test data. Record OS/version and configuration.

Installing/removing packages, altering permissions, changing a personal device,
or using a real account must stay within the user's existing authorization.
Prefer a test device/emulator when dynamic investigation needs changes. Missing
access to a device does not block useful package or document analysis.

## Trace mobile behavior

Map onboarding, navigation and the requested workflows. Include applicable
mobile-specific states: permission granted/denied, background/foreground,
offline/reconnect, interrupted actions, notification/deep-link entry, orientation,
accessibility, account changes and local/server sync conflicts. Inspect purchases
as documented/test flows without initiating a real charge unless requested.

Relate UI actions to storage, system services, bridge/native code and network
contracts using available evidence. Inspect authorized traffic/captures without
turning a historical request into a live replay. A permission declaration does
not prove runtime use; a class or endpoint can be inactive or gated. Record
coverage by platform, version, role and state.

## Outcome-specific requirements

- Stack/mechanism: platform/framework clues, local computation, native integrations,
  and the explicit boundary of unknown server behavior.
- Catalog: screens plus transitions, system integrations, role/plan differences,
  sync/background behavior and inaccessible areas.
- Recreation/private label: original branding, feature and data ownership scope,
  package identity, signing/distribution method, backend availability, offline
  guarantees, migrations and update path. Internal use still needs a viable
  deployment and authentication story.
- Improvement: observed usability/performance failures on a named device/state,
  implementation seam and regression checks across affected platforms.

If the request requires unsupported inspection, explain the exact artifact or
capability that would unlock it and proceed with what is supported. Do not turn
store screenshots into a claimed complete feature inventory or invent decrypted
code, private APIs, device access or tests.
