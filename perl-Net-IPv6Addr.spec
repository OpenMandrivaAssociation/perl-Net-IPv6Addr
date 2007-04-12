%define real_name Net-IPv6Addr

Summary:	Net::IPv6Addr - check validity of IPv6 addresses
Name:		perl-%{real_name}
Version:	0.2
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TM/TMONROE/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Net-IPv4Addr
BuildRequires:	perl-Math-Base85
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Net::IPv6Addr checks strings for valid IPv6 addresses, as
specified in RFC1884.  You throw possible addresses at it, it
either accepts them or throws an exception.

If Math::Base85 is installed, then this module is able to process
addresses formatted in the style referenced by RFC1924.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Net/IPv6Addr.pm
%{_mandir}/*/*

