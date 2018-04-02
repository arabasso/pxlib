Name:           pxlib
Version:        0.6.8
Release:        0
Summary:        Library to read and write Paradox databases
Group:          Applications/Multimedia
License:        GPL
URL:            http://pxlib.sourceforge.net/
Vendor:         Uwe Steinmann
Source:         https://ufpr.dl.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
Prefix:         %{_prefix}
Packager: 	    arabasso
BuildRoot:      %{_tmppath}/%{name}-root

%description
pxlib is a simply and still small C library to read and write Paradox DB files. It supports all versions starting from 3.0. It currently has a very limited set of functions like to open a DB file, read its header and read every single record. It can read and write blob data. The write support is still a bit experimental.

%package devel
Summary:        Library to read and write Paradox databases
Group:          Development/Libraries
Provides:       pxlib-devel
Requires:       pxlib

%description devel
pxlib is a simply and still small C library to read and write Paradox DB files. It supports all versions starting from 3.0. It currently has a very limited set of functions like to open a DB file, read its header and read every single record. It can read and write blob data. The write support is still a bit experimental.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --mandir=%{_mandir}

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
%{_libdir}/libpx.so
%{_libdir}/libpx.so.0
%{_libdir}/libpx.so.0.6.8
%{_libdir}/pkgconfig/pxlib.pc
%{_prefix}/share/*
%exclude /usr/include/paradox-gsf.h
%exclude /usr/include/paradox-mp.h
%exclude /usr/include/paradox.h
%exclude /usr/include/pxversion.h
%exclude /usr/lib64/libpx.a
%exclude /usr/lib64/libpx.la

%files devel
%defattr(-,root,root)
#%doc README AUTHORS COPYING NEWS TODO ChangeLog
#%doc doc/*.html
#%doc doc/*.jpg
#%doc doc/*.css
#%config(noreplace) /etc/%{name}.xml
%exclude /usr/lib64/libpx.so
%exclude /usr/lib64/libpx.so.0
%exclude /usr/lib64/libpx.so.0.6.8
%exclude /usr/lib64/pkgconfig/pxlib.pc
%exclude /usr/lib64/share/*
%{_prefix}/include/paradox-gsf.h
%{_prefix}/include/paradox-mp.h
%{_prefix}/include/paradox.h
%{_prefix}/include/pxversion.h
%{_libdir}/libpx.a
%{_libdir}/libpx.la

%changelog
