%global src_name gst-plugins-ugly

Summary:        GStreamer 1.0 streaming media framework "ugly" plug-ins
Name:           gstreamer1-plugins-ugly
Version:        1.14.3
Release:        1%{?dist}
License:        LGPLv2+
Group:          Applications/Multimedia
URL:            https://gstreamer.freedesktop.org/
Source0:        %{url}/src/%{src_name}/%{src_name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gettext-devel
BuildRequires:  libid3tag-devel >= 0.15.0
BuildRequires:  libmpeg2-devel >= 0.4.0
BuildRequires:  orc-devel >= 0.4.5
BuildRequires:  x264-devel >= 0.0.0-0.28
BuildRequires:  opencore-amr-devel

# Provides locale files
# relax dep to >= to make fedora/rpmfusion upgrades easier
Requires:       %{name}-free%{?_isa} >= %{version}

# Subpkg is empty, so no point -- rex
Obsoletes: %{name}-devel-docs < 1.13

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
Requires: %{name} = %{version}-%{release}
Requires: %{name}-free-devel = %{version}
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
%autosetup -p1 -n %{src_name}-%{version}


%build
%configure \
    --disable-silent-rules --disable-fatal-warnings \
    --with-package-name="gst-plugins-ugly 1.0 rpmfusion rpm" \
    --with-package-origin="http://rpmfusion.org/" \
    --disable-static \
    --enable-debug \
    --disable-gtk-doc \
    --disable-mpg123 \
    --disable-cdio \
    --disable-dvdread \
    --disable-a52dec \
    --disable-xingmux \
    --disable-lame \
    --disable-twolame

%make_build V=1


%install
%make_install V=1

rm -fv %{buildroot}%{_libdir}/gstreamer-1.0/*.la
rm -rf %{buildroot}%{_datadir}/locale/
rm -fv %{buildroot}%{_datadir}/gtk-doc/html/%{src_name}-plugins-1.0/*


%files
%doc AUTHORS README REQUIREMENTS
%license COPYING
%{_datadir}/gstreamer-1.0
# Plugins without external dependencies
%{_libdir}/gstreamer-1.0/libgstasf.so
%{_libdir}/gstreamer-1.0/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-1.0/libgstdvdsub.so
%{_libdir}/gstreamer-1.0/libgstrealmedia.so
# Plugins with external dependencies
%{_libdir}/gstreamer-1.0/libgstamrnb.so
%{_libdir}/gstreamer-1.0/libgstamrwbdec.so
%{_libdir}/gstreamer-1.0/libgstmpeg2dec.so
%{_libdir}/gstreamer-1.0/libgstx264.so

#files devel-docs
# Take the dir and everything below it for proper dir ownership
#doc %{_datadir}/gtk-doc/html/%{src_name}-plugins-1.0/


%changelog
* Tue Sep 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.14.3-1
- 1.14.3

* Sat Aug 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.2-1
- 1.14.2

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.1-2
- BR: s/mpeg2dec-devel/libmpeg2-devel/

* Thu May 31 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.1-1
- 1.14.1

* Fri Mar 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.0-1
- 1.14.0

* Wed Feb 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.13.1-1
- 1.13.1

* Wed Jan 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.12.4-3
- remove twolame (rfbz#4766)

* Sat Dec 30 2017 Sérgio Basto <sergio@serjux.com> - 1.12.4-2
- Mass rebuild for x264 and x265

* Mon Dec 11 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.4-1
- Update to 1.12.4

* Thu Sep 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.3-1
- Update to 1.12.3

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.2-1
- Update to 1.12.2

* Sun Jul 09 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.1-3
- A better fix, add requires gstreamer1-plugins-ugly-free-devel (rfbz #4589)

* Sun Jul 09 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.1-2
- Remove conflicting file in devel-docs (rfbz #4589)

* Fri Jun 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.1-1
- Update to 1.12.1

* Fri May 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.0-2
- Remove lame plugin

* Thu May 11 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.0-1
- Update to 1.12.0
- Add requires gstreamer1-plugins-ugly-free
- remove a52dec, cdio, dvdread and xingmux plugins,
  moved to gstreamer1-plugins-ugly-free package.
- Remove locale files

* Tue Apr 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.90-1
- Update to 1.11.90
- Upstream renamed libgstrmdemux.so to libgstrealmedia.so

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.2-1
- Update to 1.11.2
- Add upstream gcc-7 commit

* Mon Jan 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.1-1
- Update to 1.11.1
- Remove libmad bits as mad is no longer included in the source

* Wed Nov 30 2016 leigh scott <leigh123linux@googlemail.com> - 1.10.2-1
- Update to 1.10.2

* Fri Nov 18 2016 Adrian Reber <adrian@lisas.de> - 1.10.0-3
- Rebuilt for libcdio-0.94

* Sun Nov 13 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.10.0-2
- Drop mpg123 plugin, it is in Fedora proper now

* Fri Nov 11 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.10.0-1
- Rebase to new upstream release 1.10.0

* Sun Jun 12 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.8.2-1
- Rebase to new upstream release 1.8.2

* Wed May 18 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.8.1-1
- Rebase to new upstream release 1.8.1

* Sat Jan 23 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.6.3-1
- Rebase to new upstream release 1.6.3

* Thu Dec 24 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.6.2-1
- Rebase to new upstream release 1.6.2

* Sat Oct 31 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.6.1-1
- Rebase to new upstream release 1.6.1

* Sat May 16 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.5-1
- Rebase to new upstream release 1.4.5

* Wed Oct  1 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.3-1
- Rebase to new upstream release 1.4.3

* Fri Aug 29 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.1-1
- Rebase to new upstream release 1.4.1 (rf#3343)

* Sun Jun 15 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.4-1
- Rebase to new upstream release 1.2.4

* Sat Mar 22 2014 Sérgio Basto <sergio@serjux.com> - 1.2.3-3
- Rebuilt for x264

* Thu Mar 06 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.2.3-2
- Rebuilt for x264

* Sun Feb 23 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.3-1
- Rebase to new upstream release 1.2.3

* Fri Feb 21 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.2.1-2
- Rebuilt

* Sat Nov 16 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.1-1
- Rebase to new upstream release 1.2.1

* Tue Nov 05 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-3
- Rebuilt for x264/FFmpeg

* Tue Oct 22 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-2
- Rebuilt for x264

* Sun Oct 13 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.0-1
- Rebase to new upstream release 1.2.0

* Thu Aug 08 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.1.3-1
- Rebase to new upstream release 1.1.3

* Wed Aug 07 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.9-1
- New upstream release 1.0.9

* Tue May 07 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.6-2
- Rebuilt for x264

* Mon Mar 25 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.6-1
- New upstream release 1.0.6

* Sat Mar  2 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.5-1
- New upstream release 1.0.5
- Drop no longer needed PyXML BuildRequires (rf#2572)

* Sun Jan 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-3
- Rebuilt for FFmpeg/x264

* Fri Nov 23 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-2
- Rebuilt for x264

* Sun Oct 28 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.2-1
- New upstream release 1.0.2

* Sun Sep 23 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.99-1
- New upstream release 0.11.99

* Sun Sep 16 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.93-2
- Fix gtk-doc dir ownership (rf#2474)

* Sun Sep  9 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.93-1
- First version of gstreamer1-plugins-ugly for rpmfusion
