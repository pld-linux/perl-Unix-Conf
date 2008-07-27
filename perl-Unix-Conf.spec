#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unix
%define		pnam	Conf
Summary:	Unix::Conf - set of modules for accesing and locking config files
Summary(pl.UTF-8):	Unix::Conf - zestaw modułów ułatwiających obsługę plików konfiguracyjnych
Name:		perl-Unix-Conf
Version:	0.2
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0cd54a49aa255256714fb4e0df0d8ba0
URL:		http://www.extremix.net/UnixConf/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of modules for accessing and locking config files. It handles
dotlock and flock lock types.

%description -l pl.UTF-8
Zestaw modułów ułatwiających obsługę plików konfiguracyjnych, w tym
tworzenie blokad. Obsługiwane typy blokad to flock oraz dotfile.

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
%doc Changes README
%{perl_vendorlib}/Unix/Conf.pm
%dir %{perl_vendorlib}/Unix/Conf
%{perl_vendorlib}/Unix/Conf/*.pm
%{_mandir}/man3/*
