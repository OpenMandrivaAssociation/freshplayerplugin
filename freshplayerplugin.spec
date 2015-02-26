%define git 20150216

Summary:	Ppapi2npapi compatibility layer
Name:		freshplayerplugin
Version:	0.2.3
Release:	1.%{git}.1
License:	MIT
Group:		Networking/WWW
Url:		https://github.com/i-rinat/freshplayerplugin
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(liburiparser)
BuildRequires:	pkgconfig(libconfig)
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(libevent_pthreads)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	cmake
BuildRequires:	ragel
Requires:	chromium-pepper-flash

%description
Ppapi2npapi compatibility layer.

%files
%{_libdir}/mozilla/plugins/*.so*
%{_libdir}/PepperFlash

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{git}

%build
export LDFLAGS="%{optflags} -lrt"
%cmake
%make

%install
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins
cp build/libfreshwrapper-pepperflash.so %{buildroot}%{_libdir}/mozilla/plugins/
pushd %{buildroot}%{_libdir}
ln -s chromium/PepperFlash PepperFlash
popd

