# revision 23861
# category Package
# catalog-ctan /macros/latex/contrib/muthesis
# catalog-date 2011-08-26 08:26:07 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-muthesis
Version:	20110826
Release:	1
Summary:	Classes for University of Manchester Dept of Computer Science
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/muthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/muthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/muthesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The bundle provides thesis and project report document classes
from the University of Manchester's Department of Computer
Science.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/muthesis/muthesis.cls
%{_texmfdistdir}/tex/latex/muthesis/third-rep.cls
%doc %{_texmfdistdir}/doc/latex/muthesis/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
