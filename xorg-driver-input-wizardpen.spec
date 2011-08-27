%define		relname		xorg-input-wizardpen
Summary:	X.org input driver for most non-Wacom graphics pads
Summary(pl.UTF-8):	Sterownik wejściowy X.org do większości tabletów nie-Wacoma
Name:		xorg-driver-input-wizardpen
Version:	0.8.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://launchpad.net/wizardpen/trunk/0.8/+download/%{relname}-%{version}.tar.gz
# Source0-md5:	af818b824b1b808c851279ec604a1ac6
URL:		https://launchpad.net/wizardpen
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for most non-Wacom graphics pads.

Supported tablets: Acecad Flair II GT-504, DigiPro 5.5×4” Graphics
Tablet, Digital Ink Pad (A4 format), G-pen, Genius Wizardpen, Genius
Mousepen, Genius Easypen i405, Genius, iBall, Manhattan, Pentagram,
QWare, Trust TB-3100, Trust TB-5300, Trust TB-6300, UC-LOGIC, iBall
Tablet PF8060, AIPTEK HyperPen 10000 U, AIPTEK Slim Tablet U600
Premium II

%description -l pl.UTF-8
Sterownik wejściowy X.org dla następujących tabletów:

Acecad Flair II GT-504, DigiPro 5.5×4” Graphics Tablet, Digital Ink
Pad (A4 format), G-pen, Genius Wizardpen, Genius Mousepen, Genius
Easypen i405, Genius, iBall, Manhattan, Pentagram, QWare, Trust
TB-3100, Trust TB-5300, Trust TB-6300, UC-LOGIC, iBall Tablet PF8060,
AIPTEK HyperPen 10000 U, AIPTEK Slim Tablet U600 Premium II

%prep
%setup -q -n %{relname}-%{version}

%build

%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	 --with-xorg-conf-dir=%{_datadir}/X11/xorg.conf.d/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/wizardpen-calibrate
%attr(755,root,root) %{_libdir}/xorg/modules/input/wizardpen_drv.so
%{_sysconfdir}/udev/rules.d/70-xorg-wizardpen-settings.rules
/lib/udev/rules.d/67-xorg-wizardpen.rules
%{_mandir}/man4/wizardpen.4*
%{_datadir}/X11/xorg.conf.d/*
