Name:           baresip
Version:        0.4.5
Release:        3%{?dist}
Summary:        A simple SIP user agent

License:        BSD
URL:            http://www.creytiv.com/baresip.html
Source0:        http://www.creytiv.com/pub/%{name}-%{version}.tar.gz

BuildRequires:  re-devel
BuildRequires:  rem-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libXau-devel
BuildRequires:  libXext-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel

Patch100:	enable-alsa-by-default.patch

%description
Baresip is a portable and modular SIP User-Agent with audio and video support. 

%prep
%setup -q

# Use ALSA audio driver by default.
%patch100 -p1 -b.alsa

%build
make %{?_smp_mflags} PREFIX=%{_prefix}


%install
rm -rf $RPM_BUILD_ROOT
%make_install PREFIX=%{_prefix}


%files
%doc docs/*
%{_bindir}/baresip
%{_prefix}/lib/baresip/modules/x11.so
%{_prefix}/lib/baresip/modules/ice.so
%{_prefix}/lib/baresip/modules/selfview.so
%{_prefix}/lib/baresip/modules/vumeter.so
%{_prefix}/lib/baresip/modules/mwi.so
%{_prefix}/lib/baresip/modules/l16.so
%{_prefix}/lib/baresip/modules/x11grab.so
%{_prefix}/lib/baresip/modules/presence.so
%{_prefix}/lib/baresip/modules/syslog.so
%{_prefix}/lib/baresip/modules/natbd.so
%{_prefix}/lib/baresip/modules/vidloop.so
%{_prefix}/lib/baresip/modules/turn.so
%{_prefix}/lib/baresip/modules/menu.so
%{_prefix}/lib/baresip/modules/g711.so
%{_prefix}/lib/baresip/modules/cons.so
%{_prefix}/lib/baresip/modules/account.so
%{_prefix}/lib/baresip/modules/evdev.so
%{_prefix}/lib/baresip/modules/contact.so
%{_prefix}/lib/baresip/modules/alsa.so
%{_prefix}/lib/baresip/modules/auloop.so
%{_prefix}/lib/baresip/modules/natpmp.so
%{_prefix}/lib/baresip/modules/stdio.so
%{_prefix}/lib/baresip/modules/oss.so
%{_prefix}/lib/baresip/modules/stun.so
%{_datadir}/baresip

%changelog
* Fri Sep 27 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.5-2
- baresip use PREFIX/lib instead of LIBDIR for locating modules

* Fri Sep 27 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.5-1
- initial package build

