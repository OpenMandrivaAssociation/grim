Name:           grim
Version:        1.5.0
Release:        1
Summary:        Wayland compositor image grabber
License:        MIT
URL:            https://github.com/emersion/grim
Source0:        https://gitlab.freedesktop.org/emersion/grim/-/archive/v%{version}/grim-v%{version}.tar.bz2
#Source0:        https://git.sr.ht/~emersion/grim/archive/v%{version}/%{name}-v%{version}.tar.gz
#Source0:        https://github.com/emersion/grim/archive/v%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14

%description
This tool can grab images from a Wayland compositor.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man?/%{name}*
