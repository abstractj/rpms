Name:		  firefox
Version:  43.0
Release:	43%{?dist}
Summary:	firefox

Group:		System Environment/Browsers
License:	ISC
URL:		https://tmux.github.io/

https://download-installer.cdn.mozilla.net/pub/firefox/releases/43.0/linux-x86_64/en-US/firefox-43.0.tar.bz2
Source:	https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc ncurses-devel libevent-devel >= 2.0
Requires:	ncurses libevent

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/tmux
%{_mandir}/man1/tmux.1.gz


%changelog

