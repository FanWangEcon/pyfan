"""Generate README from Fan Rmd Frontmatter

Generates README.md TOC contents based on parsed YAML frontmatter from files listed
in a bookdown yaml file that contains a list of RMD files to process through.
"""

import yaml
import frontmatter
import pyfan.util.rmd.rmdparse as rmdparse
import os


def fs_yml2readme(sfc_prj='R4Econ',
                  sph_prj='C:/Users/fan/R4Econ/',
                  spn_prj_bookdown_yml='_bookdown.yml',
                  spn_prj_readme_toc='README_toc.md',
                  ls_st_ignore=['index.Rmd']):
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
    """

    spn_readme = sph_prj + spn_prj_readme_toc
    f_core = open(spn_readme, "w")

    spn_yml = sph_prj + spn_prj_bookdown_yml
    with open(spn_yml, 'r') as f:
        ob_book_yml = yaml.load(f)

    ls_st_rmd_files = ob_book_yml['rmd_files']

    sfc_main = '_main.Rmd'
    ctr_chapter = 0
    ctr_section = 0
    ctr_subsection = 0

    for sfc in ls_st_rmd_files:

        if sfc in ls_st_ignore:
            print('ignore')

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
            f_core.write(st_text_out)

        else:

            # Load RMD front matter and summarize
            ctr_subsection = ctr_subsection + 1
            st_head_link, ls_desc_out, ls_code_out = \
                rmdparse.fs_rmd_yml_parse(
                    sfc_prj=sfc_prj, sph_prj=sph_prj, spn_prj_rmd=sfc)

            # write to file file title and main
            st_text_out = str(ctr_subsection) + '. ' + st_head_link + '\n'
            f_core.write(st_text_out)

            # write to file file desc
            for st_desc in ls_desc_out:
                f_core.write(st_desc + '\n')
            for st_code in ls_code_out:
                f_core.write(st_code + '\n')

    # ls_front_keys = ob_book_yml.keys()
    # print(ls_front_keys)

    f_core.close()


if __name__ == '__main__':
    # sfc_prj = 'R4Econ'
    # sph_prj = 'C:/Users/fan/R4Econ/'
    # spn_prj_bookdown_yml = '_bookdown.yml'
    # spn_prj_readme_toc = 'README_toc_two.md'
    #
    # fs_yml2readme(sfc_prj=sfc_prj,
    #               sph_prj=sph_prj,
    #               spn_prj_bookdown_yml=spn_prj_bookdown_yml,
    #               spn_prj_readme_toc=spn_prj_readme_toc)
    fs_yml2readme()
