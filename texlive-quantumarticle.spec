Name:		texlive-quantumarticle
Version:	65242
Release:	1
Summary:	Document class for submissions to the Quantum journal
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/quantumarticle
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quantumarticle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quantumarticle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the preferred document class for papers
to be submitted to "Quantum -- the open journal of quantum
science". It is based on the widely used article document class
and designed to allow a seamless transition from documents
typeset with the article, revtex4-1, and elsarticle document
classes. As a service to authors, the document class comes with
a predefined bibilography style quantum.bst that is optimized
to be used with the quantumarticle document class.
Additionally, the quantumview documentclass is provided, which
can be used as a proxy to typeset the HTML-only editorial
pieces in Quantum Views in a LaTeX editor. The quantumarticle
document class also offers an option to remove the
Quantum-related branding. In that way, users appreciating the
esthetics of this document class can use it for their notes as
well.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/quantumarticle
%{_texmfdistdir}/bibtex/bst/quantumarticle
%doc %{_texmfdistdir}/doc/latex/quantumarticle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
