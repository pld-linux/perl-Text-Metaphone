%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Metaphone
Summary:	Text::Metaphone perl module
Summary(pl):	Modu� perla Text::Metaphone
Name:		perl-Text-Metaphone
Version:	1.96
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Metaphone perl module.

%description -l pl
Modu� perla Text::Metaphone.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
