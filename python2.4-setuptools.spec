%define module	setuptools
%define name	python2.4-%{module}
%define version 0.6c6
%define release %mkrel 1
 
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:    Python Distutils Enhancements
License:    Zope Public License (ZPL)
Group:      Development/Python
Url:        http://peak.telecommunity.com/DevCenter/setuptools
Source0:    http://cheeseshop.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.bz2
BuildRequires: python2.4-devel
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Extensions to the python-distutils for large or complex distributions.

%prep
%setup -q -n %{module}-%{version}

%build
python2.4 setup.py build
perl -pi -e 's|^#!python|#!/usr/bin/python2.4|' \
    easy_install.py \
    setuptools/command/easy_install.py

%install
rm -rf %{buildroot}
python2.4 setup.py install --prefix=%{buildroot}/%_prefix --old-and-unmanageable

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc setuptools.txt pkg_resources.txt api_tests.txt EasyInstall.txt  
%_bindir/*
%_libdir/python2.4/*
