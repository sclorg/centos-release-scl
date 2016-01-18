# Package centos-release-scl for RHEL users

This package provides yum Configs and basic docs for Software Collections
as delivered via the CentOS SCLo SIG only (so called sclo namespace at
https://wiki.centos.org/SpecialInterestGroup/SCLo).

On CentOS, there are packages `centos-release-scl` and `centos-release-scl-rh`
available in `centos-extra` repository, so for installing SCLo reposo
on CentOS, run:

```
sudo yum install centos-release-scl
```

On RHEL, there is no `centos-release-scl-rh` package available and users are expected to enable RHSCL repository, like this:

```
sudo yum-config-manager --enable rhel-server-rhscl-7-rpms
```

For enabling Software Collections that are not in RHSCL, but are build by SCLo SIG group in CentOS, install this package by:

```
sudo yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/rhscl/centos-release-scl/repo/epel-6/rhscl-centos-release-scl-epel-6.repo
sudo yum install centos-release-scl
```

OR

```
sudo yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/rhscl/centos-release-scl/repo/epel-7/rhscl-centos-release-scl-epel-7.repo
sudo yum install centos-release-scl
```

Again, installing this `centos-release-scl` package from Copr repository above is only expected to be done on RHEL systems.

*Important*: Please, mind, that packages build by SCLo SIG are not supported and are not part of the supported Red Hat portfolio. For installing supported Software Collections packages, install packages from official RHSCL repository only.
