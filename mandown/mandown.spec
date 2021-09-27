Name:           mandown
Version:        1.0.3
Release:        1%{?dist}
Summary:        Man-page inspired Markdown viewer

License:        MIT
URL:            https://github.com/Titor8115/mandown
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel

%description
%{summary}.


%prep
%autosetup -p1

sed -i 's|CFLAGS = -c -g -O3|CFLAGS = %{optflags}|' Makefile
sed -i 's|LDFLAGS = -g -O3|LDFLAGS = %{optflags}|' Makefile
sed -i 's|$(CC) $^ -o $@ $(LDLIB) $(LDFLAGS)|$(CC) $^ -o $@ $(LDLIB) $(LDFLAGS) $(REAL_LDFLAGS)|' Makefile


%build
REAL_LDFLAGS="%{__global_ldflags}" \
    %make_build


%install
%{__install} -D -m 0755 mdn %{buildroot}%{_bindir}/mdn


%files
%doc README.md
%license LICENSE
%{_bindir}/mdn


%changelog
* Mon Sep 27 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.3-1
- version 1.0.3

* Wed Jul 01 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.1-1
- version 1.0.1

* Sat Jun 13 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.3-1
- version 0.3

* Mon May 11 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.2-1
- first spec for version 0.2

