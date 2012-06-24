%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	EBCDIC
Summary:	Convert-EBCDIC perl module
Summary(pl):	Modu� perla Convert-EBCDIC
Name:		perl-Convert-EBCDIC
Version:	0.06
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-EBCDIC module provides two functions ascii2ebcdic and
ebcdic2ascii for converting a string from/to ASCII to/from EBCDIC.

%description -l pl
Modu� Convert-EBCDIC udost�pnia dwie funkcje, ascii2ebcdic i
ebcdic2ascii, do konwertowania �a�cuch�w ASCII do EBCDIC i EBCDIC do
ASCII.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tools
%{perl_sitelib}/Convert/EBCDIC.pm
%{_mandir}/man3/*
