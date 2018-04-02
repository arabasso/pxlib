Name:           pxview
Version:        0.2.5
Release:        0
Summary:        Program to convert Paradox databases
Group:          Applications/Databases
License:        GPL
URL:            http://pxlib.sourceforge.net/pxview/
Vendor:         Uwe Steinmann
Source:         https://ufpr.dl.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
Prefix:         %{_prefix}
Packager:       arabasso
BuildRoot:      %{_tmppath}/%{name}-root
Requires:       pxlib sqlite2

%description
pxview is a program to read Paradox database files. It is based on the pxlib library. pxview allows to output csv for reading with spread sheets, sql to import into a relational database, html and sqlite. You can also just show some information and the table structure of the database. 

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LIBS=-lm ./configure --prefix=%{_prefix} --mandir=%{_mandir} --with-sqlite
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%doc README AUTHORS COPYING NEWS TODO ChangeLog
#%doc doc/*.html
#%doc doc/*.jpg
#%doc doc/*.css
#%config(noreplace) /etc/%{name}.xml
%{_bindir}/pxview
%{_prefix}/share/*

%changelog
