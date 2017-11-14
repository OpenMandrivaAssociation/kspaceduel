%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		kspaceduel
Version:	17.08.3
Release:	1
Epoch:		1
Summary:	Two player game with shooting spaceships flying around a sun
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kspaceduel/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

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
%{_datadir}/kxmlgui5/kspaceduel/kspaceduelui.rc
%{_datadir}/metainfo/org.kde.kspaceduel.appdata.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
