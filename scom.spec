Summary:	Sunshine Commander
Name:		scom
Version:	0.3.4
Release:	1
License:	GPL
Group:		Shells
Source0:	http://www.poulsen.org/sc/snapshots/sc-%{version}.tar.gz
Patch0:		sc-automake.patch
URL:		http://www.poulsen.org/sc/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sunshine Commander is an attempt to make a consolebased,
crossplatform, filemanager, which allows the user to do common
filecentred tasks within a single program, including full
linux-filesystem support, archivehandling, FTP-handling etc.

%description -l pl
Sunshine Commander to próba stworzenia bazuj±cego na konsoli
zarz±dcy plików ze wsparciem dla archiwów, FTP itd.

%prep
%setup -q -n sc-%{version}
%patch0 -p1

%build
automake -a -c
CFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS} -I/usr/include/ncurses"
CXXFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS} \
	-I/usr/include/ncurses -fno-rtti -fno-exceptions -fno-implicit-templates"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
