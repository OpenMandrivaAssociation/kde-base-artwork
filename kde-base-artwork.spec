Summary:	KDE 4 application workspace components
Name:		kde-base-artwork
Version:	4.12.1
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.kde.org
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
* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

