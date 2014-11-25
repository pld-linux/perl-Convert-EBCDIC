#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Convert
%define		pnam	EBCDIC
%include	/usr/lib/rpm/macros.perl
Summary:	Convert::EBCDIC - Perl module for string conversion between EBCDIC and ASCII
Summary(pl.UTF-8):	Convert::EBCDIC - moduł Perla do konwersji tekstów pomiędzy EBCDIC i ASCII
Name:		perl-Convert-EBCDIC
Version:	0.06
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	931cffde61b7040b2cd42002387d320d
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Convert-EBCDIC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::EBCDIC module provides two functions ascii2ebcdic and
ebcdic2ascii for converting a string from/to ASCII to/from EBCDIC.

%description -l pl.UTF-8
Moduł Convert::EBCDIC udostępnia dwie funkcje, ascii2ebcdic i
ebcdic2ascii, do konwertowania łańcuchów tekstowych z ASCII do EBCDIC
i z EBCDIC do ASCII.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO tools
%{perl_vendorlib}/Convert/EBCDIC.pm
%{_mandir}/man3/*
