#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipython_genutils
Version  : 0.2.0
Release  : 8
URL      : http://pypi.debian.net/ipython_genutils/ipython_genutils-0.2.0.tar.gz
Source0  : http://pypi.debian.net/ipython_genutils/ipython_genutils-0.2.0.tar.gz
Summary  : Vestigial utilities from IPython
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: ipython_genutils-legacypython
Requires: ipython_genutils-python3
Requires: ipython_genutils-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# IPython vestigial utilities
This package shouldn't exist.
It contains some common utilities shared by Jupyter and IPython projects during The Big Splitâ¢.
As soon as possible, those packages will remove their dependency on this,
and this repo will go away.

%package legacypython
Summary: legacypython components for the ipython_genutils package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the ipython_genutils package.


%package python
Summary: python components for the ipython_genutils package.
Group: Default
Requires: ipython_genutils-legacypython
Requires: ipython_genutils-python3

%description python
python components for the ipython_genutils package.


%package python3
Summary: python3 components for the ipython_genutils package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ipython_genutils package.


%prep
%setup -q -n ipython_genutils-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507155366
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507155366
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
