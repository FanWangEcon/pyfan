"""pyfan generate and clean pdf files from folder
The :mod:`pyfan.util.pdf_pdfgen` generates pdf files from tex files.

Gather all tex files from a folder, allow for exclusion strings. Generate PDFs
from the tex files. And then clean up extraneous PDF outputs.

Includes method :func:`ff_pdf_gen_clean`.
"""

import subprocess
import os
from pathlib import Path


def ff_pdf_gen_clean(ls_spt_srh=None,
                     spt_out='C:/Users/fan/Documents/Dropbox (UH-ECON)/' +
                             'Project Emily Minority Survey/' +
                             'EthLang/reg_lang_abi_cls_mino/',
                     spn_pdf_exe='C:/texlive/2019/bin/win32/xelatex.exe',
                     ls_st_contain=None,
                     ls_st_ignore=None,
                     bl_recursive=False,
                     bl_clean=True,
                     ls_suf_clean=None):
    """Generate pdf files from latex files in various folders.

    This file serves important paper generation function. It compiles multiple
    files satisfying string search requirements or exclusion conditions in
    multiple folders, and saves resulting pdf outputs in one folder. This allows
    for easy testing and management of mutiple pdf/latex files for the same project.
    Suppose there is a longer version of a paper, a shorter version, and an
    appendix file. We want to regularly test the compilations of all files,
    otherwise, as we work on one of the files, perhaps we some something in the
    some shared files that lead to other files breaking without knowing.

    This should be run for all outward facing pdf/tex files for a project regularly
    in order to check if all files still compile.

    By brining resulting outputs to a single folder, this makes it easier to see
    all paper and project relevant outputs. Additionally, this cleans up all
    pdf generated extraneous files once we have pdf itself, saving pdf compile
    folder clutter.

    Parameters
    ----------
    ls_spt_srh : :obj:`list` of :obj:`str`
        A list of strings of the path in which to search for tex files. They should
        be all on the same path. If `bl_recursive` is true, then this searchs in
        all subfolders.
    spt_out : str
        The Path to store outputs. All PDFs stored under single directory. This
        path must be directly on the same path as `ls_spt_srh', can be higher up
        on the same tree, but not on a different branch.
    spn_pdf_exe: str
        The path to the pdflatex or alternative exe file
    ls_st_contain: :obj:`list` of :obj:`str`
        a list of strings the found names must contain one of these search words, not all, just one of.
    ls_st_ignore : :obj:`list` of :obj:`str`
        a list of string file names to ignore
    bl_recursive : bool
        Whether to search for all tex files within subfolders
    bl_clean : bool
        To clean up after file generation
    ls_suf_clean: :obj:`list` of :obj:`str`
        list of

    Returns
    -------
    dict
        A list of string pdf file names outputed,

    """

    # Set mutables
    if ls_spt_srh is None:
        ls_spt_srh = ['C:/Users/fan/Documents/Dropbox (UH-ECON)/' +
                      'Project Emily Minority Survey/' +
                      'EthLang/reg_lang_abi_cls_mino/']
    if ls_st_contain is None:
        ls_st_contain = None
        # ls_st_contain = ['_yg.']
    if ls_st_ignore is None:
        ls_st_ignore = ['all.tex']
    if ls_suf_clean is None:
        ls_suf_clean = ['.aux', '.log', '.out', '.bbl',
                        '.blg', '-blx.bib', '.fff', '.run.xml']

    # Search for tex files in folders
    if bl_recursive:
        # use rglob
        ls_spn_found = [spn_file
                        for spt_srh in ls_spt_srh
                        for spn_file in Path(spt_srh).rglob('*.tex')]
    else:
        # use glob
        ls_spn_found = [spn_file
                        for spt_srh in ls_spt_srh
                        for spn_file in Path(spt_srh).glob('*.tex')]

    # collect tex and pdf outputs
    dc_tex_pdf = {}
    # Generate pdf from found tex files
    for spn_found in ls_spn_found:
        # convert WindosPath to String
        spn_found = str(spn_found)

        # search through ignore list
        if sum([st_ignore in spn_found
                for st_ignore in ls_st_ignore]):
            pass
        else:

            if (ls_st_contain is None) or \
                    (sum([st_contain in spn_found
                          for st_contain in ls_st_contain]) > 0):

                # change to local directory
                os.chdir(os.path.split(spn_found)[0])

                # generate pdf
                subprocess.call([spn_pdf_exe, '-output-directory',
                                 spt_out, spn_found], shell=False)

                # collect results
                snm_file = Path(spn_found).stem
                dc_tex_pdf[spn_found] = spt_out + snm_file + '.pdf'

                # path no suffix
                if bl_clean:
                    path_no_suffix = os.path.splitext(spn_found)[0]
                    ls_st_remove_suffix = ls_suf_clean
                    for st_suffix in ls_st_remove_suffix:

                        # in tex directory
                        srn_cur_file = path_no_suffix + st_suffix
                        if os.path.isfile(srn_cur_file):
                            os.remove(srn_cur_file)

                        # in pdf output directory
                        srn_cur_file = spt_out + snm_file + st_suffix
                        if os.path.isfile(srn_cur_file):
                            os.remove(srn_cur_file)

    return dc_tex_pdf
