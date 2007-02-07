# Todo:
# - investigate the -fPIC flag on non x86_64 machines
#
Summary:	KSambaPlugin is KDE3 plugin for configuring SAMBA server
Summary(pl):	KSambaPlugin jest pluginem dla KDE3 do konfiguracji serwera SAMBA
Name:		ksambaplugin
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/ksambakdeplugin/%{name}-%{version}.tar.bz2
# Source0-md5:	d5f15874a226d99a1cc253363ba169ea
Patch0:		%{name}-build.patch
URL:		http://ksambakdeplugin.sourceforge.net/
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p1
mv %{name}-%{version} shit
mv shit/* .
rm -rf shit

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
# on x86_64 the linking stopped saying I need to pass that flag
# so I do it
export CXXFLAGS="-fPIC %{rpmcxxflags}"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Settings/Network/*.desktop \
      $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/ksambakonqiplugin.la
%attr(755,root,root) %{_libdir}/kde3/ksambakonqiplugin.so*
%{_libdir}/kde3/libkcm_kcmsambaconf.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_kcmsambaconf.so
%{_datadir}/services/ksambakonqiplugin.desktop
%{_desktopdir}/kcmsambaconf.desktop
%{_iconsdir}/*/*/*/kcmsambaconf.png
