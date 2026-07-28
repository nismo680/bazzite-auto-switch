````markdown
# SessionFlipper

> Automatic Desktop ↔ Console session switching for Linux systems using
> `steamos-session-select`.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Linux](https://img.shields.io/badge/Linux-systemd-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

SessionFlipper automatically switches between **Desktop** and **Console**
sessions based on your connected displays.

Instead of polling, SessionFlipper listens for **Linux DRM hotplug events** and
uses the official `steamos-session-select` command to switch sessions.

Whether you dock your handheld, connect an external monitor or move from your
desk to your TV, SessionFlipper automatically selects the appropriate session.

> [!WARNING]
> ## Project Status
>
> SessionFlipper is currently under active development.
>
> The core functionality is already implemented and used daily, but the project
> is not yet feature complete.
>
> **Current progress**
>
> - ✅ DRM hotplug detection
> - ✅ Automatic Desktop ↔ Console session switching
> - ✅ Display profile configuration
> - ✅ Configurable switching delay
> - ✅ systemd user service
> - ✅ Enable / Disable automatic switching
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
- Lightweight
- Minimal dependencies
- No root or sudo required

---

# How it works

Whenever a display is connected or disconnected, Linux generates a DRM hotplug
event.

SessionFlipper waits for the configured settle delay, determines which display
profile matches the current hardware configuration and automatically switches to
the appropriate session.

Typical examples:

| Display configuration | Selected session |
|----------------------|------------------|
| Internal display only | Console |
| Dock connected | Desktop |
| External monitor connected | Desktop |
| TV connected | Console *(if configured)* |

---

# Compatibility

## Officially tested

| Distribution | Status |
|--------------|--------|
| Bazzite | ✅ Tested |

## Community testing wanted

SessionFlipper is designed for Linux distributions providing
`steamos-session-select`.

This is expected to include systems such as:

- SteamOS
- ChimeraOS
- other compatible distributions

If you successfully test SessionFlipper on another distribution, please open an
issue or submit a pull request.

Community feedback is highly appreciated.

---

# Requirements

- Linux
- Python 3.12 or newer
- systemd
- `steamos-session-select`

---

# Installation

There are currently no binary releases.

Clone the repository:

```bash
git clone https://github.com/<username>/sessionflipper.git
cd sessionflipper
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install SessionFlipper:

```bash
pip install -e ".[dev]"
```

---

# Configuration

Configure your display profiles:

```bash
sessionflipper displays
```

Configure general settings:

```bash
sessionflipper settings
```

Display the current configuration:

```bash
sessionflipper config
```

---

# Commands

| Command | Description |
|----------|-------------|
| `sessionflipper list` | List detected GPUs and displays |
| `sessionflipper displays` | Configure display profiles |
| `sessionflipper settings` | Configure general settings |
| `sessionflipper config` | Show current configuration |
| `sessionflipper status` | Show current status |
| `sessionflipper enable` | Enable automatic switching |
| `sessionflipper disable` | Disable automatic switching |
| `sessionflipper install` | Install the systemd user service |
| `sessionflipper uninstall` | Remove the systemd user service |
| `sessionflipper daemon` | Start the daemon for debugging or trial use before installing|

---

# Why SessionFlipper?

Unlike polling-based solutions, SessionFlipper

- reacts immediately to display changes
- consumes virtually no CPU while idle
- integrates cleanly with systemd
- relies on the official `steamos-session-select`
- is lightweight and easy to configure

---

# Roadmap

## Near term

- KDE system tray application
- SessionFlipper application icon
- Binary releases
- Complete documentation

---

# Contributing

Contributions are always welcome.

Please feel free to:

- report bugs
- suggest new features
- improve the documentation
- submit pull requests
- test SessionFlipper on additional distributions

---

# License

Released under the MIT License.

See the `LICENSE` file for details.
````
