Summary:	backup software
Summary(pl):	Oprogramowanie do robienia kopii zapasowej
Name:		rdiff-backup
Version:	0.3.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
#Requires:	librsync
Requires:	Python >= 2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
rdiff-backup -- Mirror files while keeping incremental changes

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

cp rdiff-backup		$RPM_BUILD_ROOT%{_bindir}
cp rdiff-backup.1	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf CHANGELOG FAQ.html README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/rdiff-backup
%{_mandir}/man1/rdiff-backup.1.gz
