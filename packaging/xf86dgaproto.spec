%bcond_with x

Name:     xf86dgaproto
Summary:  X.Org X11 Protocol xf86dgaproto
Version:  2.1
Release:  1
Group:    Development/System
License:  MIT
URL:      http://www.x.org
Source0:  %{name}-%{version}.tar.bz2
Source1001: 	xf86dgaproto.manifest

BuildRequires: pkgconfig
BuildRequires: pkgconfig(xorg-macros)

%if !%{with x}
ExclusiveArch:
%endif

%description
%{summary}.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%remove_docs


%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
