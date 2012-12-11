Summary: BBS client based on Qt library in Linux
Name: qterm
Version: 0.5.12
Release: %mkrel 1
License: GPLv2+
Group: Networking/Remote access
Source0: http://mesh.dl.sourceforge.net/sourceforge/qterm/%{name}-%{version}.tar.bz2
URL: http://qterm.sourceforge.net
BuildRequires:	qt4-devel
BuildRequires:	cmake
BuildRequires:	phonon-devel
BuildRequires:	qt4-designer
BuildRequires:	qt4-assistant
BuildRequires:	pkgconfig(openssl)
BuildRequires:	desktop-file-utils
Patch0:		qterm-0.5.12-glibc216.patch
Patch1:		qterm-0.5.12-qt4.patch

%description
QTerm is a BBS client in Linux

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p0

%build
%cmake_qt4 -DQT_PHONON_INCLUDE_DIR:PATH=%_includedir/KDE -DCMAKE_SKIP_RPATH:BOOL=ON
%make

%install
%makeinstall_std -C build

desktop-file-install --vendor="" \
	--dir %{buildroot}%{_datadir}/applications \
	--remove-key="MimeTypes" \
	--remove-category="Application" \
	--add-category="RemoteAccess" \
	%buildroot%_datadir/applications/*.desktop

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_iconsdir}/*/*/*/*
%{_datadir}/applications/%{name}.desktop
