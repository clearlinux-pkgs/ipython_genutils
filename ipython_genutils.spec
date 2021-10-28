#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipython_genutils
Version  : 0.2.0
Release  : 40
URL      : http://pypi.debian.net/ipython_genutils/ipython_genutils-0.2.0.tar.gz
Source0  : http://pypi.debian.net/ipython_genutils/ipython_genutils-0.2.0.tar.gz
Summary  : Vestigial utilities from IPython
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: ipython_genutils-license = %{version}-%{release}
Requires: ipython_genutils-python = %{version}-%{release}
Requires: ipython_genutils-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# IPython vestigial utilities
This package shouldn't exist.
It contains some common utilities shared by Jupyter and IPython projects during The Big Split™.
As soon as possible, those packages will remove their dependency on this,
and this repo will go away.

%package license
Summary: license components for the ipython_genutils package.
Group: Default

%description license
license components for the ipython_genutils package.


%package python
Summary: python components for the ipython_genutils package.
Group: Default
Requires: ipython_genutils-python3 = %{version}-%{release}

%description python
python components for the ipython_genutils package.


%package python3
Summary: python3 components for the ipython_genutils package.
Group: Default
Requires: python3-core
Provides: pypi(ipython_genutils)

%description python3
python3 components for the ipython_genutils package.


%prep
%setup -q -n ipython_genutils-0.2.0
cd %{_builddir}/ipython_genutils-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603393504
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipython_genutils
cp %{_builddir}/ipython_genutils-0.2.0/COPYING.md %{buildroot}/usr/share/package-licenses/ipython_genutils/440cd463188676ce67da9319d16b0306bd95254f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipython_genutils/440cd463188676ce67da9319d16b0306bd95254f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
