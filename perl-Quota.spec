%define upstream_name    Quota
%define upstream_version 1.6.7
Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.6.7
Release:	1

Summary:	Quota module for perl 
License:	BSD-like
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOMZO/Quota-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	quota

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES INSTALL README contrib
%{perl_vendorarch}/auto/Quota
%{perl_vendorarch}/Quota.pm
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.6.6-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.6-1
+ Revision: 684823
- update to new version 1.6.6

* Tue Jan 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.5-1mdv2011.0
+ Revision: 628597
- update to new version 1.6.5

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.6.4-2mdv2011.0
+ Revision: 556117
- rebuild for perl 5.12

* Thu Jan 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.6.4-1mdv2010.1
+ Revision: 491180
- update to 1.6.4

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.6.3-2mdv2010.0
+ Revision: 440617
- rebuild

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.3-1mdv2009.1
+ Revision: 320546
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.6.2-4mdv2009.0
+ Revision: 258279
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.6.2-3mdv2009.0
+ Revision: 246341
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.2-1mdv2008.1
+ Revision: 152910
- update to new version 1.6.2
- update to new version 1.6.2

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.6.1-2mdv2008.1
+ Revision: 152249
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.1-1mdv2008.1
+ Revision: 114492
- update to new version 1.6.1

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.0-1mdv2008.1
+ Revision: 104568
- update to new version 1.6.0

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.2-1mdv2008.1
+ Revision: 97561
- update to new version 1.5.2

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-3mdv2008.0
+ Revision: 25454
- rebuild

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.5.1-2mdv2008.0
+ Revision: 25105
- rebuild


* Thu Apr 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-1mdk
- initial Mandriva package


