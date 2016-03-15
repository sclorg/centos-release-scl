# Package centos-release-scl for RHEL users

This package provides yum Configs and basic docs for Software Collections
packages as delivered via the CentOS SCLo SIG.

## How to install SCLo packages on CentOS systems

On CentOS, there are packages `centos-release-scl` and `centos-release-scl-rh`
available in `centos-extra` repository, so for installing SCLo repos
on CentOS, run:

```
sudo yum install centos-release-scl
```

For installing SCLo repository with only collections that are availabla in RHSCL, run:
```
sudo yum install centos-release-scl-rh
```

## How to install SCLo packages on RHEL systems

On RHEL, there is no `centos-release-scl-rh` package available and users are expected to enable RHSCL repository, like this:

```
sudo yum-config-manager --enable rhel-server-rhscl-7-rpms
```

For rare cases where there is no RHSCL channel available, you can enable CentOS SIG by installing this package (example for RHEL-7):
```
sudo yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/rhscl/centos-release-scl-rh/repo/epel-7/rhscl-centos-release-scl-rh-epel-7.repo
sudo yum install centos-release-scl-rh
```

For enabling Software Collections that are not in RHSCL, but are build by SCLo SIG group only in CentOS, install this package (example for RHEL-7):

```
sudo yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/rhscl/centos-release-scl/repo/epel-7/rhscl-centos-release-scl-epel-7.repo
sudo yum install centos-release-scl
```

Again, installing these `centos-release-scl` and `centos-release-scl-rh` packages from Copr repository above is only expected to be done on RHEL systems.

**Important**: Please, mind, that packages build by SCLo SIG are not supported and are not part of the supported Red Hat portfolio. For installing supported Software Collections packages, install packages from official RHSCL repository only.
