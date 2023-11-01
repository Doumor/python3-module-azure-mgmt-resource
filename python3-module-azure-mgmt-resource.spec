%define pypi_name azure-mgmt-resource

%def_without check

Name:    python3-module-%pypi_name
Version: 23.0.1
Release: alt1

Summary: Microsoft Azure Resource Management Client Library for Python
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/azure-mgmt-resource/

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-azure-devtools
BuildRequires: python3-module-azure-mgmt-keyvault
BuildRequires: python3-module-azure-mgmt-resource
BuildRequires: python3-module-azure-sdk-tools
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-dotenv
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/azure/
%python3_sitelibdir/azure_mgmt_resource-%version.dist-info/


%changelog
* Wed Oct 24 2023 Danilkin Danila <danild@altlinux.org> 23.0.1-alt1
- Initial build for Sisyphus
