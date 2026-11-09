#
# spec file for package gulkan
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define _libver 0.16

Name:           gulkan
Version:        0.16.0
Release:        0
Summary:        A GLib library for Vulkan abstraction
License:        MIT
Url:            https://gitlab.freedesktop.org/xrdesktop/gulkan
Source:         %{name}-%{version}.tar.bz2
Patch0:         0001_use_gdk_4_0_gir.patch
BuildRequires:  meson
BuildRequires:  libstdc++-devel
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(graphene-1.0)


BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(libdrm_amdgpu)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)

BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(json-glib-1.0)

BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)

%description
A GLib library for Vulkan abstraction

%package -n typelib-1_0-Gulkan-0_16
Summary:        Introspection bindings for the Gulkan library
Group:          System/Libraries

%description -n typelib-1_0-Gulkan-0_16
This package provides the GObject Introspection bindings for Gulkan.

%package devel
Summary:        A GLib library for Vulkan abstraction
Requires:       %{name} = %{version}
Requires:       typelib-1_0-Gulkan-0_16 = %{version}

%description devel
A GLib library for Vulkan abstraction

%prep
%setup -q
%patch -P0 -p1

%build
export SUSE_ASNEEDED=0
%meson -Dintrospection=true
%meson_build

%install
export SUSE_ASNEEDED=0
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%{_bindir}/%{name}-cube
%{_bindir}/%{name}-toy
%{_libdir}/lib%{name}-%{_libver}.so.*

%files devel
%dir %{_includedir}/%{name}-%{_libver}
%{_includedir}/%{name}-%{_libver}/*.h
%{_libdir}/pkgconfig/%{name}-%{_libver}.pc
%{_libdir}/lib%{name}-%{_libver}.so
%{_datadir}/gir-1.0/*.gir

%files -n typelib-1_0-Gulkan-0_16
%{_libdir}/girepository-1.0/Gulkan-0.16.typelib

%changelog
