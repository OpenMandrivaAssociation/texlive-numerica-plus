%global tl_name numerica-plus
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0.0
Release:	%{tl_revision}.1
Summary:	Iteration and recurrence relations: finding fixed points, zeros and extrema o...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/numerica-plus
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numerica-plus.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numerica-plus.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines commands to iterate functions of a single variable,
find fixed points, zeros and extrema of such functions, and calculate
the terms of recurrence relations. numerica-plus requires the package
numerica, which in turn requires l3kernel , l3packages, and the amsmath
and mathtools packages.

