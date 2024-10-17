Name:		texlive-numerica-plus
Version:	68019
Release:	1
Summary:	Iteration and recurrence relations: finding fixed points, zeros and extrema of functions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/numerica-plus
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numerica-plus.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numerica-plus.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines commands to iterate functions of a single
variable, find fixed points, zeros and extrema of such
functions, and calculate the terms of recurrence relations.
numerica-plus requires the package numerica, version 2, which
in turn requires l3kernel , l3packages, and the amsmath and
mathtools packages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/numerica-plus
%doc %{_texmfdistdir}/doc/latex/numerica-plus

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
