# Home Assistant SimpliSafe Fix

Temporary HACS-installable dependency override for Home Assistant Core 2026.8.3.

This custom component is a thin wrapper around Home Assistant's built-in `simplisafe` integration. It delegates runtime code back to the stock Home Assistant integration while changing the Python dependency from `simplisafe-python==2024.01.0` to `simplisafe-python==2026.06.0`.

The newer library contains the upstream fix for SimpliSafe camera WebSocket events that omit `_links["playback/hls"]`, which otherwise causes Home Assistant to log:

```
Unexpected error in websocket loop: 'playback/hls'
KeyError: 'playback/hls'
```

Home Assistant's development branch changed the official SimpliSafe dependency to `simplisafe-python==2026.06.0` on 2026-08-27. This repository is intended as a temporary backport until an official Home Assistant release containing that change is installed.

## Installation with HACS

1. Add this repository to HACS as a custom repository of type **Integration**.
2. Install **SimpliSafe Fix**.
3. Restart Home Assistant.
4. Verify the startup log shows the custom SimpliSafe integration warning and that the `playback/hls` traceback no longer occurs.

Your existing SimpliSafe config entry is reused; do not delete or recreate it.

## Removal

After Home Assistant ships the official dependency update:

1. Remove **SimpliSafe Fix** in HACS.
2. Restart Home Assistant.

Home Assistant will return to its built-in `simplisafe` integration.
