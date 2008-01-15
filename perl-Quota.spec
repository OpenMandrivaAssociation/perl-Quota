%define real_name Quota

Summary:	Quota module for perl 
Name:		perl-%{real_name}
Version:	1.6.1
Release:	%mkrel 2
License:	BSD-like
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOMZO/%{real_name}-%{version}.tar.bz2
Requires:	quota
BuildRequires:	perl-devel
BuildRequires:	quota
#BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Quota module provides access to file system quotas. The quotactl
system call or ioctl is used to query or set quotas on the local host,
or queries are submitted via RPC to a remote host. Mount tables can be
parsed with getmntent and paths can be translated to device files (or
whatever the actual quotactl implementations needs as argument) of the
according file system.


%prep
%setup -q -n %{real_name}-%{version} 

# fix perl path
find -type f | xargs perl -pi -e "s|/usr/drwho/local/bin/perl|%{_bindir}/perl|g"
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
#make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES INSTALL README contrib
%dir %{perl_vendorarch}/auto/Quota
%{perl_vendorarch}/auto/Quota/*
%{perl_vendorarch}/Quota.pm
%{_mandir}/*/*

