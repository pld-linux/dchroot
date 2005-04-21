Summary:	Execute commands under different root filesystems
Summary(pl):	Wykonywanie poleceñ w innym g³ównym systemie
Name:		dchroot
Version:	0.11
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.gz
# Source0-md5:	7eba43966a03f8b3e0f3697eaa4416dc
URL:		http://packages.qa.debian.org/d/dchroot.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	help2man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Execute commands under different root filesystems.

%description -l pl
Wykonywanie poleceñ w innym g³ównym systemie.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make} docs \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO debian/changelog
%attr(4755,root,root) %{_bindir}/%{name}
%attr(640,root,root) %verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man?/*
