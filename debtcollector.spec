#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : debtcollector
Version  : 1.4.0
Release  : 19
URL      : http://tarballs.openstack.org/debtcollector/debtcollector-1.4.0.tar.gz
Source0  : http://tarballs.openstack.org/debtcollector/debtcollector-1.4.0.tar.gz
Summary  : A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner.
Group    : Development/Tools
License  : Apache-2.0
Requires: debtcollector-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pyflakes-python
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : wrapt-python

%description
Debtcollector
=============
.. image:: https://img.shields.io/pypi/v/debtcollector.svg
:target: https://pypi.python.org/pypi/debtcollector/
:alt: Latest Version

%package python
Summary: python components for the debtcollector package.
Group: Default
Requires: six-python
Requires: wrapt-python

%description python
python components for the debtcollector package.


%prep
%setup -q -n debtcollector-1.4.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
