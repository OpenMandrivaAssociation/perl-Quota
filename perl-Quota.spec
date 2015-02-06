%define upstream_name    Quota
%define upstream_version 1.7.1
Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:	Quota module for perl 

License:	BSD-like
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOMZO/Quota-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	tirpc-devel
BuildRequires:	quota


Requires:	quota

%description
The Quota module provides access to file system quotas. The quotactl
system call or ioctl is used to query or set quotas on the local host,
or queries are submitted via RPC to a remote host. Mount tables can be
parsed with getmntent and paths can be translated to device files (or
whatever the actual quotactl implementations needs as argument) of the
according file system.


%prep
%setup -q -n %{upstream_name}-%{version}

# fix perl path
find -type f | xargs perl -pi -e "s|/usr/drwho/local/bin/perl|%{_bindir}/perl|g"
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install

%makeinstall_std

%clean 

%files
%doc CHANGES INSTALL README contrib
%{perl_vendorarch}/auto/Quota
%{perl_vendorarch}/Quota.pm
%{_mandir}/*/*


