````markdown
# SessionFlipper

<p align="center">
  <b>Automatic Desktop ↔ Console session switching for Linux systems using <code>steamos-session-select</code>.</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Linux](https://img.shields.io/badge/Linux-systemd-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

</p>

---

SessionFlipper automatically switches between **Desktop** and **Console**
sessions based on your connected displays.

It monitors **DRM hotplug events** instead of polling and uses the official
`steamos-session-select` command to perform the session switch.

Whether you dock your handheld, connect external monitors or move between your
desk and your TV, SessionFlipper automatically selects the appropriate session.

---

> [!WARNING]
> ## Project Status
>
> **SessionFlipper is under active development.**
>
> The core functionality is already working and used daily, but the project is
> not yet feature complete.
>
> ### Current status
>
> - ✅ DRM hotplug detection
> - ✅ Automatic Desktop ↔ Console switching
> - ✅ Display profile configuration
> - ✅ Configurable switching delay
> - ✅ systemd user service
> - ✅ Manual enable/disable
> - 🚧 KDE system tray application
> - 🚧 Documentation
> - 🚧 First public release
>
> There are currently **no binary releases or distribution packages**.
>
> Installation currently requires cloning the repository and running
> SessionFlipper from source.
>
> Feedback, bug reports and pull requests are always welcome.

---

# Features

- Automatic Desktop ↔ Console session switching
- DRM hotplug event detection
- No polling
- Uses the official `steamos-session-select`
- Configurable display profiles
- Configurable display settle delay
- Runs as a systemd user service
- KDE system tray integration *(planned)*
- Lightweight with minimal dependencies

---

# How it works

Whenever a display is connected or disconnected, the Linux DRM subsystem emits
a hotplug event.

SessionFlipper receives this event, waits for the configured settle delay,
determines the matching display profile and automatically switches to the
appropriate session.

Typical examples:

| Displays | Session |
|----------|---------|
| Internal display only | Console |
| Dock connected | Desktop |
| External monitor | Desktop |
| TV connected | Console *(if configured)* |

---

# Compatibility

## Officially tested

- ✅ Bazzite

## Community testing wanted

SessionFlipper is designed for Linux distributions providing
`steamos-session-select`.

This should include systems such as:

- SteamOS
- ChimeraOS
- other compatible distributions

Community testing is highly appreciated.

If you've successfully tested SessionFlipper on another distribution, please
open an issue or pull request so it can be added here.

---

# Requirements

- Linux
- Python 3.12+
- systemd
- `steamos-session-select`

---

# Installation

At the moment there are no binary releases.

Clone the repository and run SessionFlipper from source.

```bash
git clone https://github.com/<yourname>/sessionflipper.git
cd sessionflipper
```

---

# Commands

```text
sessionflipper list
sessionflipper setup displays
sessionflipper setup settings
sessionflipper show config
sessionflipper status
sessionflipper enable
sessionflipper disable
sessionflipper install
sessionflipper uninstall
```

---

# Why SessionFlipper?

Unlike simple polling solutions, SessionFlipper

- reacts instantly to display changes
- consumes virtually no CPU while idle
- integrates cleanly with systemd
- relies on the official SteamOS session switching mechanism
- is designed to be lightweight and reliable

---

# Roadmap

## Near term

- KDE system tray application
- Application icon
- Improved installer
- Binary releases
- More documentation

## Future ideas

- Additional profile options
- Import/export configuration
- GUI configuration utility
- Automatic updates
- More community-tested distributions

---

# Contributing

Contributions are welcome.

If you have ideas, discover bugs or successfully test SessionFlipper on another
distribution, please open an issue or submit a pull request.

---

# License

MIT License
````
