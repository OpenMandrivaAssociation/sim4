%define name		sim4
%define version		20030921
%define split_version	2003-09-21
%define release		%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Program to align cDNA and genomic DNA
Group:		Sciences/Biology
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
URL:		http://globin.cse.psu.edu
Source:		http://globin.cse.psu.edu/dist/sim4/%{name}.%{split_version}.tar.bz2

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
