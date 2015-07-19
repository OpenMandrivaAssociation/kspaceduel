Name:		kspaceduel
Version:	15.04.3
Release:	2
Epoch:		1
Summary:	Two player game with shooting spaceships flying around a sun
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kspaceduel/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs-devel
BuildRequires:	cmake(KDEGames)

%description
In KSpaceDuel each of two possible players control a satellite spaceship
orbiting the sun. As the game progresses players have to eliminate the
opponent's spacecraft with bullets or mines.

%files
%{_bindir}/kspaceduel                                                                                  
%{_datadir}/applications/kde4/kspaceduel.desktop                                                       
%{_datadir}/apps/kspaceduel                                                                            
%doc %{_docdir}/*/*/kspaceduel                                                                         
%{_iconsdir}/hicolor/*/apps/kspaceduel.png                                                             
%{_datadir}/config.kcfg/kspaceduel.kcfg        

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

