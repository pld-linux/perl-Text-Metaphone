#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Metaphone
Summary:	Text::Metaphone - a modern soundex, phonetic encoding of words
Summary(pl.UTF-8):	Text::Metaphone - współczesny soundex, fonetyczne kodowanie słów
Name:		perl-Text-Metaphone
Version:	20081017
Release:	7
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3c1233c6a6363d5b611f08add1f1120
URL:		http://search.cpan.org/dist/Text-Metaphone/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metaphone() is a function whereby a string/word is broken down into a
rough approximation of its English phonetic pronunciation. Very
similar in concept and purpose to soundex, but much more comprehensive
in its approach.

%description -l pl.UTF-8
Mataphone() jest funkcją, w której łańcuch lub słowo jest łamane na
zgrubne przybliżenie jego angielskiej wymowy. Moduł jest bardzo
podobny w założeniach i celu do soundeksa, ale jest dużo rozleglejszym
podejściem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Metaphone/Metaphone.so
%{_mandir}/man3/*
