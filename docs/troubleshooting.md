# Troubleshooting

## No automatic switching

Check whether automatic switching is enabled:

```bash
sessionflipper status
```

---

## Daemon not running

Start the daemon:

```bash
sessionflipper daemon
```

or enable the systemd user service.

---

## Wrong session selected

Verify:

- configured display profiles
- session priority
- current display configuration

Use:

```bash
sessionflipper list
```

and

```bash
sessionflipper config
```

---

## Displays are detected too early

Increase

```
display_settle_time
```

slightly.

---

## Repeated switching after a session change

Increase

```
debounce_time
```

slightly.
