#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Applying STAT information from a Stylespace to a variable font
Summary(pl.UTF-8):	Nanoszenie informacji STAT ze Stylespace na zmienny font
Name:		python3-statmake
Version:	0.4.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/statmake/
Source0:	https://files.pythonhosted.org/packages/source/s/statmake/statmake-%{version}.tar.gz
# Source0-md5:	3e58ac9c5ed18a3261593a41725ca203
URL:		https://pypi.org/project/statmake/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-attrs >= 18.2
BuildRequires:	python3-cattrs >= 1.1
BuildRequires:	python3-cattrs < 2.0
# fonttools[ufo]
BuildRequires:	python3-fonttools >= 4.11
BuildRequires:	python3-fonttools < 5.0
BuildRequires:	python3-fs >= 2.2.0
%if "%{py3_ver}" == "3.7"
BuildRequires:	python3-importlib_metadata >= 1.6.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
statmake takes a user-written Stylespace that defines OpenType STAT
information for an entire font family and then (potentially subsets
and) applies it to a specific variable font. This spares users from
having to deal with raw TTX dumps and juggling with nameIDs.

%description -l pl.UTF-8
statmake przyjmuje napisane przez użytkownika Stylespace, definiujące
informacje OpenType STAT dla całej rodziny fontów, a następnie nanosi
je (lub podzbiór) na określony zmienny font. Oszczędza to użytkownikom
obsługi surowych zrzutów TTX i żonglowania polami nameID.

%prep
%setup -q -n statmake-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/statmake
%{py3_sitescriptdir}/statmake
%{py3_sitescriptdir}/statmake-%{version}-py*.egg-info
