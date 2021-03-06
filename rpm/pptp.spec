Name:       pptp
Summary:    Client for the proprietary Microsoft Point-to-Point Tunneling Protocol
Version:    1.10.0
Release:    1
License:    GPLv2+
URL:        http://pptpclient.sourceforge.net/
Source0:    https://sourceforge.net/projects/pptpclient/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:     ip-location.patch
Patch1:     install-ownership.patch
BuildRequires:  coreutils
BuildRequires:  ppp-devel


%description
PPTP client for the proprietary Microsoft Point-to-Point Tunneling Protocol.

%package setup
Summary:    PPTP configuration script
Requires:   %{name} = %{version}-%{release}

%description setup
PPTP Configuration script.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%license COPYING
%{_sbindir}/pptp
%config %{_sysconfdir}/ppp/options.pptp
%exclude %{_mandir}/man8/pptp.8.gz
%exclude %{_mandir}/man8/pptpsetup.8.gz

%files setup
%{_sbindir}/pptpsetup

