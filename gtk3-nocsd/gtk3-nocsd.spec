Name:    gtk3-nocsd
Version: 3.0.6
Release: 1%{?dist}
Summary: A hack to disable gtk+ 3 client side decoration

License: LGPLv2.1
URL:     https://github.com/ZaWertun/%{name}
Source0: https://github.com/ZaWertun/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig gcc sed make
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)

%description
%{summary}.


%prep
%autosetup -n %{name}-%{version}


%build
sed -i 's|#!/bin/sh|#!/usr/bin/sh|' gtk3-nocsd.in

LDLIBS="%build_ldflags" make %{?_smp_mflags} libdir=%{_libdir}


%install
%make_install prefix=%{_prefix} libdir=%{_libdir}

gzip -9 %{buildroot}%{_mandir}/man1/*.1
chmod +x %{buildroot}%{_libdir}/lib%{name}.so.0


%check
%{__make} check


%files
%doc README.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.0
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/bash-completion/completions/gtk3-nocsd


%changelog
* Sat Jun 19 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.0.6-1
- version 3.0.6

* Thu Apr 29 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.0.5-1
- version 3.0.5

* Tue Sep 22 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.0.4-1
- version 3.0.4

* Sat Jun 13 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.0.2-1
- version 3.0.2

* Mon Jul 29 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.0.1-5
- version 3.0.1

* Wed Feb 20 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 3-4.20190220gitcc31f53
- one more fix

* Wed Feb 20 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 3-3.20190220gita8965b8
- switched to my repo, it contains several fixes

* Tue Feb 19 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 3-2.20160617git82ff5a0
- added patch to fix issue in Geary:
  create account dialog disappears after selecting provider


