#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

Summary:	A C++ interface for atk library
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki atk
Name:		atkmm
Version:	2.24.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/atkmm/2.24/%{name}-%{version}.tar.xz
# Source0-md5:	279f32c23b74e5d25bce2b941294cdc8
URL:		http://www.gtkmm.org/
BuildRequires:	atk-devel >= 1:2.18.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	glibmm-devel >= 2.46.1
BuildRequires:	libtool >= 2:2.0
BuildRequires:	mm-common >= 0.9.8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glibmm >= 2.46.1
Provides:	gtkmm-atk
Obsoletes:	gtkmm-atk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C++ interface for atk library.

%description -l pl.UTF-8
Interfejs C++ dla biblioteki atk.

%package devel
Summary:	Header files for atkmm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki atkmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	atk-devel >= 1:2.18.0
Requires:	glibmm-devel >= 2.46.1
Provides:	gtkmm-atk-devel
Obsoletes:	gtkmm-atk-devel

%description devel
Header files for atkmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki atkmm.

%package apidocs
Summary:	atkmm API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki atkmm
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for atkmm library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki atkmm.

%package static
Summary:	atkmm static library
Summary(pl.UTF-8):	Biblioteka statyczna atkmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	gtkmm-atk-static
Obsoletes:	gtkmm-atk-static

%description static
Static atkmm library.

%description static -l pl.UTF-8
Statyczna biblioteka atkmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdocdir=%{_gtkdocdir}/atkmm-1.6 \
	devhelpdir=%{_gtkdocdir}/atkmm-1.6

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libatkmm-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatkmm-1.6.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm-1.6.so
%{_libdir}/atkmm-1.6
%{_includedir}/atkmm-1.6
%{_pkgconfigdir}/atkmm-1.6.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/atkmm-1.6

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libatkmm-1.6.a
%endif
