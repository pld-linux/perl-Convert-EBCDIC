%include	/usr/lib/rpm/macros.perl
Summary:	Convert-EBCDIC perl module
Summary(pl):	Modu³ perla Convert-EBCDIC
Name:		perl-Convert-EBCDIC
Version:	0.06
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-EBCDIC-%{version}.tar.gz
Patch0:		perl-Convert-EBCDIC-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-EBCDIC module provides two functions ascii2ebcdic and
ebcdic2ascii for converting a string from/to ASCII to/from EBCDIC.

%description -l pl
Modu³ Convert-EBCDIC udostêpnia dwie funkcje, ascii2ebcdic i
ebcdic2ascii, do konwertowania ³añcuchów ASCII do EBCDIC i EBCDIC do
ASCII.

%prep
%setup -q -n Convert-EBCDIC-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Convert/EBCDIC
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO}.gz tools

%{perl_sitelib}/Convert/EBCDIC.pm
%{perl_sitearch}/auto/Convert/EBCDIC

%{_mandir}/man3/*
