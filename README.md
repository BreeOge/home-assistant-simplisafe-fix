# Home Assistant SimpliSafe Fix

Temporary HACS-installable backport for Home Assistant Core 2026.8.3.

This repository mirrors Home Assistant's built-in `simplisafe` integration from Core 2026.8.3 and changes the `simplisafe-python` requirement from `2024.01.0` to `2026.06.0` to include the upstream fix for camera WebSocket events that omit `_links["playback/hls"]`.

## Why this exists

Home Assistant Core 2026.8.3 can log:

```
Unexpected error in websocket loop: 'playback/hls'
KeyError: 'playback/hls'
```

Home Assistant's development branch updated the SimpliSafe dependency to `simplisafe-python==2026.06.0` on 2026-08-27. This repository is intended only as a temporary backport until an official Home Assistant release containing that dependency update is installed.

## Important

This custom component overrides Home Assistant's built-in `simplisafe` integration while installed. Remove it after upgrading to an official Home Assistant release that includes the newer dependency.
