Summary:        GStreamer 1.0 streaming media framework "ugly" plug-ins
Name:           gstreamer1-plugins-ugly
Version:        0.11.93
Release:        2%{?dist}
License:        LGPLv2+
Group:          Applications/Multimedia
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gettext-devel gtk-doc
%if 0%{?fedora} <= 17
BuildRequires:  libsidplay-devel >= 1.36.0
%endif
BuildRequires:  a52dec-devel >= 0.7.3
BuildRequires:  libdvdread-devel >= 0.9.0
BuildRequires:  lame-devel >= 3.89
BuildRequires:  libid3tag-devel >= 0.15.0
BuildRequires:  libmad-devel >= 0.15.0
BuildRequires:  mpeg2dec-devel >= 0.4.0
BuildRequires:  orc-devel >= 0.4.5
BuildRequires:  libcdio-devel >= 0.82
BuildRequires:  twolame-devel
BuildRequires:  x264-devel >= 0.0.0-0.28
BuildRequires:  opencore-amr-devel
BuildRequires:  PyXML

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains well-written plug-ins that can't be shipped in
gstreamer-plugins-good because:
- the license is not LGPL
- the license of the library is not LGPL
- there are possible licensing issues with the code.


%package devel-docs
Summary: Development documentation for the GStreamer "ugly" plug-ins
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description devel-docs
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development documentation for the plug-ins that can't
be shipped in gstreamer-plugins-good because:
- the license is not LGPL
- the license of the library is not LGPL
- there are possible licensing issues with the code.


%prep
%setup -q -n gst-plugins-ugly-%{version}


%build
%configure \
    --with-package-name="gst-plugins-ugly 1.0 rpmfusion rpm" \
    --with-package-origin="http://rpmfusion.org/" \
    --enable-debug --enable-gtk-doc \
    --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang gst-plugins-ugly-1.0
rm $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/*.la


%files -f gst-plugins-ugly-1.0.lang
%doc AUTHORS COPYING README REQUIREMENTS
%{_datadir}/gstreamer-1.0
# Plugins without external dependencies
%{_libdir}/gstreamer-1.0/libgstasf.so
%{_libdir}/gstreamer-1.0/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-1.0/libgstdvdsub.so
%{_libdir}/gstreamer-1.0/libgstrmdemux.so
%{_libdir}/gstreamer-1.0/libgstxingmux.so
# Plugins with external dependencies
%{_libdir}/gstreamer-1.0/libgsta52dec.so
%{_libdir}/gstreamer-1.0/libgstamrnb.so
%{_libdir}/gstreamer-1.0/libgstamrwbdec.so
%{_libdir}/gstreamer-1.0/libgstcdio.so
%{_libdir}/gstreamer-1.0/libgstdvdread.so
%{_libdir}/gstreamer-1.0/libgstlame.so
%{_libdir}/gstreamer-1.0/libgstmad.so
%{_libdir}/gstreamer-1.0/libgstmpeg2dec.so
%if 0%{?fedora} <= 17
%{_libdir}/gstreamer-1.0/libgstsid.so
%endif
%{_libdir}/gstreamer-1.0/libgsttwolame.so
%{_libdir}/gstreamer-1.0/libgstx264.so

%files devel-docs
# Take the dir and everything below it for proper dir ownership
%doc %{_datadir}/gtk-doc


%changelog
* Sun Sep 16 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.93-2
- Fix gtk-doc dir ownership (rf#2474)

* Sun Sep  9 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.93-1
- First version of gstreamer1-plugins-ugly for rpmfusion
