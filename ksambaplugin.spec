Summary:	KSambaPlugin is KDE3 plugin for configuring SAMBA server
Summary(pl):	KSambaPlugin jest pluginem dla KDE3 do konfiguracji serwera SAMBA
Name:		ksambaplugin
Version:	0.4.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://download.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.bz2
URL:		http://ksambakdeplugin.sourceforge.net
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KSambaPlugin is a KDE 3 plugin for configuring a SAMBA server. It
consists of two plugins, a KControl Center module for all SAMBA
options and a Konqueror properties dialog plugin for quickly
configuring the SAMBA share options of a directory. It is meant to be
a full SAMBA configuration tool.

%description -l pl
KSambaPlugin jest pluginem dla KDE3 s³u¿±cym do konfiguracji serwera
SAMBA. Sk³ada siê z dwóch czê¶ci: modu³u KControl Center dla
wszystkich opcji SAMBY i plugina w dialogu w³a¶ciwo¶ci w Konquerorze
do szybkiego skonfigurowania opcji udostêpniania katalogu w SAMBIE.
Jest pomy¶lana jako pe³ne narzêdzie do konfiguracji SAMBY.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE
mv $RPM_BUILD_ROOT%{_applnkdir}/{Settings/[!K]*,Settings/KDE}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/ksambakonqiplugin.la
%attr(755,root,root) %{_libdir}/kde3/ksambakonqiplugin.so*
%{_libdir}/kde3/libkcm_kcmsambaconf.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_kcmsambaconf.so
%{_datadir}/services/ksambakonqiplugin.desktop
%{_applnkdir}/Settings/KDE/Network/kcmsambaconf.desktop
%{_pixmapsdir}/*/*/*/kcmsambaconf.png
