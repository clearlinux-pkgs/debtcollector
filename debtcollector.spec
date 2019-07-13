#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : debtcollector
Version  : 1.21.0
Release  : 39
URL      : http://tarballs.openstack.org/debtcollector/debtcollector-1.21.0.tar.gz
Source0  : http://tarballs.openstack.org/debtcollector/debtcollector-1.21.0.tar.gz
Source99 : http://tarballs.openstack.org/debtcollector/debtcollector-1.21.0.tar.gz.asc
Summary  : A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner.
Group    : Development/Tools
License  : Apache-2.0
Requires: debtcollector-license = %{version}-%{release}
Requires: debtcollector-python = %{version}-%{release}
Requires: debtcollector-python3 = %{version}-%{release}
Requires: funcsigs
Requires: pbr
Requires: six
Requires: wrapt
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/debtcollector.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

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

%description python3
python3 components for the debtcollector package.


%prep
%setup -q -n debtcollector-1.21.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557084130
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/debtcollector
cp LICENSE %{buildroot}/usr/share/package-licenses/debtcollector/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/debtcollector/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
