#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Metaphone
Summary:	Text::Metaphone - a modern soundex, phonetic encoding of words
Summary(pl):	Text::Metaphone - wspó³czesny soundex, fonetyczne kodowanie s³ów
Name:		perl-Text-Metaphone
Version:	1.96
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b918985b2364b8d3a5bd0b0ba714ebd0
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metaphone() is a function whereby a string/word is broken down into a
rough approximation of its English phonetic pronunciation. Very
similar in concept and purpose to soundex, but much more comprehensive
in its approach.

%description -l pl
Mataphone() jest funkcj±, w której ³añcuch lub s³owo jest ³amane na
zgrubne przybli¿enie jego angielskiej wymowy. Modu³ jest bardzo
podobny w za³o¿eniach i celu do soundeksa, ale jest du¿o rozleglejszym
podej¶ciem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Text/Metaphone.pm
%dir %{perl_vendorarch}/auto/Text/Metaphone
%{perl_vendorarch}/auto/Text/Metaphone/Metaphone.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Metaphone/Metaphone.so
%{_mandir}/man3/*
