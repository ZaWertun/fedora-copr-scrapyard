%global real_name   systemd-bootchart

%global commit      6bc59c0eed61fb28f23fc631d6c269cf87344c30
%global commitdate  20190606
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           systemd-bootchart-user
Version:        233
Release:        1.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Fork of systemd-bootchart that tracks processes of current user

License:        GPLv2 and LGPLv2.1
URL:            https://github.com/davidedmundson/systemd-bootchart
Source0:        %{url}/archive/%{commit}/%{real_name}-%{shortcommit}.tar.gz
Source1:        ++-systemd-bootchart-user.sh

Patch0:         fix-crash.patch

BuildRequires:  gcc make automake autoconf autoconf-archive intltool libtool

BuildRequires:  %{_bindir}/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  pkgconfig(libsystemd)


%description
%{summary}.


%prep
%autosetup -n %{real_name}-%{commit} -p1


%build
./autogen.sh
%configure
%make_build


%install
%__install -Dp -m755 %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/++-systemd-bootchart-user.sh
%__install -Dp -m755 systemd-bootchart %{buildroot}/%{_bindir}/%{name}


%files
%license LICENSE.GPL2 LICENSE.LGPL2.1
%{_bindir}/%{name}
%{_sysconfdir}/X11/xinit/xinitrc.d/++-systemd-bootchart-user.sh


%changelog
* Thu Nov 12 11:34:12 MSK 2020 Yaroslav Sidlovsky <zawertun@gmail.com>
- first spec
