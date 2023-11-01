%global fontname julietaula-montserrat
%global fontconf 61-%{fontname}
%global common_desc \
A typeface inspired by signs around the Montserrat area of Buenos Aires, Argentina

Name:		%{fontname}-fonts
Version:	7.200
Release:	2%{?dist}.2
# Override versioning to sync with upstream
Epoch:		1
Summary:	Sans-serif typeface inspired from Montserrat area

License:	OFL
URL:		https://github.com/JulietaUla/Montserrat
Source0:	%{url}/archive/Montserrat/v%{version}.tar.gz#/Montserrat-%{version}.tar.gz
Source1:	%{name}-fontconfig.conf
Source3:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
Requires:	fontpackages-filesystem

# Reset the old date based versioning
Obsoletes:	%{name} < 1:%{version}-%{release}


%description
%common_desc

%_font_pkg -f %{fontconf}.conf *.otf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%license Montserrat-%{version}/OFL.txt
%doc Montserrat-%{version}/README.md 

%prep
%autosetup -c

%build


%install
install -Dpm 0644 Montserrat-%{version}/fonts/otf/*.otf -t %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

# Install Montserrat fonts
install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

for fconf in %{fontconf}.conf ; do
    ln -s %{_fontconfig_templatedir}/$fconf \
	%{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata file, Repeat for every font family
install -Dm 0644 -p %{SOURCE3} \
		%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Wed May 27 2020 Akira TAGOH <tagoh@redhat.com> - 1:7.200-2.1
- Backport fontconfig files from Fedora
- Sub-packaging per family names as usually do in Fdora.
  Resolves: rhbz#1777843

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1:7.200-1
- Upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1:6.002-2
- Fix obsolete tag

* Mon May 15 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1:6.002-1
- Use Epoch to sync version with upstream
- Latest stable upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:20151221-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 20 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0:20151221-5
- Improved appstream file with fonts list

* Sun Mar 27 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0:20151221-4
- Fixed compatibility issue with Fedora 22 and EPEL7 less

* Fri Mar 25 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0:20151221-3
- Switched doc section to license
- Deleted oft and ttf subdirectories

* Fri Mar 25 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0:20151221-2
- Moved appstream-util to check section

* Thu Mar 24 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0:20151221-1
- Initial build
