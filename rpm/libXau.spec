Name: libXau
Summary: Sample Authorization Protocol for X
Version: 1.0.10+git1
Release: 1
License: MIT
URL: https://xcb.freedesktop.org/
Source0: %{name}-%{version}.tar.zst
BuildRequires: libtool
BuildRequires: pkgconfig(xorg-macros) >= 1.18
BuildRequires: pkgconfig(xproto)

%description
This is a very simple mechanism for providing individual access to an X Window
System display. It uses existing core protocol and library hooks for specifying
authorization data in the connection setup block to restrict use of the display
to only those clients that show that they know a server-specific key called a
"magic cookie".

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig(xproto)

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%reconfigure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_mandir}

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.so
%{_libdir}/pkgconfig/xau.pc
