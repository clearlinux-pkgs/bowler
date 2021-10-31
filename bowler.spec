#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bowler
Version  : 0.9.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/f4/02/4728875b1fc4382ea71e771c3475a2af6ccaf140663b36c8456ebba4ac5a/bowler-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f4/02/4728875b1fc4382ea71e771c3475a2af6ccaf140663b36c8456ebba4ac5a/bowler-0.9.0.tar.gz
Summary  : Safe code refactoring for modern Python projects
Group    : Development/Tools
License  : MIT
Requires: bowler-bin = %{version}-%{release}
Requires: bowler-license = %{version}-%{release}
Requires: bowler-python = %{version}-%{release}
Requires: bowler-python3 = %{version}-%{release}
Requires: attrs
Requires: click
Requires: fissix
Requires: moreorless
Requires: volatile
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : fissix
BuildRequires : moreorless
BuildRequires : setuptools
BuildRequires : volatile

%description
**Safe code refactoring for modern Python projects.**

%package bin
Summary: bin components for the bowler package.
Group: Binaries
Requires: bowler-license = %{version}-%{release}

%description bin
bin components for the bowler package.


%package license
Summary: license components for the bowler package.
Group: Default

%description license
license components for the bowler package.


%package python
Summary: python components for the bowler package.
Group: Default
Requires: bowler-python3 = %{version}-%{release}

%description python
python components for the bowler package.


%package python3
Summary: python3 components for the bowler package.
Group: Default
Requires: python3-core
Provides: pypi(bowler)
Requires: pypi(attrs)
Requires: pypi(click)
Requires: pypi(fissix)
Requires: pypi(moreorless)
Requires: pypi(volatile)

%description python3
python3 components for the bowler package.


%prep
%setup -q -n bowler-0.9.0
cd %{_builddir}/bowler-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635708437
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bowler
cp %{_builddir}/bowler-0.9.0/LICENSE %{buildroot}/usr/share/package-licenses/bowler/1506731a652bba9abdf804ba3c95651ec5a68bdc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bowler

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bowler/1506731a652bba9abdf804ba3c95651ec5a68bdc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
