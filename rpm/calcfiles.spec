Name:           calcfiles
Version:        1.0
Release:        1%{?dist}
Summary:        Simple script to count files in directory, excluding links and repositories
Requires:       unzip
License:        MIT
URL:            https://github.com/sychaleksandr/SA
Source0:        https://github.com/sychaleksandr/SA/archive/main.zip
BuildArch:      noarch

%description
calc_files.sh -it is a simple script to count files in directory, excluding links and repositories

%prep
%autosetup -n SA-main

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_builddir}/SA-main/calc_files.sh %{buildroot}/usr/bin/calc_files

%files
/usr/bin/calc_files

%changelog
* Wed Dec 29 2023 Sych Oleksandr <sychaleksandr04@gmail.com> - 1.0-1
- First build
