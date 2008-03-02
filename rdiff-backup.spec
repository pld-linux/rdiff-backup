Summary:	Backup software
Summary(pl.UTF-8):	Oprogramowanie do robienia kopii zapasowych
Name:		rdiff-backup
Version:	1.1.15
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://savannah.nongnu.org/download/rdiff-backup/%{name}-%{version}.tar.gz
# Source0-md5:	7c3dfae289d0f4dea3647ae2831c46c7
URL:		http://www.nongnu.org/rdiff-backup/
BuildRequires:	librsync-devel >= 0.9.6
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-pylibacl
Requires:	python-pyxattr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdiff-backup is a script, written in Python, that backs up one
directory to another and is intended to be run periodically (nightly
from cron for instance). The target directory ends up a copy of the
source directory, but extra reverse diffs are stored in the target
directory, so you can still recover files lost some time ago. The idea
is to combine the best features of a mirror and an incremental backup.
rdiff-backup can also operate in a bandwidth efficient manner over a
pipe, like rsync. Thus you can use rdiff-backup and SSH to securely
back a hard drive up to a remote location, and only the differences
from the previous backup will be transmitted.

%description -l pl.UTF-8
rdiff-backup jest skryptem napisanym w Pythonie, służącym do robienia
kopii zapasowych. Pomyślany został w taki sposób, aby działać okresowo
- na przykład w nocy, poprzez crona. Katalog docelowy po zakończeniu
działania skryptu zawiera kopię katalogu źródłowego, ale dodatkowo w
katalogu docelowym przechowywane są dodatkowe informacje o zmianach,
co umożliwia odzyskanie plików sprzed jakiegoś czasu. Ideą działania
skryptu jest połączenie funkcjonalności mirrorowania oraz
przyrostowych kopii zapasowych. rdiff-backup potrafi również być
przyjaznym dla łącza umożliwiając backup przez sieć z wykorzystaniem
bezpiecznego połączenia SSH, gdzie jedynymi przesyłanymi danymi będą
różnice w stosunku do poprzedniej kopii zapasowej.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README FAQ.html examples.html
%attr(755,root,root) %{_bindir}/rdiff-backup
%attr(755,root,root) %{_bindir}/rdiff-backup-statistics
%{_mandir}/man1/rdiff-backup.1*
%{_mandir}/man1/rdiff-backup-statistics.1*
%dir %{py_sitedir}/rdiff_backup
%{py_sitedir}/rdiff_backup/*.py[co]
%attr(755,root,root) %{py_sitedir}/rdiff_backup/*.so
