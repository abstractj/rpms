Name:           libunix-dbus-java
Version:        0.8.0
Release:        1%{?dist}
Summary:        Unix Sockets Library for DBus Java
Group:          Development/Libraries

License:        MIT

URL:            https://github.com/abstractj/libunix-dbus-java
Source:         https://github.com/abstractj/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc, java-1.8.0-openjdk-devel

%description
Native code to allow you to read and write Unix sockets in Java.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc
%{_libdir}/*.so.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Wed Mar  2 2016 abstractj
-
