Name:		texlive-muthesis
Version:	23861
Release:	1
Summary:	Classes for University of Manchester Dept of Computer Science
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/muthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/muthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/muthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides thesis and project report document classes
from the University of Manchester's Department of Computer
Science.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/muthesis
%doc %{_texmfdistdir}/doc/latex/muthesis

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
