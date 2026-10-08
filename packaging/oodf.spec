Name:           oodf
Version:        0.2.0
Release:        1%{?dist}
Summary:        Filesystem free space and mount point storage auditor in pure openOODA.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oodf
Source0:        oodf-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oodf is a sovereign, capability-bounded filesystem free space and
storage capacity inspector written in pure openOODA, featuring zero
ambient authority, oote terminal themes, and a streaming Model
Context Protocol (MCP) JSON-RPC 2.0 stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oodf
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oodf-uninstall

%files
/usr/bin/oodf
/usr/bin/oodf-uninstall

%changelog
* Wed Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate oodf to v0.2.0 sovereign storage inspector with streaming MCP
