Name:           baresip
Version:        0.4.5
Release:        1%{?dist}
Summary:        A simple SIP user agent

License:        BSD
URL:            http://www.creytiv.com/baresip.html
Source0:        http://www.creytiv.com/pub/%{name}-%{version}.tar.gz

BuildRequires:  re-devel
BuildRequires:  rem-devel
BuildRequires:  alsa-lib-devel

%description
Baresip is a portable and modular SIP User-Agent with audio and video support. 

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install LIBDIR=%{_libdir}


%files
%doc docs/*
%{_bindir}/baresip
%{_libdir}/baresip
%{_datadir}/baresip

%changelog
* Fri Sep 27 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.5-1
- initial package build

