
Summary:	General-purpose library
Name:		libHX
Version:	1.10.2
Release:	1
License:	LGPL2 LGPL3 but NOT LATER
Group:		Libraries
Source0:	http://jengelh.hopto.org/f/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	913d01d511c8378d7e563cfd3aa439ba
URL:		http://jengelh.hopto.org/p/%{name}/
#BuildRequires:	autoconf >= 2.50
#BuildRequires:	automake
#BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for:
- A+R/B trees to use for lists or maps (associative arrays)
- Deques (double-ended queues) (Stacks (LIFO) / Queues (FIFOs))
- platform independent opendir-style directory access
- platform independent dlopen-style shared library access
- auto-storage strings with direct access
- command line option (argv) parser
- shell-style config file parser
- platform independent random number generator with transparent
  /dev/urandom support
- various string, memory and zvec ops

%package devel
Summary:	libHX header files
Summary(pl.UTF-8):	Pliki nagłówkowe libHX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libHX header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe libHX.

%package static
Summary:	libHX static library
Summary(pl.UTF-8):	Statyczna biblioteka libHX
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libHX static library.

%description static -l pl.UTF-8
Statyczna biblioteka libHX.

%prep
%setup -q

%build
# supplied libtool is broken (no C++ libraries support)
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
