%undefine __cmake_in_source_build

Name:           xwinmosaic
Version:        0.4.3
License:        BSD-3-Clause
Release:        2%{?dist}
Summary:        X11 window switcher that draws windows list as colour mosaic
Url:            https://github.com/ZaWertun/xwinmosaic
Group:          Applications/Productivity
Source:         https://github.com/ZaWertun/xwinmosaic/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  gtk2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  xorg-x11-proto-devel

%description
Inspired by XMonad.Actions.GridSelect, but written in C + GTK+2, uses
nice-looking colours and has some set of helpful features.

%prep
%autosetup

%build
%cmake .
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root)
%doc %{_mandir}/man1/xwinmosaic.1.gz
%doc LICENSE README.md
%{_bindir}/xwinmosaic

%changelog
* Sat Sep 19 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.4.3-2
- new crutches

* Wed Mar 25 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.4.3-1
- version 0.4.3

* Mon Mar 25 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.4.2.2-3
- version 0.4.2.2

* Mon May 21 2018 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.4.2.1-2
- version 0.4.2.1

* Sun Mar 01 2015 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.4.1.1-1
- initial version

