#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-GlobalDestruction
Version  : 0.14
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Devel-GlobalDestruction-0.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Devel-GlobalDestruction-0.14.tar.gz
Summary  : "Provides function returning the equivalent of C<${^GLOBAL_PHASE} eq 'DESTRUCT'> for older perls."
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Exporter::Progressive)

%description
NAME
Devel::GlobalDestruction - Provides function returning the equivalent of
"${^GLOBAL_PHASE} eq 'DESTRUCT'" for older perls.

%package dev
Summary: dev components for the perl-Devel-GlobalDestruction package.
Group: Development
Provides: perl-Devel-GlobalDestruction-devel = %{version}-%{release}

%description dev
dev components for the perl-Devel-GlobalDestruction package.


%prep
%setup -q -n Devel-GlobalDestruction-0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Devel/GlobalDestruction.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::GlobalDestruction.3
