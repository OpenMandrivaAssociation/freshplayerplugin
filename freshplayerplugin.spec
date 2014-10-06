%define git 20140903

Summary:	Ppapi2npapi compatibility layer
Name:		freshplayerplugin
Version:	0
Release:	0.%{git}.2
License:	MIT
Group:		Networking/WWW
Url:		https://github.com/i-rinat/freshplayerplugin
Source0:	%{name}-%{git}.tar.gz

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libconfig)
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(libevent_pthreads)
BuildRequires:	pkgconfig(liburiparser)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	cmake
Requires:	chromium-browser-pepper-flash

%description
Ppapi2npapi compatibility layer.

%files
%{_libdir}/mozilla/plugins/*.so*
%{_libdir}/PepperFlash

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}

%build
%cmake
%make

%install
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins
cp build/libfreshwrapper-pepperflash.so %{buildroot}%{_libdir}/mozilla/plugins/
mkdir -p %{buildroot}/usr/lib/
pushd %{buildroot}%{_libdir}
ln -s chromium-browser/PepperFlash PepperFlash
popd


