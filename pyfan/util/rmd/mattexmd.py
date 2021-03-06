"""Convert matlab MLX files to MD and RMD files
The :mod:`pyfan.util.rmd.mattexmd` generates md and rmd file from tex file converted from matlab mlx.

Use matlab's own functions to export a MLX file to tex. Clean some elements of this text file, use
pandoc to convert to MD. Then resave the md file as a RMD file by combining yml info from a preamble.yml file
that is in the folder.

Includes method :func:`fp_md2rmd`, :func:`fp_mlxtex2md`
"""

from pathlib import Path
import subprocess
import os
import yaml
import pyfan.util.path.getfiles as getfiles


def fp_md2rmd(spt_root="C:/Users/fan/Math4Econ/",
              ls_srt_subfolders=['calconevar/'],
              snm_folder_yml='preamble.yml',
              st_yml_file_key='file',
              st_rglob_md='*.md', verbose=False):
    """Generate RMD from MD with YAML Header

    In each folder, there is a prior preamble.yaml for all files in folder.
    There are md files generated by the fp_mlxtex2md function, this file stacks the yaml
    header on top of the md after searching for the yml header with the no suffix
    file name of the md file, which is the search key in the yaml.

    Parameters
    ----------
    spt_root : string
        The root folder
    ls_srt_subfolders : :obj:`list` of :obj:`str`
        List of subfolders to search in
    snm_folder_yml: string
        name of the file containing all rmd yaml header under spt_root
    st_yml_file_key: string
        the key in the yaml header snm_folder_yml with file names no suffix
    st_rglob_md : string
        md files search string rglob
    verbose : bool
        print extra

    Returns
    -------
    None
        nothing is returned, mlx generated tex files updates, and pandoc md generated

    Examples
    --------
    >>> fp_md2rmd(spt_root="C:/Users/fan/M4Econ/amto/",
    ...          ls_srt_subfolders=['array/'],
    ...          snm_folder_yml='preamble.yml',
    ...          st_yml_file_key='file',
    ...          st_rglob_md='fs_slicing.md', verbose=False)
    """

    ls_spn_found_md = \
        getfiles.fp_search_rglob(spt_root=spt_root, ls_srt_subfolders=ls_srt_subfolders,
                                 st_rglob=st_rglob_md, verbose=verbose)

    for spn_md in ls_spn_found_md:
        if verbose:
            print(spn_md)

        # spn_md = "C:/Users/fan/Math4Econ/matrix_basics/matrix_matlab.md"
        sna_file = Path(spn_md).stem
        spn_rmd = os.path.splitext(spn_md)[0] + '.Rmd'
        spn_yml = os.path.split(spn_md)[0] + '/' + snm_folder_yml

        # Open existing md file
        fl_md = open(spn_md)
        tx_fl_md = fl_md.read()

        # Link String
        st_link_line_1 = "**back to** [**Fan**](https://fanwangecon.github.io)**'s** [**Intro Math\n"
        st_link_line_2 = "for Econ**](https://fanwangecon.github.io/Math4Econ/)**,** [**Matlab\n"
        st_link_line_3 = "Examples**](https://fanwangecon.github.io/M4Econ/)**, or**\n"
        st_link_line_4 = "[**MEconTools**](https://fanwangecon.github.io/MEconTools/)\n"
        st_link_line_5 = "**Repositories**\n"
        st_link_lines = st_link_line_1 + st_link_line_2 + st_link_line_3 + st_link_line_4 + st_link_line_5

        st_link_rep_1 = "```{r global_options, include = FALSE}\ntry(source('../.Rprofile'))\n```\n"
        st_link_rep_2 = "\n`r text_shared_preamble_one`\n`r text_shared_preamble_two`\n`r text_shared_preamble_thr`\n"

        # replace md elements
        ls_st_old = ['![image]', '.png)', st_link_line_1, st_link_line_2, st_link_line_3, st_link_line_4,
                     st_link_line_5]
        ls_st_new = ['![]', '.png){width=500px}', st_link_rep_1, st_link_rep_2, '', '', '']

        # zip and loop and replace
        for old, new in zip(ls_st_old, ls_st_new):
            tx_fl_md = tx_fl_md.replace(old, new)
        if verbose:
            print(tx_fl_md)

        # Open and get yml component
        # Assume that there is a yml file under the immediate path
        fl_yml = open(spn_yml)
        ls_dict_yml = yaml.load(fl_yml, Loader=yaml.BaseLoader)
        if verbose:
            print(ls_dict_yml)

        # From the file with all folder file yamls, find the file specific yaml
        ls_dict_selected = [dict_yml for dict_yml in ls_dict_yml
                            if dict_yml[st_yml_file_key] in [sna_file]]

        # Put Overall String Structure Together
        st_rmd_yml = yaml.dump(ls_dict_selected[0])

        # Open new RMD file
        fl_rmd = open(spn_rmd, 'w')
        fl_rmd.write('---\n')
        fl_rmd.write(st_rmd_yml)
        fl_rmd.write('---\n\n')
        fl_rmd.write(tx_fl_md)

        # closing
        fl_md.close()
        fl_yml.close()
        fl_rmd.close()
        # print


