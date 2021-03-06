#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : debtcollector
Version  : 2.2.0
Release  : 48
URL      : http://tarballs.openstack.org/debtcollector/debtcollector-2.2.0.tar.gz
Source0  : http://tarballs.openstack.org/debtcollector/debtcollector-2.2.0.tar.gz
Source1  : http://tarballs.openstack.org/debtcollector/debtcollector-2.2.0.tar.gz.asc
Summary  : A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner.
Group    : Development/Tools
License  : Apache-2.0
Requires: debtcollector-license = %{version}-%{release}
Requires: debtcollector-python = %{version}-%{release}
Requires: debtcollector-python3 = %{version}-%{release}
Requires: pbr
Requires: six
Requires: wrapt
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : six
BuildRequires : wrapt

%description
Team and repository tags
        ========================

%package license
Summary: license components for the debtcollector package.
Group: Default

%description license
license components for the debtcollector package.


%package python
Summary: python components for the debtcollector package.
Group: Default
Requires: debtcollector-python3 = %{version}-%{release}

%description python
python components for the debtcollector package.


%package python3
Summary: python3 components for the debtcollector package.
Group: Default
Requires: python3-core
Provides: pypi(debtcollector)
Requires: pypi(pbr)
Requires: pypi(six)
Requires: pypi(wrapt)

%description python3
python3 components for the debtcollector package.


%prep
%setup -q -n debtcollector-2.2.0
cd %{_builddir}/debtcollector-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595959442
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/debtcollector
cp %{_builddir}/debtcollector-2.2.0/LICENSE %{buildroot}/usr/share/package-licenses/debtcollector/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/debtcollector/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
