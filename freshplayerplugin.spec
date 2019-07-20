
Summary:	Ppapi2npapi compatibility layer
Name:		freshplayerplugin
Version:	0.3.11
Release:	1
License:	MIT
Group:		Networking/WWW
Url:		https://github.com/i-rinat/freshplayerplugin
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(libva-x11)
BuildRequires:	pkgconfig(liburiparser)
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(libevent_pthreads)
BuildRequires:	pkgconfig(cairo)
BuildRequires:  pkgconfig(openssl)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	cmake
BuildRequires:	ragel

Requires:	chromium-pepper-flash

Conflicts:	%{name} < %{EVRD}

%description
Ppapi2npapi compatibility layer.

%files
%{_libdir}/mozilla/plugins/*.so*
%{_libdir}/PepperFlash

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}

%build
%ifarch %ix86
# i586 segfaults with clang
export CC=gcc
export CXX=g++
%endif

export LDFLAGS="%{optflags} -lrt"
%cmake
%make

%install
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins
cp build/libfreshwrapper-flashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/
pushd %{buildroot}%{_libdir}
ln -s chromium/PepperFlash PepperFlash
popd

