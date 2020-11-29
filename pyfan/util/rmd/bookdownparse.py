"""Generate README from Fan Rmd Frontmatter
The :mod:`pyfan.util.rmd.bookdownparse` generates rmd frontmatter.

Generates README.md TOC contents based on parsed YAML frontmatter from files listed
in a bookdown yaml file that contains a list of RMD files to process through.

Includes method :func:`fs_yml2readme`
"""

import yaml
import frontmatter
import pyfan.util.rmd.rmdparse as rmdparse
import os


def fs_yml2readme(sfc_prj='R4Econ',
                  sph_prj='C:/Users/fan/R4Econ/',
                  spn_prj_bookdown_yml='_bookdown.yml',
                  spn_prj_readme_toc='README_toc.md',
                  ls_st_ignore=['index.Rmd', 'README_appendix.md', 'title.Rmd', 'main.Rmd'],
                  sph_pdf='htmlpdfr',
                  sph_html='htmlpdfr',
                  sph_r='htmlpdfr',
                  st_file_type='r',
                  verbose=False):
    """Write to file README detailed TOC for files in bookdown yaml list

    Parameters
    ----------
    sfc_prj : string
        The git project name
    sph_prj : string
        the local path to the git project
    spn_prj_bookdown_yml : string
        yml file name under project root contains rmd names under 'rmd_files' key
    spn_prj_readme_toc : string
        md generated file name under project root
    ls_st_ignore: list
        list of string names to ignore
    sph_pdf : string
        subfolder to store pdf files in the rmd folder
    sph_html : string
        subfolder to store html files in the rmd folder
    sph_r : string
        subfolder to store r files in the rmd folder does not
        have to be r, any other raw file type, m of py for example
    st_file_type: string
        the RMD file is for which underlying language: r for R, m for matlab, py
        for python
    verbose: bool
        print details

    Returns
    -------
    None
        nothing is returned, the spn_prj_readme_toc toc file is generated

    Examples
    --------

    >>> fs_yml2readme(sfc_prj='pyfan', sph_prj='../../../', verbose=False)

    """

    spn_readme = sph_prj + spn_prj_readme_toc
    f_core = open(spn_readme, "w")

    spn_yml = sph_prj + spn_prj_bookdown_yml
    with open(spn_yml, 'r') as f:
        ob_book_yml = yaml.load(f, Loader=yaml.BaseLoader)

    ls_st_rmd_files = ob_book_yml['rmd_files']

    sfc_main = 'main.Rmd'
    ctr_chapter = 0
    ctr_section = 0
    ctr_subsection = 0

    for sfc in ls_st_rmd_files:

        if sfc in ls_st_ignore:
            if verbose:
                print('ignore:' + sfc)

        elif sfc_main in sfc:

            # Load _main File
            spn_rmd_main = sph_prj + sfc
            ob_yml_rmd_main = frontmatter.load(spn_rmd_main)
            ob_yml_rmd_main = ob_yml_rmd_main.content + '\n\n'

            # section heading with proper numbering
            it_pound = ob_yml_rmd_main.count("#")
            if it_pound == 1:
                ctr_chapter = ctr_chapter + 1
                ctr_section = 0
                ctr_subsection = 0
                st_text_out = '# ' + str(ctr_chapter) + ' ' + \
                              ob_yml_rmd_main.replace("#", "")
                if ctr_chapter != 1:
                    st_text_out = '\n' + st_text_out
            elif it_pound == 2:
                ctr_section = ctr_section + 1
                ctr_subsection = 0
                st_text_out = '## ' + str(ctr_chapter) + '.' + str(ctr_section) + \
                              ' ' + ob_yml_rmd_main.replace("#", "")
                if ctr_section != 1:
                    st_text_out = '\n' + st_text_out
            # write to file
            if verbose:
                print(st_text_out)
            f_core.write(st_text_out)

        else:

            # Load RMD front matter and summarize
            ctr_subsection = ctr_subsection + 1
            st_head_link, ls_desc_out, ls_code_out = \
                rmdparse.fs_rmd_yml_parse(
                    sfc_prj=sfc_prj, sph_prj=sph_prj, spn_prj_rmd=sfc,
                    sph_pdf=sph_pdf,
                    sph_html=sph_html,
                    sph_r=sph_r,
                    st_file_type=st_file_type)

            # write to file file title and main
            st_text_out = str(ctr_subsection) + '. ' + st_head_link + '\n'
            if verbose:
                print(st_text_out)
            f_core.write(st_text_out)

            # write to file file desc
            for st_desc in ls_desc_out:
                f_core.write(st_desc + '\n')
            for st_code in ls_code_out:
                f_core.write(st_code + '\n')

    # ls_front_keys = ob_book_yml.keys()
    # print(ls_front_keys)

    f_core.close()

# if __name__ == '__main__':
#     # sfc_prj = 'R4Econ'
#     # sph_prj = 'C:/Users/fan/R4Econ/'
#     # spn_prj_bookdown_yml = '_bookdown.yml'
#     # spn_prj_readme_toc = 'README_toc_two.md'
#     #
#     # fs_yml2readme(sfc_prj=sfc_prj,
#     #               sph_prj=sph_prj,
#     #               spn_prj_bookdown_yml=spn_prj_bookdown_yml,
#     #               spn_prj_readme_toc=spn_prj_readme_toc)
#
#     # fs_yml2readme(sfc_prj='pyfan', sph_prj='../../../', verbose=False)
#
#     fs_yml2readme(sfc_prj='Math4Econ',
#                   sph_prj='C:/Users/fan/Math4Econ/',
#                   spn_prj_bookdown_yml='_bookdown.yml',
#                   spn_prj_readme_toc='README_toc.md',
#                   ls_st_ignore=['index.Rmd', 'README_appendix.md', 'title.Rmd', 'main.Rmd'],
#                   sph_pdf='htmlpdfm',
#                   sph_html='htmlpdfm',
#                   sph_r='htmlpdfm',
#                   st_file_type='m',
#                   verbose=True)
