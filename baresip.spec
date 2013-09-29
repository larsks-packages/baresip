Name:           baresip
Version:        0.4.5
Release:        4%{?dist}
Summary:        A simple SIP user agent

License:        BSD
URL:            http://www.creytiv.com/baresip.html
Source0:        http://www.creytiv.com/pub/%{name}-%{version}.tar.gz
Patch100:       baresip-0.4.5-enable-alsa-by-default.patch
Patch101:	baresip-0.4.5-modules-in-libdir.patch

BuildRequires:  re-devel
BuildRequires:  rem-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libXau-devel
BuildRequires:  libXext-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel

%description
Baresip is a portable and modular SIP User-Agent with audio and video support. 

%prep
%setup -q

# Use ALSA audio driver by default.
%patch100 -p1 -b.alsa
%patch101 -p1 -b.libdir

%build
make %{?_smp_mflags} PREFIX=%{_prefix} LIBDIR=%{_libdir}


%install
rm -rf $RPM_BUILD_ROOT
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}


%files
%doc docs/*
%{_bindir}/baresip
%{_libdir}/baresip/modules/x11.so
%{_libdir}/baresip/modules/ice.so
%{_libdir}/baresip/modules/selfview.so
%{_libdir}/baresip/modules/vumeter.so
%{_libdir}/baresip/modules/mwi.so
%{_libdir}/baresip/modules/l16.so
%{_libdir}/baresip/modules/x11grab.so
%{_libdir}/baresip/modules/presence.so
%{_libdir}/baresip/modules/syslog.so
%{_libdir}/baresip/modules/natbd.so
%{_libdir}/baresip/modules/vidloop.so
%{_libdir}/baresip/modules/turn.so
%{_libdir}/baresip/modules/menu.so
%{_libdir}/baresip/modules/g711.so
%{_libdir}/baresip/modules/cons.so
%{_libdir}/baresip/modules/account.so
%{_libdir}/baresip/modules/evdev.so
%{_libdir}/baresip/modules/contact.so
%{_libdir}/baresip/modules/alsa.so
%{_libdir}/baresip/modules/auloop.so
%{_libdir}/baresip/modules/natpmp.so
%{_libdir}/baresip/modules/stdio.so
%{_libdir}/baresip/modules/oss.so
%{_libdir}/baresip/modules/stun.so
%{_datadir}/baresip

%changelog
* Fri Sep 27 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.5-4
- make rpmlint happy: patch baresip to use _libdir for modules.

* Fri Sep 27 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.5-2
- baresip use PREFIX/lib instead of LIBDIR for locating modules

* Fri Sep 27 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.5-1
- initial package build

