Name:       centos-release-scl
Epoch:      10
Version:    6
Release:    7%{?dist}
Summary:    Software collections from the CentOS SCLo SIG

License:    GPLv2
URL:        http://wiki.centos.org/SpecialInterestGroup/SCLo
Source0:    CentOS-SCLo.repo
Source1:    RPM-GPG-KEY-CentOS-SIG-SCLo
Source2:    GPL

BuildArch: noarch

%description
yum Configs and basic docs for Software Collections as delivered via the CentOS SCLo SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl.repo
sed -i -e "s/SCLGROUP/sclo/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-SCLo-scl.repo
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

# use a docdir
mkdir -p -m 755 %{buildroot}/%{_docdir}/centos-release-scl
install -m 644 %{SOURCE2} %{buildroot}/%{_docdir}/centos-release-scl

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg
%{_docdir}/centos-release-scl/*

%changelog
* Mon Jan 18 2016 Honza Horak <hhorak@redhat.com> - 10:6-7
- Remove centos-release* dependencies for RHEL variant

* Fri Oct 02 2015 Thomas Oulevey <thomas.oulevey@cern.ch>
- Initial version.
