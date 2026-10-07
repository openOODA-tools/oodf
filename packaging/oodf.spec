Name:           oodf
Version:        0.1.0
Release:        1%{?dist}
Summary:        Mount point storage inspector displaying total, used, and available blocks and inodes.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oodf
Source0:        oodf-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oodf is a sovereign, capability-bounded FREE SPACE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oodf
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oodf-uninstall

%files
/usr/bin/oodf
/usr/bin/oodf-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
