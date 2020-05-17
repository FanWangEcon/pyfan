# cd "C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/Math4Econ/calconevar"
# pandoc -s interval.tex -o interval.md
# pandoc -s localglobal.tex -o localglobal.md
# pandoc -s polynomial.tex -o polynomial.md
#
# cd "C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/Math4Econ/calconevar"
# pandoc -s polynomial.tex -o polynomial.md
#
# replace matlabcode by lstlisting
# replace matlabtitle by subsubsection
# replace matlabtitle by subsubsection
# replace matlabheading by paragraph
# replace [width=/maxwidth{56.196688409433015em}]{
#     by {polynomial_image/
#
# 1. convert mlx to tex
# 2. tex replace as above
# 3. convert to md
# 4. md add front matter as separate files, to be merged with md output here.

# spt_convert_tex = 'C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/Math4Econ/calconevar/'
# snm_mat_tex_auto = 'interval.tex'
# spn_convert_tex = spt_convert_tex + snm_mat_tex_auto
#
# with open(spn_convert_tex) as fl_tex:
#     fl_tex_new = fl_tex.read().replace('matlabcode', 'lstlisting')
#
# with open(spn_convert_tex, "w") as f:
#     f.write(fl_tex_new)
#
# from pathlib import Path

from pathlib import Path
import subprocess
import os


def ff_mlxtex2md():
    verbose = False

    # Directories to search in
    spt_root = "C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/Math4Econ/"
    ls_srt_subfolders = ['calconevar/', 'derivative/', 'derivative_application/',
                         'matrix_basics/',
                         'opti_firm_constrained/', 'opti_hh_constrained_brsv/',
                         'opti_hh_constrained_brsv_inequality/']
    ls_spt = [spt_root + srt_subf for srt_subf in ls_srt_subfolders]
    print(ls_spt)

    # get file names
    ls_spn_found_tex = [spn_file for spt_srh in ls_spt
                        for spn_file in Path(spt_srh).rglob('*.tex')]
    print(ls_spn_found_tex)

    for spn_found_tex in ls_spn_found_tex:
        if verbose:
            print(spn_found_tex)
        fl_tex_contents = open(spn_found_tex)
        stf_tex_contents = fl_tex_contents.read()

        # file image folder
        sna_file = Path(spn_found_tex).stem

        # define new and old
        ls_st_old = ['matlabcode', 'matlabtitle', 'matlabheading',
                     '[width=\\maxwidth{56.196688409433015em}]{']
        ls_st_new = ['lstlisting', 'subsubsection', 'paragraph',
                     'by {' + sna_file + '_image/']

        # zip and loop and replace
        for old, new in zip(ls_st_old, ls_st_new):
            stf_tex_contents = stf_tex_contents.replace(old, new)
        if verbose:
            print(stf_tex_contents)

        # convert from tex to md
        path_no_suffix = os.path.splitext(spn_found_tex)[0]
        spn_md = path_no_suffix + '.md'
        print(spn_found_tex)
        print(spn_md)
        subprocess.call(['pandoc', '-s', str(spn_found_tex), '-o', str(spn_md)])

    # m4econ to root
    # with several testing md files with preamble/frontmatter, generate bookdown
    # after generating bookdown, add in personalized preamble.
    # generate a folder with only preambles, and merge the md files created here with those


if __name__ == '__main__':
    ff_mlxtex2md()
