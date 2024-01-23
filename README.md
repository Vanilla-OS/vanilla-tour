<div align="center">
    <img src="data/icons/hicolor/scalable/apps/org.vanillaos.Tour.svg" height="64">
    <h1>Vanilla OS Tour</h1>
    <p>A quick slideview Tour of all new things in Vanilla OS.</p>
    <hr />
    <br />
    <img src="data/screenshot.png">
</div>

## Build

### Dependencies

- build-essential
- meson
- libadwaita-1-dev
- gettext
- desktop-file-utils
- blueprint-compiler

```bash
meson build
ninja -C build
```

### Install

```bash
sudo ninja -C build install
```

## Run

```bash
vanilla-tour
```
