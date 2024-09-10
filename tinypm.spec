%define version %{getenv:TPM_VERSION}
%define release %{getenv:TPM_RELEASE}

Name:         tiny_process_manager

Version:	%{version}
Release:	%{release}

Summary:        Tiny http process manager
BuildArch:      noarch

License:       GPL
Source0:       tiny_process_manager-%{version}-%{release}.tar.gz

Requires:      python3
Requires(pre): /usr/sbin/useradd, /usr/bin/getent

%description
Tiny Process manager build

%prep
%setup -q -n tiny_process_manager-%{version}-%{release} -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp tiny_process_manager $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/systemd/system
cp tiny_process_manager.service $RPM_BUILD_ROOT/%{_libdir}/systemd/system

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/tiny_process_manager
%{_libdir}/systemd/system/tiny_process_manager.service

%pre
groupadd -f -r -g 889 HGCAL_pro
getent user HGCAL_pro > /dev/null 2>&1 || useradd -c HGCAL_Production_Servics -g HGCAL_pro -r HGCAL_pro
exit 0

