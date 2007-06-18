Summary:	BBS client based on Qt library in Linux
Name:	qterm
Version:	0.4.0
Release:	%mkrel 1
License:	GPL
Group:	Networking/Remote access
Source:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
QTerm is a BBS client in Linux

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x

%make

%install
make install-strip DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
