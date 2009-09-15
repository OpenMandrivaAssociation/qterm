Summary: BBS client based on Qt library in Linux
Name: qterm
Version: 0.5.2
Release: %mkrel 2
License: GPLv2+
Group: Networking/Remote access
Source:	http://mesh.dl.sourceforge.net/sourceforge/qterm/%{name}-%{version}.tar.bz2
Patch0: qterm-0.5.2-link-crypto.patch
Patch1: qterm-0.5.2-gcc43.patch
URL: http://qterm.sourceforge.net
BuildRequires:	qt4-devel cmake
BuildRequires:	openssl-devel
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
QTerm is a BBS client in Linux

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .crypto
%patch1 -p0

%build
%cmake_qt4
%make

%install
rm -f %buildroot
%makeinstall_std -C build

cd src
mv -f %name.desktop.in %name.desktop
desktop-file-install --vendor="" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--remove-key="MimeTypes" \
	--remove-category="Application" \
	--add-category="RemoteAccess" \
	*.desktop
install -D %name.png %buildroot%_iconsdir/%name.png
cd -

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
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/icons/%{name}.png
%{_datadir}/applications/%{name}.desktop
