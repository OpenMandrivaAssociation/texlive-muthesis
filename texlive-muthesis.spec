# revision 23861
# category Package
# catalog-ctan /macros/latex/contrib/muthesis
# catalog-date 2011-08-26 08:26:07 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-muthesis
Version:	20110826
Release:	8
Summary:	Classes for University of Manchester Dept of Computer Science
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/muthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/muthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/muthesis.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/muthesis/muthesis.cls
%{_texmfdistdir}/tex/latex/muthesis/third-rep.cls
%doc %{_texmfdistdir}/doc/latex/muthesis/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110826-2
+ Revision: 754239
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110826-1
+ Revision: 719092
- texlive-muthesis
- texlive-muthesis
- texlive-muthesis
- texlive-muthesis

