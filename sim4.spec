%define name		sim4
%define version		20030921
%define split_version	2003-09-21
%define release		%mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Program to align cDNA and genomic DNA
Group:		Sciences/Biology
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
URL:		http://globin.cse.psu.edu/html/docs/sim4.html
Source:		http://globin.cse.psu.edu/ftp/dist/sim4/%{name}.%{split_version}.tar.bz2

%description
sim4 is a similarity-based tool for aligning an expressed DNA sequence
(EST, cDNA, mRNA) with a genomic sequence for the gene.
It also detects end matches when the two input sequences overlap at one end
(i.e., the start of one sequence overlaps the end of the other)

Reference for Sim4:
L. Florea, G. Hartzell, Z. Zhang, G. Rubin, and W. Miller (1998)
"A computer program for aligning a cDNA sequence with a genomic DNA sequence."
Genome Research 8, 967-974.

%prep
%setup -n %{name}.%{split_version}

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
install -m 755 %{name} -D %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYRIGHT README.sim4 VERSION
%{_bindir}/%{name}


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 20030921-8mdv2011.0
+ Revision: 614866
- the mass rebuild of 2010.1 packages

* Mon Mar 15 2010 Eric Fernandez <zeb@mandriva.org> 20030921-7mdv2010.1
+ Revision: 519808
- bump release version and rebuild

* Wed May 06 2009 Eric Fernandez <zeb@mandriva.org> 20030921-6mdv2010.0
+ Revision: 372453
- new URL and rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 20030921-6mdv2009.0
+ Revision: 242688
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Eric Fernandez <zeb@mandriva.org> 20030921-4mdv2008.0
+ Revision: 60144
- Import sim4



* Wed Aug 08 2007 Eric Fernandez <zeb@zebulon.org.uk> 20030921-4mdv2008.0
- rebuild

* Fri Jun 23 2006 Eric Fernandez <zeb@zebulon.org.uk> 20030921-3mdv2007.0
- rebuild

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 20030921-1mdk
- New release 20030921
- spec cleanup

* Wed Aug 04 2004 Guillaume Rousse <guillomovitch@mandrake.org> 20020303-3mdk 
- rebuild

* Mon Aug 04 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 20020303-2mdk
- rebuild
- rm -rf %%{buildroot} in %%install, not %%prep
- cosmetics

* Sat Jan 25 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 20020303-1mdk
- first mdk release with a spec stolen from Luc Ducazu <luc@biolinux.org>
