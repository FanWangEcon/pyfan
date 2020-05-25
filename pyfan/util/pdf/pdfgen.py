"""pyfan generate and clean pdf files from folder

Gather all tex files from a folder, allow for exclusion strings. Generate PDFs
from the tex files. And then clean up extraneous PDF outputs.
"""

import subprocess
import os
from pathlib import Path


def ff_pdf_gen_clean(ls_spt_srh=None,
                     spt_out='C:/Users/fan/Documents/Dropbox (UH-ECON)/' +
                             'Project Emily Minority Survey/' +
                             'EthLang/reg_lang_abi_cls/',
                     spn_pdf_exe='C:/texlive/2019/bin/win32/xelatex.exe',
                     ls_st_contain=None,
                     ls_st_ignore=None,
                     bl_recursive=False,
                     bl_clean=True,
                     ls_suf_clean=None):
    """Generate pdf files from latex files in various folders.

    Parameters
    ----------
    ls_spt_srh : :obj:`list` of :obj:`str`
        A list of strings of the path in which to search for tex files.
    spt_out : str
        The Path to store outputs. All PDFs stored under single directory.
    spn_pdf_exe: str
        The path to the pdflatex or alternative exe file
    ls_st_contain: :obj:`list` of :obj:`str`
        a list of strings the found names must contain one of these search words
    ls_st_ignore : :obj:`list` of :obj:`str`
        a list of string file names to ignore
    bl_recursive : bool
        Whether to search for all tex files within subfolders
    bl_clean : bool
        To clean up after file generation
    ls_suf_clean: :obj:`list` of :obj:`str`
        list of
    """

    # Set mutables
    if ls_spt_srh is None:
        ls_spt_srh = ['C:/Users/fan/Documents/Dropbox (UH-ECON)/' +
                      'Project Emily Minority Survey/' +
                      'EthLang/reg_lang_abi_cls/']
    if ls_st_contain is None:
        ls_st_contain = None
        ls_st_contain = ['t6']
    if ls_st_ignore is None:
        ls_st_ignore = ['all.tex']
    if ls_suf_clean is None:
        ls_suf_clean = ['aux', 'log', 'out', 'bbl', 'blg']

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

                # path no suffix
                if bl_clean:
                    path_no_suffix = os.path.splitext(spn_found)[0]
                    ls_st_remove_suffix = ls_suf_clean
                    for st_suffix in ls_st_remove_suffix:
                        srn_cur_file = path_no_suffix + "." + st_suffix
                        if os.path.isfile(srn_cur_file):
                            os.remove(path_no_suffix + "." + st_suffix)


if __name__ == '__main__':
    ff_pdf_gen_clean()
