%global pkg_name beust-jcommander
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global short_name   jcommander

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.30
Release:          5.9%{?dist}
Summary:          Java framework for parsing command line parameters
License:          ASL 2.0
URL:              http://jcommander.org/
Source0:          https://github.com/cbeust/%{short_name}/archive/%{short_name}-%{version}.tar.gz
BuildArch:        noarch
BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    maven30-beust-jcommander

%description
JCommander is a very small Java framework that makes it trivial to
parse command line parameters (with annotations).

%package javadoc
Summary:          API documentation for %{pkg_name}

%description javadoc
This package contains the %{summary}.

%prep
%setup -q -n %{short_name}-%{short_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
chmod -x license.txt
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_file : %{pkg_name}
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc license.txt notice.md README.markdown

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.30-5.9
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.30-5.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.30-5.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-5.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-5.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-5.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-5.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.30-5
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-4
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.30-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Feb  6 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-2
- Replace BR: xmvn with maven-local

* Thu Jan 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.30-1
- Update to upstream version 1.30
- Build with xmvn

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.17-6
- Install NOTICE files

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.17-3
- Use the new maven macro.

* Mon May 16 2011 Jaromir Capik <jcapik@redhat.com> - 1.17-2
- Unwanted comment removal
- Target javadoc:jar replaced with javadoc:aggregate

* Fri May 13 2011 Jaromir Capik <jcapik@redhat.com> - 1.17-1
- Initial version of the package
