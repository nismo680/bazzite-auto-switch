# SessionFlipper

> Automatic Desktop ↔ Console session switching for Linux systems using `steamos-session-select`.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-systemd-FCC624?logo=linux&logoColor=black)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Automatically switches between **Desktop** and **Console** whenever your display
configuration changes.

No polling. No timers. No root privileges.

---

## Why?

If you regularly connect and disconnect

- a docking station
- an external monitor
- a TV

you probably switch manually between

- 🎮 Console Mode
- 🖥 Desktop Mode

SessionFlipper does this automatically.

---

## Features

- ⚡ DRM hotplug event detection
- 🚫 No polling
- 🎮 Uses the official `steamos-session-select`
- 🖥 Automatic Desktop ↔ Console switching
- ⚙ Configurable display profiles
- ⏱ Configurable settle delay
- 🔧 systemd user service
- 🔒 No root or sudo required
- 🐬 KDE tray application *(coming soon)*

---

## Example

| Displays | Session |
|----------|---------|
| Steam Deck only | 🎮 Console |
| Dock connected | 🖥 Desktop |
| External monitor | 🖥 Desktop |
| TV | 🎮 Console *(if configured)* |

---

## Project Status

> [!WARNING]
> SessionFlipper is under active development.

### Already implemented

- ✅ DRM hotplug monitoring
- ✅ Automatic session switching
- ✅ Display profile configuration
- ✅ Configurable switching delay
- ✅ systemd user service
- ✅ Enable / Disable switching

### In progress

- 🚧 KDE tray application
- 🚧 Documentation
- 🚧 First public release
- 🚧 Binary packages

There are currently **no binary releases**.

Feedback and testing are highly appreciated.

---

## Compatibility

### Tested

| Distribution | Status |
|--------------|--------|
| Bazzite | ✅ |

### Community testing welcome

SessionFlipper is designed for systems providing
`steamos-session-select`.

This is expected to include:

- SteamOS
- ChimeraOS
- other compatible distributions

If you've tested SessionFlipper successfully, please let me know.

---

## Installation

```bash
git clone https://github.com/nismo680/sessionflipper.git

cd sessionflipper

python -m venv .venv

source .venv/bin/activate

pip install -e ".[dev]"
```

---

## Quick Start

Configure your display profiles.

```bash
sessionflipper displays
```

Configure general settings.

```bash
sessionflipper settings
```

Install the daemon.

```bash
sessionflipper install
```

That's it.

---

## Commands

| Command | Description |
|---------|-------------|
| `sessionflipper list` | List detected displays |
| `sessionflipper displays` | Configure display profiles |
| `sessionflipper settings` | Configure settings |
| `sessionflipper config` | Show configuration |
| `sessionflipper status` | Show current status |
| `sessionflipper enable` | Enable automatic switching |
| `sessionflipper disable` | Disable automatic switching |
| `sessionflipper install` | Install the user service |
| `sessionflipper uninstall` | Remove the user service |
| `sessionflipper daemon` | Run in foreground |

---

## How it works

Linux generates a DRM hotplug event whenever a display is connected or
disconnected.

SessionFlipper receives this event, waits for the configured settle delay,
matches the current display profile and switches to the appropriate session
using `steamos-session-select`.

---

## Roadmap

- KDE tray application
- Dolphin application icon 🐬
- Binary releases
- Complete documentation
- Additional profile options

---

## Contributing

Contributions are welcome.

Especially appreciated are

- bug reports
- pull requests
- documentation improvements
- testing on additional distributions

---

## License

Released under the MIT License.

See [LICENSE](LICENSE).
