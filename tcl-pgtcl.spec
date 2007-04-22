# TODO: extra (pgtclsh, pgwish) - messy Makefile, requires libpgtcl in library path and with proper soname
Summary:	pgtcl-ng - Tcl interface for PostgreSQL
Summary(pl.UTF-8):	pgtcl-ng - interfejs Tcl dla PostgreSQL
Name:		tcl-pgtcl
Version:	1.6.0
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://pgfoundry.org/frs/download.php/1229/pgtcl%{version}.tar.gz
# Source0-md5:	25eda4bb40fb3d4ec9b205a1fdc1bbbc
URL:		http://pgfoundry.org/projects/pgtclng/
BuildRequires:	postgresql-devel
BuildRequires:	tcl-devel >= 8
Provides:	tcl(Pgtcl)
Obsoletes:	postgresql-tcl
Obsoletes:	tcl-libpgtcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pgtcl is the Tcl interface for the PostgreSQL Database Management
System. It is a loadable Tcl module implementing commands which allow
an application to interact with a PostgreSQL database. pgtcl-ng is a
new revision of the pgtcl interface.

%description -l pl.UTF-8
pgtcl to interfejs Tcl do systemu baz danych PostgreSQL. Jest to
ładowalny moduł Tcl-a implementujący polecenia pozwalające aplikacji
współpracować z bazą danych PostgreSQL. pgtcl-ng to nowa wersja
interfejsu pgtcl.

%package devel
Summary:	C header file for pgtcl-ng interface
Summary(pl.UTF-8):	Plik nagłówkowy C dla interfejsu pgtcl-ng
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	postgresql-devel
Obsoletes:	postgresql-tcl-devel
Obsoletes:	postgresql-tcl-static
Obsoletes:	tcl-libpgtcl-devel

%description devel
C header file for pgtcl-ng interface.

%description devel -l pl.UTF-8
Plik nagłówkowy C dla interfejsu pgtcl-ng.

%prep
%setup -q -n pgtcl%{version}

%build
%configure

%{__make} \
	CFLAGS_OPTIMIZE="%{rpmcflags} -D__NO_STRING_INLINES -D__NO_MATH_INLINES"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog* NEWS README*
%dir %{_libdir}/pgtcl%{version}
%attr(755,root,root) %{_libdir}/pgtcl%{version}/libpgtcl%{version}.so
%{_libdir}/pgtcl%{version}/pkgIndex.tcl

%files devel
%defattr(644,root,root,755)
%{_includedir}/libpgtcl.h
