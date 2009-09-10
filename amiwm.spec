%define name	amiwm
%define	version	0.20.48
%define release	%mkrel 13

Summary:  	A Window Manager for the X Window System
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Graphical desktop/Other
URL:		http://www.lysator.liu.se/~marcus/amiwm.html
Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}README
Source2:	amiwmrc-default
Source3:	startamiwm
Source4:	%{name}-wmsession.xpm

Requires:	mandrake_desk >= 7.2-18mdk, xloadimage
BuildRequires:	X11-devel byacc flex
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
amiwm is an X window manager that tries to make your display look and feel
like an Amiga® Workbench® screen. It is fully functional and can do all the
usual window manager stuff, like moving and resizing windows.

%prep
%setup -q

%build
%configure --prefix=%_prefix/X11R6 --exec_prefix=%_prefix/X11R6

%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}/X11R6/bin/

make install \
    prefix=%buildroot%_prefix/X11R6 \
    exec_prefix=%buildroot%_prefix/X11R6 \
    mandir=%buildroot%_mandir

mkdir -p %{buildroot}%_prefix/X11R6/lib/amiwm/
cp %{SOURCE2} %{buildroot}%_prefix/X11R6/lib/amiwm/system.amiwmrc

# wmsession support
mkdir -p %{buildroot}/etc/X11/wmsession.d/
cat << EOFT > %{buildroot}/etc/X11/wmsession.d/20AmiWM
NAME=AMIWM
ICON=amiwm-wmsession.xpm
EXEC=/usr/X11R6/bin/startamiwm
DESC=AMIWM desktop environment
SCRIPT: 
exec /usr/X11R6/bin/startamiwm
EOFT

install -m 755 %{SOURCE3} %{buildroot}%{_prefix}/X11R6/bin/startamiwm

rm -f %buildroot%_prefix/X11R6/bin/requestchoice

%clean
rm -fr %{buildroot}

%post
%{make_session}

%postun
%{make_session}

%files
%defattr(-,root,root) 
%doc README LICENSE INSTALL
%{_prefix}/X11R6/bin/amiwm
%{_prefix}/X11R6/bin/startamiwm
%{_prefix}/X11R6/bin/ppmtoinfo
%config(noreplace) /etc/X11/wmsession.d/*
#%dir %{prefix}/lib/X11/%{name}/icons
%{_mandir}/man1/amiwm.1*
#%{_bindir}/executecmd
#%{_bindir}/Keyboard
#%{_bindir}/requestchoice
%dir %{_prefix}/X11R6/lib/%name
%{_prefix}/X11R6/lib/%name/*

