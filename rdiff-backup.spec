%include        /usr/lib/rpm/macros.python

Summary:	backup software
Summary(pl):	Oprogramowanie do robienia kopii zapasowej
Name:		rdiff-backup
Version:	0.12.6
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://rdiff-backup.stanford.edu/%{name}-%{version}.tar.gz
# Source0-md5:	49d7baedd303fb278a65682064ec8c64
URL:		http://rdiff-backup.stanford.edu/
BuildRequires:	librsync-devel >= 0.9.6
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
Requires:	python >= 2.2
Requires:	python-modules
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
Mirrorowanie plików przy przechowywaniu przyrostowych zmian.

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
%{py_sitedir}/rdiff_backup/*.so
