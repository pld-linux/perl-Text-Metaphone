%include	/usr/lib/rpm/macros.perl
Summary:	Text-Metaphone perl module
Summary(pl):	Modu³ perla Text-Metaphone
Name:		perl-Text-Metaphone
Version:	1.96
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Metaphone-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Text-Metaphone perl module. 

%description -l pl
Modu³ perla Text-Metaphone.

%prep
%setup -q -n Text-Metaphone-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Text/Metaphone/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/Metaphone
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitearch}/Text/Metaphone.pm

%dir %{perl_sitearch}/auto/Text/Metaphone
%{perl_sitearch}/auto/Text/Metaphone/.packlist
%{perl_sitearch}/auto/Text/Metaphone/Metaphone.bs
%attr(755,root,root) %{perl_sitearch}/auto/Text/Metaphone/Metaphone.so

%{_mandir}/man3/*
