# Architecture

SessionFlipper is completely event driven.

No polling is used.

```
DRM hotplug event
        │
        ▼
display_settle_time
        │
        ▼
Read current display configuration
        │
        ▼
Match configured display profiles
        │
        ▼
Select preferred session
        │
        ▼
Switch session
        │
        ▼
debounce_time
        │
        ▼
Discard queued DRM events
        │
        ▼
Wait for next hotplug event
```

## Components

### daemon

Waits for DRM hotplug events.

### events

Receives udev DRM events.

### drm

Reads the current DRM connector state.

### decision

Determines whether Desktop or Console should be active.

### session

Checks the current session and performs session switches using
`steamos-session-select`.

### config

Loads and stores the user configuration.
