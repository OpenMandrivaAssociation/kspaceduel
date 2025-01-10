#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		plasma6-kspaceduel
Version:	24.12.1
Release:	%{?git:0.%{git}.}1
Summary:	Two player game with shooting spaceships flying around a sun
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/kspaceduel/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kspaceduel/-/archive/%{gitbranch}/kspaceduel-%{gitbranchd}.tar.bz2#/kspaceduel-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kspaceduel-%{version}.tar.xz
%endif
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)

%description
In KSpaceDuel each of two possible players control a satellite spaceship
orbiting the sun. As the game progresses players have to eliminate the
opponent's spacecraft with bullets or mines.

%files -f %{name}.lang
%{_bindir}/kspaceduel
%{_datadir}/applications/org.kde.kspaceduel.desktop
%{_datadir}/kspaceduel
%{_iconsdir}/hicolor/*/apps/kspaceduel.png
%{_datadir}/config.kcfg/kspaceduel.kcfg
%{_datadir}/metainfo/org.kde.kspaceduel.appdata.xml

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kspaceduel-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
