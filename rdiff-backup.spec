%include        /usr/lib/rpm/macros.python
Summary:	Backup software
Summary(pl):	Oprogramowanie do robienia kopii zapasowych
Name:		rdiff-backup
Version:	0.13.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://rdiff-backup.stanford.edu/%{name}-%{version}.tar.gz
# Source0-md5:	f2c75e5734cb641f04ed1cd545417acd
URL:		http://rdiff-backup.stanford.edu/
BuildRequires:	librsync-devel >= 0.9.6
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdiff-backup is a script, written in Python, that backs up one
directory to another and is intended to be run periodically (nightly
from cron for instance). The target directory ends up a copy of the
source directory, but extra reverse diffs are stored in the target
directory, so you can still recover files lost some time ago. The idea
is to combine the best features of a mirror and an incremental backup.
rdiff-backup can also operate in a bandwidth efficient manner over a
pipe, like rsync. Thus you can use rdiff-backup and ssh to securely
back a hard drive up to a remote location, and only the differences
from the previous backup will be transmitted.

%description -l pl
rdiff-backup jest skryptem napisanym w Pythonie, s³u¿±cym do robienia
kopii zapasowych. Pomy¶lany zosta³ w taki sposób, aby dzia³aæ
okresowo - na przyk³ad w nocy, poprzez crona. Katalog docelowy po
zakoñczeniu dzia³ania skryptu zawiera kopiê katalogu ¼ród³owego, ale
dodatkowo w katalogu docelowym przechowywane s± dodatkowe informacje o
zmianach, co umo¿liwia odzyskanie plików sprzed jakiego¶ czasu. Ide±
dzia³ania skryptu jest po³±czenie funkcjonalno¶ci mirrorowania oraz
przyrostowych kopii zapasowych. rdiff-backup potrafi równie¿ byæ
przyjaznym dla ³±cza umo¿liwiaj±c backup przez sieæ z wykorzystaniem
bezpiecznego po³±czenia ssh, gdzie jedynymi przesy³anymi danymi bêd±
ró¿nice w stosunku do poprzedniej kopii zapasowej.

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
%doc CHANGELOG README FAQ.html
%attr(755,root,root) %{_bindir}/rdiff-backup
%{_mandir}/man1/rdiff-backup.1*
%dir %{py_sitedir}/rdiff_backup
%{py_sitedir}/rdiff_backup/*.py[co]
%attr(755,root,root) %{py_sitedir}/rdiff_backup/*.so