def fp_mlxtex2md(spt_root="C:/Users/fan/Math4Econ/",
                 ls_srt_subfolders=['calconevar/'],
                 st_rglob_tex='*.tex', verbose=False):
    """Edit and replace MLX based tex and convert to markdown

    Several mlx auto converted tex elements need to be constructed, otherwise
    the md file would not work. Importantly, convert how images are stored to
    aggregate subfolder. Which relies on movefiles.py to generate to put
    in the image folder structure as specified here which is under an
    aggregate img folder.

    Parameters
    ----------
    spt_root : string
        The root folder
    ls_srt_subfolders : :obj:`list` of :obj:`str`
        List of subfolders to search in
    st_rglob_tex : string
        tex files search string rglob
    verbose : bool
        print extra

    Returns
    -------
    None
        nothing is returned, mlx generated tex files updates, and pandoc md generated

    Examples
    --------
    >>> fp_mlxtex2md(spt_root='C:/Users/fan/Math4Econ/matrix_application/',
    ...              ls_srt_subfolders=None, st_rglob_tex='twogoods.tex', verbose=True)
    >>> fp_mlxtex2md(spt_root='C:/Users/fan/M4Econ/amto/array/',
    ...              ls_srt_subfolders=None, st_rglob_tex='fs_slicing.tex', verbose=True)
    """

    # spt_root = "C:/Users/fan/Math4Econ/"
    # ls_srt_subfolders = ['calconevar/', 'derivative/', 'derivative_application/',
    #                      'matrix_basics/',
    #                      'opti_firm_constrained/', 'opti_hh_constrained_brsv/',
    #                      'opti_hh_constrained_brsv_inequality/']
    # ls_srt_subfolders = ['matrix_basics/']
    # st_rglob_tex = '*.tex'
    ls_spn_found_tex = \
        getfiles.fp_search_rglob(spt_root=spt_root, ls_srt_subfolders=ls_srt_subfolders,
                                 st_rglob=st_rglob_tex, verbose=verbose)

    for spn_found_tex in ls_spn_found_tex:
        if verbose:
            print(spn_found_tex)
        fl_tex_contents = open(spn_found_tex)
        stf_tex_contents = fl_tex_contents.read()

        # file image folder
        sna_file = Path(spn_found_tex).stem
        fl_tex_contents.close()
        # --listing
        # define new and old
        ls_st_old = ['\\begin{matlabcode}',
                     '\\end{matlabcode}',
                     'matlaboutput',
                     'matlabtitle', 'matlabheading',
                     '[width=\\maxwidth{56.196688409433015em}]{']
        ls_st_new = ['\\begin{lstlisting}',
                     '\\end{lstlisting}',
                     'lstlisting',
                     'subsection', 'subsubsection',
                     '{img/' + sna_file + '_images/']

        # zip and loop and replace
        for old, new in zip(ls_st_old, ls_st_new):
            stf_tex_contents = stf_tex_contents.replace(old, new)
        if verbose:
            print(stf_tex_contents)
        # Open new file
        fl_tex_contents = open(spn_found_tex, 'w')
        fl_tex_contents.write(stf_tex_contents)

        # convert from tex to md
        path_no_suffix = os.path.splitext(spn_found_tex)[0]
        spn_md = path_no_suffix + '.md'
        # print(spn_found_tex)
        # print(spn_found_tex)
        if verbose:
            print(str(['pandoc', '-s', str(spn_found_tex), '-o', str(spn_md)]))

        # atx - headers: so convert all to pounds
        subprocess.Popen(['pandoc',
                          '--atx-headers',
                          '-s', str(spn_found_tex), '-o', str(spn_md)])
        if verbose:
            print(spn_md)

# if __name__ == '__main__':
#     # spt_root_u = "C:/Users/fan/Math4Econ/"
#     # ls_srt_subfolders_u = ['calconevar/', 'derivative/', 'derivative_application/',
#     #                        'matrix_basics/',
#     #                        'opti_firm_constrained/', 'opti_hh_constrained_brsv/',
#     #                        'opti_hh_constrained_brsv_inequality/']
#     # ls_srt_subfolders_u = ['matrix_basics/', 'matrix_application/']
#     # st_rglob_tex_u = '*.tex'
#     # st_rglob_md_u = '*.md'
#     # verbose_u = False
#     #
#     # fp_mlxtex2md(spt_root=spt_root_u, ls_srt_subfolders=ls_srt_subfolders_u,
#     #              st_rglob_tex=st_rglob_tex_u, verbose=verbose_u)
#     #
#     # fp_md2rmd(spt_root=spt_root_u, ls_srt_subfolders=ls_srt_subfolders_u,
#     #           st_rglob_md=st_rglob_md_u, verbose=verbose_u)
#     # from subprocess import Popen, PIPE
#     #
#     # # python -c "from pyfan.util.rmd.mattexmd import fp_mlxtex2md; fp_mlxtex2md(spt_root='C:/Users/fan/Math4Econ/matrix_application/', ls_srt_subfolders=None, st_rglob_tex='twogoods.tex', verbose=True)"
#     #
#     # spg_py_run = "from pyfan.util.rmd.mattexmd import fp_mlxtex2md; fp_mlxtex2md(spt_root='C:/Users/fan/Math4Econ/matrix_application/', ls_srt_subfolders=None, st_rglob_tex='twogoods.tex', verbose=True)"
#     # # spg_py_run = "1+1"
#     #
#     # cmd_popen = Popen(["python", "-c",
#     #                    "\"" + spg_py_run + "\""],
#     #                   stdin=PIPE, stdout=PIPE, stderr=PIPE)
#     # print(cmd_popen)
#     # output, err = cmd_popen.communicate()
#     # print(output.decode('utf-8'))
#     # print(err.decode('utf-8'))
#
#     # fp_mlxtex2md(spt_root='C:/Users/fan/M4Econ/amto/array/',
#     #              ls_srt_subfolders=None,
#     #              st_rglob_tex='fs_slicing.tex',
#     #              verbose=True)
#
#     fp_md2rmd(spt_root="C:/Users/fan/M4Econ/amto/",
#               ls_srt_subfolders=['array/'],
#               snm_folder_yml='preamble.yml',
#               st_yml_file_key='file',
#               st_rglob_md='fs_slicing.md', verbose=False)
