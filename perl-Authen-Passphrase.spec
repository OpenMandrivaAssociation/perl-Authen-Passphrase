%define upstream_name    Authen-Passphrase
%define upstream_version 0.007

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Hashed passwords/passphrases as objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Authen/%{upstream_name}-%{upstream_version}.tar.lzma

BuildRequires:	perl-devel
BuildRequires:	perl(Authen::DecHpwd)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Crypt::Blowfish)
BuildRequires:	perl(Crypt::DES)
BuildRequires:	perl(Crypt::Eksblowfish::Bcrypt)
BuildRequires:	perl(Crypt::MySQL)
BuildRequires:	perl(Crypt::PasswdMD5)
BuildRequires:	perl(Crypt::Rijndael)
BuildRequires:	perl(Crypt::UnixCrypt_XS)
BuildRequires:	perl(Data::Entropy::Algorithms)
BuildRequires:	perl(Digest)
BuildRequires:	perl(Digest::MD4)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Params::Classify)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(base)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This is the base class for a system of objects that encapsulate
passphrases. An object of this type is a passphrase recogniser: its job is
to recognise whether an offered passphrase is the right one. For security,
such passphrase recognisers usually do not themselves know the passphrase
they are looking for; they can merely recognise it when they see it. There
are many schemes in use to achieve this effect, and the intent of this
class is to provide a consistent interface to them all, hiding the details.

The CPAN package Authen::Passphrase contains implementations of several
specific passphrase schemes in addition to the base class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.7.0-3mdv2011.0
+ Revision: 653551
- rebuild for updated spec-helper

* Sun Aug 29 2010 Shlomi Fish <shlomif@mandriva.org> 0.7.0-2mdv2011.0
+ Revision: 574168
- Add Crypt-Rijndael to the build requires
- import perl-Authen-Passphrase

