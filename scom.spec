%define	name	scom
%define	version	0.3.3b
%define	release	1
%define	prefix	/usr

%define fname	sc

Summary:	Sunshine Commander.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Prefix:		%{prefix}
Copyright:	GPL
Group:		System Environment/Shells
URL:		http://www.poulsen.org/sc/
Vendor:		Morten Poulsen <sc@poulsen.org>
Source:		%{fname}-%{version}.tar.gz
Patch:		sc-0.2.0-makefix.patch
BuildRoot:	/var/tmp/%{name}-%{version}

%description
  Sunshine Commander is an attempt to make a consolebased, crossplatform,
filemanager, which allows the user to do common filecentred tasks within a 
single program, including full linux-filesystem support, archivehandling, 
FTP-handling etc.

%prep
%setup -q -n %{fname}-%{version}
%patch -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS"; export CXXFLAGS;
%configure --prefix=%{prefix}

make

%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install-strip

%clean
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{prefix}/bin/*

%changelog
* Tue Jun 27 2000 Ryan Weaver <ryanw@infohwy.com>
  [scom-0.3.3b-1]
- Still working on proper handling of archives with no dir-records. 
- A couple of cosmetic bugs when running in a quite large terminal
  window.
    
  [scom-0.3.2-1]
- Begun work on FTP and fixing dirs in tar.gz archives
- Accelerated startup in Linux seriously
- Some cosmetic changes in monochrome support, now only active when you
  are actually running a monochrome console
- Fixed some keyboard issues regarding the rxvt console
- Several smaller cosmetic problems fixed  
- Fixed a bug which caused sc to crash sometime when running as root.
  
  [scom-0.3.1-1]
- Fixed a bug in DOS-version which caused SC to skip 1 entry in each
  accessed directory.
    
  [scom-0.3.0-1]
- Begun implementing TAB-completed dirsearch in tree. Check it out
  and tell what you think.
- Enabled printing (linux only, so far), just copy files to the printer  
- Fixed a bug when deleting whole dirs including symlinks

* Mon May 15 2000 Ryan Weaver <ryanw@infohwy.com>
  [scom-0.2.0-1]
- fixed some archive related bugs
- some more minor speed optimizations
- Fixed a strange bug when pressing enter at [..] entry. Sometimes
  it didn't change to upper dir...
- Reformatted Changelog and README to the look nicer when viewed from
  the System info dialog.
- Debug log is now disabled, enable with parameter -d or --debug
- Get info about commandline parameters with -h or --help
- Huge speed improvements!          
- Worked on the usermenu has great features now, and more are coming!
- Added wordwrapping in textfile viewer (key w)                              
- Builtin ChangeLog and README-files
- Fixed filesystem info
- Now checking for available space at destination when copying/moving
- I begun to make some kind on monochrome support, for consoles which do not
  support colors in any flavor (curses should work on just about anything, 
  right?)
- Fixed some bugs in the editor (quite a few actually ;-))
- Tried to optimize screenwriting of files a bit...
- Quick drivechange in DOS-version (ctrl-driveletter), what should these
  keys do in linux? Any suggestions?
- Ending up in the last accessed directory now works in Linux!!!
  Please read the README-file for information on how to set it up.
- Fixed a bug causing the tree to fail when accessed from the root
- Targz and ZIP should now work, but I have noticed some unstability but
  have been unable to located the errors. Please report.
- As always some minor fixes/changes.  
- Fixed a lot of smaller issues, like [..]-bugs in linux, gotolast dir
  in DOS (still working on linux...).
- Added a "tip of the day"-function, now I just have to think of some
  tips... ;-) And fixed it afterwards... 

* Mon Mar 20 2000 Ryan Weaver <ryanw@infohwy.com>
- Renamed rpm from sc to scom. sc is a SpreedSheat rpm still being
  distributed in the SUSE Distribution. (Thanks Frank Ball <frankb@sonic.net>)

  [scom-0.1.1a-1]
- I am working on tar.gz and zip support... Please standby
- Executing external programs fixed

* Fri Mar 17 2000 Ryan Weaver <ryanw@infohwy.com>
  [sc-0.1.0-1]
- Initial RPM Build.
- Initial Release.
