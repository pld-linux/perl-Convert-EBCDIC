#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	EBCDIC
Summary:	Convert::EBCDIC - Perl module for string conversion between EBCDIC and ASCII
Summary(pl):	Convert::EBCDIC - modu³ Perla do konwersji tekstów pomiêdzy EBCDIC i ASCII
Name:		perl-Convert-EBCDIC
Version:	0.06
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	931cffde61b7040b2cd42002387d320d
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::EBCDIC module provides two functions ascii2ebcdic and
ebcdic2ascii for converting a string from/to ASCII to/from EBCDIC.

%description -l pl
Modu³ Convert::EBCDIC udostêpnia dwie funkcje, ascii2ebcdic i
ebcdic2ascii, do konwertowania ³añcuchów tekstowych z ASCII do EBCDIC
i z EBCDIC do ASCII.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

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
