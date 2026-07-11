%global tl_name muthesis
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Classes for University of Manchester Dept of Computer Science
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/muthesis
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/muthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/muthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides thesis and project report document classes from the
University of Manchester's Department of Computer Science.

