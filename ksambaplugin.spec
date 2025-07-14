Summary:	KSambaPlugin - KDE3 plugin for configuring SAMBA server
Summary(pl.UTF-8):	KSambaPlugin - wtyczka KDE3 do konfiguracji serwera SAMBA
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
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSambaPlugin is a KDE 3 plugin for configuring a SAMBA server. It
consists of two plugins, a KControl Center module for all SAMBA
options and a Konqueror properties dialog plugin for quickly
configuring the SAMBA share options of a directory. It is meant to be
a full SAMBA configuration tool.

%description -l pl.UTF-8
KSambaPlugin jest wtyczką KDE3 służącym do konfiguracji serwera SAMBA.
Składa się z dwóch części: modułu KControl Center dla wszystkich opcji
SAMBY i wtyczki okna dialogowego właściwości w Konquerorze do
szybkiego skonfigurowania opcji udostępniania katalogu w SAMBIE. Jest
pomyślana jako pełne narzędzie do konfiguracji SAMBY.

%prep
%setup -q
%patch -P0 -p1
mv %{name}-%{version}/* .
rmdir %{name}-%{version}

# -Wmissing-prototypes is not a valid g++ option, breaks detection of another options
sed -i -e 's/\(CXXFLAGS=.*\) -Wmissing-prototypes/\1/' configure

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mydatadir=%{_desktopdir}/kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/ksambakonqiplugin.la
%attr(755,root,root) %{_libdir}/kde3/ksambakonqiplugin.so*
%{_libdir}/kde3/libkcm_kcmsambaconf.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_kcmsambaconf.so
%{_datadir}/services/ksambakonqiplugin.desktop
%{_desktopdir}/kde/kcmsambaconf.desktop
%{_iconsdir}/hicolor/16x16/apps/kcmsambaconf.png
