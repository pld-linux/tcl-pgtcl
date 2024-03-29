# TODO: extra (pgtclsh, pgwish) - messy Makefile, requires libpgtcl in library path and with proper soname
Summary:	pgtcl-ng - Tcl interface for PostgreSQL
Summary(pl.UTF-8):	pgtcl-ng - interfejs Tcl dla PostgreSQL
Name:		tcl-pgtcl
Version:	3.0.0
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	https://github.com/flightaware/Pgtcl/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cc01148205fbf130f1a2930fdee00ec1
URL:		https://flightaware.github.io/Pgtcl/
BuildRequires:	postgresql-devel
BuildRequires:	tcl-devel >= 8
Provides:	tcl(Pgtcl)
Obsoletes:	postgresql-tcl < 3.0.0
Obsoletes:	tcl-libpgtcl < 3.0.0
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
Obsoletes:	postgresql-tcl-devel < 3.0.0
Obsoletes:	postgresql-tcl-static < 3.0.0
Obsoletes:	tcl-libpgtcl-devel < 3.0.0

%description devel
C header file for pgtcl-ng interface.

%description devel -l pl.UTF-8
Plik nagłówkowy C dla interfejsu pgtcl-ng.

%prep
%setup -q -n Pgtcl-%{version}

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE ChangeLog* README*
%dir %{_libdir}/pgtcl*.*
%attr(755,root,root) %{_libdir}/pgtcl*.*/libpgtcl*.so
%{_libdir}/pgtcl*.*/pkgIndex.tcl
%{_libdir}/pgtcl*.*/postgres-helpers.tcl
%{_mandir}/mann/PgGetConnectionId.n*
%{_mandir}/mann/pg_*.n*

%files devel
%defattr(644,root,root,755)
%{_includedir}/pgtclId.h
