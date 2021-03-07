#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

%define		atk_ver		1:2.18
%define		glibmm_ver	2.68.0
Summary:	A C++ interface for atk library
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki atk
Name:		atkmm2.36
Version:	2.36.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/atkmm/2.36/atkmm-%{version}.tar.xz
# Source0-md5:	b3c8253a56850bf3bbfd963482480996
URL:		https://www.gtkmm.org/
BuildRequires:	atk-devel >= %{atk_ver}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	doxygen >= 1:1.8.9
BuildRequires:	glibmm2.68-devel >= %{glibmm_ver}
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtool >= 2:2.0
BuildRequires:	mm-common >= 0.9.12
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	atk >= %{atk_ver}
Requires:	glibmm2.68 >= %{glibmm_ver}
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
Requires:	atk-devel >= %{atk_ver}
Requires:	glibmm2.68-devel >= %{glibmm_ver}
Requires:	libstdc++-devel >= 6:7

%description devel
Header files for atkmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki atkmm.

%package apidocs
Summary:	atkmm API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki atkmm
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
API documentation for atkmm library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki atkmm.

%package static
Summary:	atkmm static library
Summary(pl.UTF-8):	Biblioteka statyczna atkmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static atkmm library.

%description static -l pl.UTF-8
Statyczna biblioteka atkmm.

%prep
%setup -q -n atkmm-%{version}

%build
mm-common-prepare --copy --force
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-maintainer-mode \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdocdir=%{_gtkdocdir}/atkmm-2.36 \
	devhelpdir=%{_gtkdocdir}/atkmm-2.36

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libatkmm-2.36.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatkmm-2.36.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatkmm-2.36.so
%{_libdir}/atkmm-2.36
%{_includedir}/atkmm-2.36
%{_pkgconfigdir}/atkmm-2.36.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/atkmm-2.36

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libatkmm-2.36.a
%endif
