#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	SVN
%define		pnam	Simple
Summary:	SVN::Simple - Simple interface for delta editors
Summary(pl.UTF-8):	SVN::Simple - prosty interfejs do edytorów różnic
Name:		perl-SVN-Simple
Version:	0.28
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.cpan.org/modules/by-authors/id/C/CL/CLKAO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4de2374434df79dace03075c69e7b93f
URL:		http://search.cpan.org/dist/SVN-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-subversion
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVN::Simple::Edit, a simple interface for driving svn delta editors
and SVN::Simple::Editor, a simple interface for writing a delta
editor.

%description -l pl.UTF-8
SVN::Simple::Edit to prosty interfejs do sterowania edytorami różnic
(delt) svn, a SVN::Simple::Editor to prosty interfejs do pisania
edytora różnic.

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
