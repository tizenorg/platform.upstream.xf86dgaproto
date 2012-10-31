Name:     xf86dgaproto
Summary:  X.Org X11 Protocol xf86dgaproto
Version:  2.1
Release:  1
Group:    Development/System
License:  MIT
URL:      http://www.x.org
Source0:  %{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires: pkgconfig(xorg-macros)

%description
%{summary}.

%prep
%setup -q

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
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
