Summary:	Backup software
Summary(pl):	Oprogramowanie do robienia kopii zapasowych
Name:		rdiff-backup
Version:	1.0.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://savannah.nongnu.org/download/rdiff-backup/%{name}-%{version}.tar.gz
# Source0-md5:	dedae55157ec11d046ffd79bd48db25c
URL:		http://www.nongnu.org/rdiff-backup/
BuildRequires:	librsync-devel >= 0.9.6
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 2.2.1
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

%description -l pl
rdiff-backup jest skryptem napisanym w Pythonie, s�u��cym do robienia
kopii zapasowych. Pomy�lany zosta� w taki spos�b, aby dzia�a� okresowo
- na przyk�ad w nocy, poprzez crona. Katalog docelowy po zako�czeniu
dzia�ania skryptu zawiera kopi� katalogu �r�d�owego, ale dodatkowo w
katalogu docelowym przechowywane s� dodatkowe informacje o zmianach,
co umo�liwia odzyskanie plik�w sprzed jakiego� czasu. Ide� dzia�ania
skryptu jest po��czenie funkcjonalno�ci mirrorowania oraz
przyrostowych kopii zapasowych. rdiff-backup potrafi r�wnie� by�
przyjaznym dla ��cza umo�liwiaj�c backup przez sie� z wykorzystaniem
bezpiecznego po��czenia SSH, gdzie jedynymi przesy�anymi danymi b�d�
r�nice w stosunku do poprzedniej kopii zapasowej.

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
%{_mandir}/man1/rdiff-backup.1*
%dir %{py_sitedir}/rdiff_backup
%{py_sitedir}/rdiff_backup/*.py[co]
%attr(755,root,root) %{py_sitedir}/rdiff_backup/*.so
