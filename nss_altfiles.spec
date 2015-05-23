Summary:	NSS module to read passwd/group files from alternate locations
Name:		nss_altfiles
Version:	2.18.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://github.com/aperezdc/nss-altfiles/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9b7974fe70147d38f778b2ef7d153405
URL:		https://github.com/aperezdc/nss-altfiles
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_check_so 1 

%description
This is a NSS module which can read user information from files in the
same format as /etc/passwd and /etc/group stored in an alternate
location (/lib by default).

Essentially, it is a tweaked copy of the sources for the NSS files
module included with eglibc. It should work with glibc2 as well.

%prep
%setup -q -n nss-altfiles-%{version}

%build
%configure \
	--libdir=/%{_lib}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) /%{_lib}/libnss_altfiles.so.2
