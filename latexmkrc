# Build configuration for the existing XeLaTeX template.
# The source directory is the working directory when invoked by the root justfile.

use Cwd qw(abs_path);

my $source_dir = abs_path('.');

# TeX and BibTeX may run from the output directory. Keep source resources
# discoverable without requiring machine-specific absolute paths in .tex files.
$ENV{'TEXINPUTS'} = "$source_dir//:" . ($ENV{'TEXINPUTS'} // '');
$ENV{'BIBINPUTS'} = "$source_dir//:" . ($ENV{'BIBINPUTS'} // '');

$pdf_mode = 5;
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -halt-on-error %O %S';
$bibtex = 'bibtex %O %B';

# Keep build decisions deterministic and let latexmk perform required reruns.
$max_repeat = 8;
