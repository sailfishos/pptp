Name:       pptp
Summary:    Client for the proprietary Microsoft Point-to-Point Tunneling Protocol
Version:    1.8.0
Release:    1
Group:      Applications/Internet
License:    GPLv2+
URL:        http://pptpclient.sourceforge.net/
Source0:    https://sourceforge.net/projects/pptpclient/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:     ip-location.patch
Patch1:     install-ownership.patch
BuildRequires:  coreutils
BuildRequires:  ppp-devel

%description
PPTP client for the proprietary Microsoft Point-to-Point Tunneling Protocol.


%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1
%patch1 -p1

%build
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/sbin/pptp
/usr/sbin/pptpsetup
%config %{_sysconfdir}/ppp/options.pptp
%exclude %{_mandir}/man8/pptp.8.gz
%exclude %{_mandir}/man8/pptpsetup.8.gz

