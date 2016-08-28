Summary:	J.Engelh's general-purpose library
Summary(pl.UTF-8):	Biblioteka ogólnego przeznaczenia J. Engelha
Name:		libHX
Version:	3.12.1
Release:	2
License:	LGPL v2 or LGPL v3
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libhx/%{name}-%{version}.tar.xz
# Source0-md5:	de66ebb98e73ffd4831090257a7b9533
URL:		http://libhx.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz >= 1:4.999.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
J. Engelh's general-purpose library for:
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

%description -l pl.UTF-8
Biblioteka J. Engelha ogólnego przeznaczenia, obejmująca:
- drzewa czerwono-czarne do list i tablic asocjacyjnych
- kolejki o dwóch końcach (stosy LIFO/kolejki FIFO)
- niezależny od platformy dostęp do katalogów w stylu opendir
- niezależny od platformy dostęp do bibliotek współdzielonych w stylu
  dlopen
- łańcuchy znaków z automatycznym zarządzaniem pamięcią i bezpośrednim
  dostępem
- analizator opcji linii poleceń (argv)
- analizator plików konfiguracyjnych w stylu powłoki sh
- niezależny od platformy generator liczb losowych z przezroczystą
  obsługą /dev/urandom
- różne operacje na łańcuchach znaków, pamięci i strukturach zvec

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
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-static

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libhx

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/changelog.txt doc/libHX_Documentation.pdf
%attr(755,root,root) %{_libdir}/libHX.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libHX.so.28
%{_libdir}/libHX_rtcheck.so

%files devel
%defattr(644,root,root,755)
%doc doc/[!c]*.txt
%attr(755,root,root) %{_libdir}/libHX.so
%{_includedir}/libHX.h
%{_includedir}/%{name}
%{_pkgconfigdir}/libHX.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libHX.a
%{_libdir}/libHX_rtcheck.a
