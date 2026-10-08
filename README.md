# oodf: Sovereign Disk Space & Mount Point Storage Inspector

<div align="center">

```
================================================================================
                                oodf v0.2.0
               Sovereign openOODA Free Disk Space Inspector
================================================================================
```

**Sovereign Disk Space & Mount Point Storage Inspector**  
*Mount point storage inspector displaying total, used, and available blocks and inodes.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage streaming MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64](https://img.shields.io/badge/Arch-x86__64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64)
```bash
curl -fsSL https://openooda-tools.github.io/oodf/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oodf-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oodf/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oodf/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oodf-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oodf/uninstall.sh | bash
```

---

## 2. CLI Usage & Options

```
Usage: oodf [OPTION]... [FILE]...
Show information about the file system on which each FILE resides,
or all file systems by default.

Options:
  -a, --all             include pseudo, duplicate, and inaccessible file systems
  -h, --human-readable  print sizes in powers of 1024 (e.g., 1023M, 14G)
  -H, --si              print sizes in powers of 1000
  -i, --inodes          list inode information instead of block usage
  -k                    like --block-size=1K
  -m                    like --block-size=1M
  -t, --type=TYPE       limit listing to file systems of type TYPE
  -x, --exclude-type=T  limit listing to file systems not of type T
      --total           produce a grand total summary row
  -j, --json            output raw structured telemetry in JSON format
  -D, --demo            run synthetic multi-mount storage showcase
      --theme=NAME      terminal ANSI palette (ember, ocean, matrix, cyber, monochrome)
      --mcp             launch streaming MCP JSON-RPC 2.0 stdio server
      --help            display this help and exit
  -v, --version         output version information and exit
```

### Examples
```bash
# Human-readable live inspection with grand total
oodf -h --total

# Inode consumption across ext4 and btrfs mounts
oodf -i -t btrfs

# Exclude virtual memory filesystems
oodf -h -x tmpfs

# JSON output for automated scripting
oodf -j

# Synthetic storage cluster showcase
oodf -D --theme=ocean
```

---

## 3. Model Context Protocol (MCP)

When launched with `--mcp`, `oodf` runs a streaming JSON-RPC 2.0 stdio server compliant with the standard Model Context Protocol.

```bash
oodf --mcp
```

### Registered Tools

| Tool | Parameters | Description |
| :--- | :--- | :--- |
| `df_inspect` | `path`, `all`, `human_readable`, `inodes`, `total`, `type`, `exclude_type`, `json`, `theme` | Inspect filesystem capacity, block usage, and mount hierarchy. |
| `df_mounts` | *(none)* | Return raw JSON array of all active filesystem mounts. |
| `df_inodes` | `path`, `all` | Inspect inode consumption and free inode capacity. |
| `df_path` | `path` (required) | Inspect disk capacity specifically for a target path or block device. |
| `df_demo` | *(none)* | Return synthetic multi-filesystem storage showcase document. |

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit capability tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient disk write access or socket network leakage.
* **Negative-Trust Architecture:** Strict parameter bounding and path sanitization.
* **Hermetic Binary:** Standalone zero-dependency executable compiled via `oodac`.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
