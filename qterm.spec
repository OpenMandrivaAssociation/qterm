Summary: BBS client based on Qt library in Linux
Name: qterm
Version: 0.5.11
Release: %mkrel 1
License: GPLv2+
Group: Networking/Remote access
Source:	http://mesh.dl.sourceforge.net/sourceforge/qterm/%{name}-%{version}.tar.bz2
URL: http://qterm.sourceforge.net
BuildRequires:	qt4-devel
BuildRequires:	cmake
BuildRequires:	phonon-devel
BuildRequires:	openssl-devel
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
QTerm is a BBS client in Linux

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_qt4 -DQT_PHONON_INCLUDE_DIR:PATH=%_includedir/KDE -DCMAKE_SKIP_RPATH:BOOL=ON
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

desktop-file-install --vendor="" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--remove-key="MimeTypes" \
	--remove-category="Application" \
	--add-category="RemoteAccess" \
	%buildroot%_datadir/applications/*.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_iconsdir}/*/*/*/*
%{_datadir}/applications/%{name}.desktop
