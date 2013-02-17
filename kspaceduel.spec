Name:		kspaceduel
Version:	4.10.0
Release:	1
Epoch:		1
Summary:	Two player game with shooting spaceships flying around a sun
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kspaceduel/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
In KSpaceDuel each of two possible players control a satellite spaceship
orbiting the sun. As the game progresses players have to eliminate the
opponent's spacecraft with bullets or mines.

%files
%{_kde_bindir}/kspaceduel
%{_kde_applicationsdir}/kspaceduel.desktop
%{_kde_appsdir}/kspaceduel
%{_kde_docdir}/*/*/kspaceduel
%{_kde_iconsdir}/hicolor/*/apps/kspaceduel.png
%{_kde_datadir}/config.kcfg/kspaceduel.kcfg

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

