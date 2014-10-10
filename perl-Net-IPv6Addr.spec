%define real_name Net-IPv6Addr

Summary:	Net::IPv6Addr - check validity of IPv6 addresses
Name:		perl-%{real_name}
Version:	0.2
Release:	7
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TM/TMONROE/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Net::IPv4Addr)
BuildRequires:	perl(Math::Base85)
BuildArch:	noarch

%description
Net::IPv6Addr checks strings for valid IPv6 addresses, as
specified in RFC1884.  You throw possible addresses at it, it
either accepts them or throws an exception.

If Math::Base85 is installed, then this module is able to process
addresses formatted in the style referenced by RFC1924.

%prep
%setup -q -n %{real_name}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/Net/IPv6Addr.pm
%{_mandir}/*/*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2-5mdv2010.0
+ Revision: 430512
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2009.0
+ Revision: 241781
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2-2mdv2008.0
+ Revision: 86703
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdk
- initial Mandriva package

