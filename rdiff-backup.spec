Summary:	backup software
Summary(pl):	Oprogramowanie do robienia kopii zapasowej
Name:		rdiff-backup
Version:	0.3.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	%{name}-%{version}.tar.gz
#Requires:	librsync
Requires:	python >= 2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
rdiff-backup - Mirror files while keeping incremental changes.

%description -l pl
Mirrorowanie plików przy przechowywaniu przyrostowych zmian.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install rdiff-backup	$RPM_BUILD_ROOT%{_bindir}
install rdiff-backup.1	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf CHANGELOG README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz FAQ.html
%attr(755,root,root) %{_bindir}/rdiff-backup
%{_mandir}/man1/rdiff-backup.1*
