Summary:	BBS client based on Qt library in Linux
Name:	qterm
Version:	0.4.0
Release:	%mkrel 1
License:	GPL
Group:	Networking/Remote access
Source:	%{name}-%{version}.tar.bz2
URL:	http://qterm.sourceforge.net
BuildRequires:	qt3-devel
BuildRequires:	openssl-devel
BuildRequires:	arts-devel
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
QTerm is a BBS client in Linux

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x

%make

%install
%makeinstall_std
desktop-file-install --vendor="" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--remove-key="MimeTypes" \
	--remove-category="Application" \
	--add-category="RemoteAccess" \
	$RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/icons/%{name}.png
%{_datadir}/applications/%{name}.desktop
