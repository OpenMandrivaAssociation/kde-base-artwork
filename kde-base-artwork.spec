Name:		kde-base-artwork
Summary:	KDE 4 application workspace components
Version:	4.10.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildArch:	noarch
Conflicts:	kdebase4-workspace < 2:4.9.1

%description
This package provides the Air and Ariya Splash Screen.

%files
%doc COPYING
%{_kde_appsdir}/ksplash/Themes/Air

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# Rename Default ksplashx folder to Air & edit the Theme.rc to match the folder name so we can have a description
sed -i 's/KSplash\ Theme\:\ Default/KSplash\ Theme\:\ Air/' %{buildroot}%{_kde_appsdir}/ksplash/Themes/Default/Theme.rc
sed -i 's/Default\ Splash\ Screen/Air\ and\ Ariya\ Splash\ Screen/' %{buildroot}%{_kde_appsdir}/ksplash/Themes/Default/Theme.rc
mv %{buildroot}%{_kde_appsdir}/ksplash/Themes/Default/ %{buildroot}%{_kde_appsdir}/ksplash/Themes/Air

%changelog
* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

