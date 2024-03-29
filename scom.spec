Summary:	Sunshine Commander
Summary(pl.UTF-8):	Sunshine Commander
Name:		scom
Version:	0.5.1
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://www.poulsen.org/sc-%{version}.tar.gz
# Source0-md5:	0a71e1272d52e9309281da1652c872b9
Patch0:		sc-automake.patch
Patch1:		sc-am_fix.patch
Patch2:		sc-glibc.patch
URL:		http://sc.poulsen.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sunshine Commander is an attempt to make a consolebased,
crossplatform, filemanager, which allows the user to do common
filecentred tasks within a single program, including full
linux-filesystem support, archivehandling, FTP-handling etc.

%description -l pl.UTF-8
Sunshine Commander to próba stworzenia bazującego na konsoli zarządcy
plików ze wsparciem dla archiwów, FTP itd.

%prep
%setup -q -n sc-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
CXXFLAGS="%{rpmcflags} \
	-I/usr/include/ncurses -fno-rtti -fno-exceptions -fno-implicit-templates"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install scedit $RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
