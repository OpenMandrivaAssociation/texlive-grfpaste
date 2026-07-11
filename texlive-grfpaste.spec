%global tl_name grfpaste
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Include fragments of a dvi file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/grfpaste
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grfpaste.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grfpaste.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides a mechanism to include fragments of dvi files with the graphicx
package, so that you can use \includegraphics to include dvi files. The
package requires the dvipaste program.

