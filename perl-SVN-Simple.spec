#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SVN
%define	pnam	Simple
Summary:	SVN::Simple - Simple interface for delta editors
Name:		perl-SVN-Simple
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	559c41fa75797e2f33af1cead21897cf
URL:		http://www.geocities.com/easydatabase/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-subversion
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVN::Simple::Edit, a simple interface for driving svn delta editors
and SVN::Simple::Editor, a simple interface for writing a delta
editor.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc CHANGE*
%{perl_vendorlib}/SVN/Simple
%{_mandir}/man3/*
