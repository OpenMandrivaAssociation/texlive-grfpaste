Name:		texlive-grfpaste
Version:	17354
Release:	1
Summary:	Include fragments of a dvi file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/grfpaste
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grfpaste.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grfpaste.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
