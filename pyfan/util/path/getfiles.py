from pathlib import Path


def fp_search_rglob(spt_root="../",
                    st_rglob='*.py',
                    ls_srt_subfolders=None,
                    verbose=False,
                    ):
    """Searches for files with search string in a list of folders

    Parameters
    ----------
    spt_root: string
        root folder to search in
    st_rglob: string
        search for files with this rglob string
    ls_srt_subfolders: :obj:`list` of :obj:`str`
        a list of subfolders of the spt_root to search in
    verbose: bool
        print details

    Returns
    -------
    :obj:`list` of :obj:`str`
        A list of file names

    Examples
    --------

    >>> ls_spn = fp_search_rglob(spt_root="../",
    >>>                          ls_srt_subfolders=['rmd', 'pdf'],
    >>>                          st_rglob = '*d*.py')
    [WindowsPath('../rmd/bookdownparse.py'), WindowsPath('../rmd/mattexmd.py'), WindowsPath('../rmd/rmdparse.py'), WindowsPath('../pdf/pdfgen.py')]

    """

    # Directories to search in
    if ls_srt_subfolders is None:
        # ls_srt_subfolders = ['calconevar/', 'derivative/', 'derivative_application/',
        #                      'matrix_basics/',
        #                      'opti_firm_constrained/', 'opti_hh_constrained_brsv/',
        #                      'opti_hh_constrained_brsv_inequality/']
        # ls_srt_subfolders = ['matrix_basics/']
        ls_spt = [spt_root]
    else:
        ls_spt = [spt_root + srt_subf for srt_subf in ls_srt_subfolders]

    if verbose:
        print(ls_spt)

    # get file names
    ls_spn_found_tex = [spn_file for spt_srh in ls_spt
                        for spn_file in Path(spt_srh).rglob(st_rglob)]
    if verbose:
        print(ls_spn_found_tex)

    return ls_spn_found_tex


if __name__ == '__main__':
    spt_root_u = "../"
    ls_srt_subfolders_u = ['rmd', 'pdf']
    st_rglob_u = '*d*.py'
    verbose_u = False
    ls_spn = fp_search_rglob(spt_root=spt_root_u, ls_srt_subfolders=ls_srt_subfolders_u,
                             st_rglob=st_rglob_u, verbose=verbose_u)
    print(ls_spn)

