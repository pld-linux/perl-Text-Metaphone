%include	/usr/lib/rpm/macros.perl
Summary:	Text-Metaphone perl module
Summary(pl):	Modu³ perla Text-Metaphone
Name:		perl-Text-Metaphone
Version:	1.96
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Metaphone-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Metaphone perl module.

%description -l pl
Modu³ perla Text-Metaphone.

%prep
%setup -q -n Text-Metaphone-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Text/Metaphone.pm
%dir %{perl_sitearch}/auto/Text/Metaphone
%{perl_sitearch}/auto/Text/Metaphone/Metaphone.bs
%attr(755,root,root) %{perl_sitearch}/auto/Text/Metaphone/Metaphone.so
%{_mandir}/man3/*
