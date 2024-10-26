#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeappsver	23.08.5
# packages version, not cmake config version (which is 5.24.5)
%define		ka_ver		%{version}
%define		kf_ver		5.105.0
%define		qt_ver		5.15.2
%define		kaname		pimcommon
Summary:	Common PIM libraries
Summary(pl.UTF-8):	Wspólne biblioteki PIM
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{version}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1fc440ae9f505f70392ac3c8749b134a
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Designer-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5UiTools-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5Xml-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt5-devel >= 5.1
BuildRequires:	ka5-akonadi-contacts-devel >= %{ka_ver}
BuildRequires:	ka5-akonadi-devel >= %{ka_ver}
BuildRequires:	ka5-akonadi-search-devel >= %{ka_ver}
BuildRequires:	ka5-kimap-devel >= %{ka_ver}
BuildRequires:	ka5-kldap-devel >= %{ka_ver}
BuildRequires:	ka5-kpimtextedit-devel >= %{ka_ver}
BuildRequires:	ka5-libkdepim-devel >= %{ka_ver}
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-karchive-devel >= %{kf_ver}
BuildRequires:	kf5-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf5-kcodecs-devel >= %{kf_ver}
BuildRequires:	kf5-kcompletion-devel >= %{kf_ver}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kcontacts-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kio-devel >= %{kf_ver}
BuildRequires:	kf5-kitemmodels-devel >= %{kf_ver}
BuildRequires:	kf5-kjobwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-knewstuff-devel >= %{kf_ver}
BuildRequires:	kf5-ktextaddons-devel
BuildRequires:	kf5-kservice-devel >= %{kf_ver}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kf5-purpose-devel >= %{kf_ver}
BuildRequires:	libxslt-progs
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5DBus >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Network >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	ka5-akonadi-contacts >= %{ka_ver}
Requires:	ka5-akonadi >= %{ka_ver}
Requires:	ka5-akonadi-search >= %{ka_ver}
Requires:	ka5-kimap >= %{ka_ver}
Requires:	ka5-kldap >= %{ka_ver}
Requires:	ka5-kpimtextedit >= %{ka_ver}
Requires:	ka5-libkdepim >= %{ka_ver}
Requires:	kf5-kcmutils >= %{kf_ver}
Requires:	kf5-kcodecs >= %{kf_ver}
Requires:	kf5-kcompletion >= %{kf_ver}
Requires:	kf5-kconfig >= %{kf_ver}
Requires:	kf5-kcontacts >= %{kf_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
Requires:	kf5-ki18n-devel >= %{kf_ver}
Requires:	kf5-kio >= %{kf_ver}
Requires:	kf5-kitemmodels >= %{kf_ver}
Requires:	kf5-kjobwidgets >= %{kf_ver}
Requires:	kf5-knewstuff >= %{kf_ver}
Requires:	kf5-purpose >= %{kf_ver}
Requires:	kf5-kwidgetsaddons >= %{kf_ver}
Requires:	kf5-kxmlgui >= %{kf_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common PIM libraries.

%description -l pl.UTF-8
Wspólne biblioteki PIM.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5DBus-devel >= %{qt_ver}
Requires:	Qt5Gui-devel >= %{qt_ver}
Requires:	Qt5Widgets-devel >= %{qt_ver}
Requires:	ka5-akonadi-contacts-devel >= %{ka_ver}
Requires:	ka5-akonadi-devel >= %{ka_ver}
Requires:	ka5-kimap-devel >= %{ka_ver}
Requires:	ka5-kpimtextedit-devel >= %{ka_ver}
Requires:	ka5-libkdepim-devel >= %{ka_ver}
Requires:	kf5-kconfig-devel >= %{kf_ver}
Requires:	kf5-kcontacts-devel >= %{kf_ver}
Requires:	kf5-kio-devel >= %{kf_ver}
Requires:	kf5-ktextaddons-devel

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang libpimcommon

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libpimcommon.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKPim5PimCommon.so.*.*.*
%ghost %{_libdir}/libKPim5PimCommon.so.5
%attr(755,root,root) %{_libdir}/libKPim5PimCommonAkonadi.so.*.*.*
%ghost %{_libdir}/libKPim5PimCommonAkonadi.so.5
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/pimcommon5akonadiwidgets.so
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/pimcommon5widgets.so
%{_datadir}/qlogging-categories5/pimcommon.categories
%{_datadir}/qlogging-categories5/pimcommon.renamecategories

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKPim5PimCommon.so
%{_libdir}/libKPim5PimCommonAkonadi.so
%{_includedir}/KPim5/PimCommon
%{_includedir}/KPim5/PimCommonAkonadi
%{_libdir}/cmake/KPim5PimCommon
%{_libdir}/cmake/KPim5PimCommonAkonadi
%{_libdir}/qt5/mkspecs/modules/qt_PimCommon.pri
%{_libdir}/qt5/mkspecs/modules/qt_PimCommonAkonadi.pri
