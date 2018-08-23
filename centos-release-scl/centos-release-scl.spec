Name:       centos-release-scl
Epoch:      10
Version:    6
Release:    9%{?dist}
Summary:    Software collections from the CentOS SCLo SIG

License:    GPLv2
URL:        http://wiki.centos.org/SpecialInterestGroup/SCLo
Source0:    CentOS-SCLo.repo
Source1:    RPM-GPG-KEY-CentOS-SIG-SCLo
Source2:    GPL

Source6:    CentOS-6-SCLo-Vault.repo
Source7:    CentOS-7-SCLo-Vault.repo

BuildArch:  noarch
Requires:   centos-release

%description
yum Configs and basic docs for Software Collections as delivered via the CentOS SCLo SIG.

%prep

%build

%install
function install_repo
{
    local repo="$1"
    local repo_renamed="${2:-$repo}"

    install -D -m 644 "$repo" %{buildroot}%{_sysconfdir}/yum.repos.d/"$repo_renamed"
    # variable $releasever in RHEL might expand into something like 7Server, which is not what we want here
    sed --in-place \
        --expression "s/SCLGROUP/sclo/g" \
        --expression "s/\$releasever/%{?rhel}%{!?rhel:\$releasever}/g" \
        %{buildroot}%{_sysconfdir}/yum.repos.d/"$repo_renamed"
}

install_repo %{SOURCE0} CentOS-SCLo-scl.repo

install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%if %{?rhel}%{!?rhel:0} == 6
install_repo %{SOURCE6} CentOS-SCLo-scl-Vault.repo
%endif
%if %{?rhel}%{!?rhel:0} == 7
install_repo %{SOURCE7} CentOS-SCLo-scl-Vault.repo
%endif

# use a docdir
mkdir -p -m 755 %{buildroot}/%{_docdir}/centos-release-scl
install -m 644 %{SOURCE2} %{buildroot}/%{_docdir}/centos-release-scl

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg
%{_docdir}/centos-release-scl/*

%changelog
* Thu Aug 23 2018 Jan Staněk <jstanek@redhat.com> - 10:6-9
- Add repo definitions for vault

* Mon Jan 18 2016 Honza Horak <hhorak@redhat.com> - 10:6-8
- Use explicit releasever in repo file

* Mon Jan 18 2016 Honza Horak <hhorak@redhat.com> - 10:6-7
- Remove centos-release* dependencies for RHEL variant

* Fri Oct 02 2015 Thomas Oulevey <thomas.oulevey@cern.ch>
- Initial version.
