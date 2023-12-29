Name:           calc_files
Version:        1.0
Release:        1%{?dist}
Summary:        Script to calculate the number of files in /etc

License:        MIT
URL:            https://github.com/sychaleksandr/SystemAdministration_Lab_Sych

Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  /usr/bin/tar

%description
This package provides a script to calculate the number of files in /etc (excluding directories and links).

%prep
%autosetup

%build
# No build steps required

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{SOURCE0} %{buildroot}/usr/bin/calc_files.sh

%files
/usr/bin/calc_files.sh

%changelog
* Mon Dec 28 2023 Oleksandr Sych <sychaleksandr04@gmail.com> - 1.0-1
- Initial package release