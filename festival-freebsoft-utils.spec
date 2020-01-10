Name:          festival-freebsoft-utils
Version:       0.10
Release:       7%{?dist}
Summary:       A collection of utilities that enhance Festival with some useful features

Group:         System Environment/Libraries
BuildArch:     noarch
License:       GPLv2+
URL:           http://www.freebsoft.org/festival-freebsoft-utils
Source0:       http://devel.freebsoft.org/pub/projects/%{name}/%{name}-%{version}.tar.gz

BuildRequires: festival

Requires: festival
Requires: sox

%description
A collection of utilities that enhance Festival with some useful features. They 
provide all that is needed for interaction with Speech Dispatcher.

Key festival-freebsoft-utils features are:
- Generalized concept of input events. festival-freebsoft-utils allows not only 
  plain text synthesis, but also combining it with sounds. Additionally, 
  mechanism of logical events mapped to other events is provided. 
- Substitution of events for given words. 
- High-level voice selection mechanism and setting of basic prosodic parameters. 
- Spelling mode. 
- Capital letter signalization. 
- Punctuation modes, for explicit reading or not reading punctuation characters. 
- Incremental synthesis of texts and events. 
- Speech Dispatcher support. 
- Rudimentary SSML support. 
- Enhance the Festival extension language with functions commonly used in Lisp.
- Support for wrapping already defined Festival functions by your own code.
- Everything is written in the extension language, no patching of the Festival 
  C++ sources is needed.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_datadir}/festival/lib/
cp -p *.scm %{buildroot}/%{_datadir}/festival/lib/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING NEWS README
%{_datadir}/festival/lib/*.scm

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.10-7
- Mass rebuild 2013-12-27

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.10-5
- Update URLs and modernise spec

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 30 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.10-1
- Initial packaging
