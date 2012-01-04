# revision 17354
# category Package
# catalog-ctan /macros/latex/contrib/grfpaste
# catalog-date 2010-03-06 14:40:43 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-grfpaste
Version:	0.2
Release:	2
Summary:	Include fragments of a dvi file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/grfpaste
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grfpaste.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grfpaste.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a mechanism to include fragments of dvi files with the
graphicx package, so that you can use \includegraphics to
include dvi files. The package requires the dvipaste program.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/grfpaste/grfpaste.sty
%doc %{_texmfdistdir}/doc/latex/grfpaste/doc/grfpaste.pdf
%doc %{_texmfdistdir}/doc/latex/grfpaste/doc/grfpaste.tex
%doc %{_texmfdistdir}/doc/latex/grfpaste/dvipaste.txt
%doc %{_texmfdistdir}/doc/latex/grfpaste/grfp1.tex
%doc %{_texmfdistdir}/doc/latex/grfpaste/grfp2.tex
%doc %{_texmfdistdir}/doc/latex/grfpaste/grfp3.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
