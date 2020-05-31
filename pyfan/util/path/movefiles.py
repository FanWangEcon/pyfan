import pathlib
import os
import shutil
from distutils.dir_util import copy_tree


def fp_agg_move_subfiles(spt_root_src="C:/Users/fan/pyfan/vig/support/inout/_folder/fd/faa/",
                         st_srt_srh="_images",
                         st_fle_srh="*",
                         srt_agg='img',
                         ls_srt_dest=['C:/Users/fan/pyfan/vig/support/inout/_folder/fd/faa/',
                                      'C:/Users/fan/pyfan/vig/support/inout/_folder/'],
                         bl_delete_src=True,
                         bl_test=True,
                         verbose=False):
    """Aggregate and Move a Collection of Non-empty Folders

    A program (forexample mlx to tex conversion) creates in a folder a number
    of subfolder that stores images. Aggregate all the various image folders into
    a common image folder. And then move this common image folder to other destinations
    in order to flexibly generate aggregation files with common path that rely on
    images from various subfolders.

    Parameters
    ----------
    spt_root_src: string
        root folder where subfolders are contained
    st_srt_srh: string
        gather subfolder names that contain this string
    st_fle_srh: string
        search in subfolders for files whose name contain string
    srt_agg: string
        name of subfolder where found folders are aggregated at
    ls_srt_dest: :obj:`list` of :obj:`str`
        list of folder paths to move aggregate subfolders over to
    bl_delete_src: bool
        delete folders at existing locations
    bl_test: bool
        test by searching for paths dest and src, do not move
    verbose: bool
        print details

    Returns
    -------
    None
        nothing is returned

    Examples
    --------

    >>> fp_agg_move_subfiles(spt_root_src="C:/Users/fan/Math4Econ/matrix_application/",
    >>> 					 st_srt_srh="_images",
    >>> 					 st_fle_srh="*.png",
    >>> 					 srt_agg='img',
    >>> 					 ls_srt_dest=["C:/Users/fan/Math4Econ/"],
    >>> 					 bl_delete_src=False,
    >>> 					 bl_test=False,
    >>> 					 verbose=False)

    """

    # 1. Gather Folders
    ls_ls_srt_found = [[spt_root_src + spt, spt]
                       for spt in os.listdir(spt_root_src)
                       if ((st_srt_srh in spt)
                           and
                           (len([spn for spn
                                 in pathlib.Path(spt_root_src + spt).rglob(st_fle_srh)]) > 0))]
    if verbose:
        print(ls_ls_srt_found)

    # 2 Loop over destination folders, loop over source folders
    for srt in ls_srt_dest:

        # Move each folder over
        for ls_srt_found in ls_ls_srt_found:
            # Paths
            srt_source = ls_srt_found[0]
            srt_dest_subfolder = ls_srt_found[1]
            srt_dest = os.path.join(srt, srt_agg, srt_dest_subfolder)

            # print if verbose or testing
            if verbose or bl_test:
                print('srt_source:' + srt_source + ', srt_dest:' + srt_dest)

            # if not testing
            if not bl_test:
                # dest folders
                pathlib.Path(srt_dest).mkdir(parents=True, exist_ok=True)
                # move
                copy_tree(srt_source, srt_dest)

    # 3. Delete Sources
    if bl_delete_src and not bl_test:
        for ls_srt_found in ls_ls_srt_found:
            shutil.rmtree(ls_srt_found[0])


if __name__ == '__main__':
    # spt_root_src_u = "C:/Users/fan/Math4Econ/matrix_application/"
    # st_srt_srh_u = "_images"
    # st_fle_srh_u = "*.png"
    # srt_agg_u = 'img'
    # ls_srt_dest_u = [spt_root_src_u,
    #                  "C:/Users/fan/Math4Econ/"]
    # bl_delete_src_u = False
    # bl_test_u = False
    # verbose_u = False
    # fp_agg_move_subfiles(spt_root_src=spt_root_src_u,
    #                      st_srt_srh=st_srt_srh_u,
    #                      st_fle_srh=st_fle_srh_u,
    #                      srt_agg=srt_agg_u,
    #                      ls_srt_dest=ls_srt_dest_u,
    #                      bl_delete_src=bl_delete_src_u,
    #                      bl_test=bl_test_u,
    #                      verbose=verbose_u)

    spt_root_src_u = "C:/Users/fan/Math4Econ/matrix_application/"
    st_srt_srh_u = "twogoods_images"
    st_fle_srh_u = "*.png"
    srt_agg_u = 'img'
    ls_srt_dest_u = ['C:/Users/fan/Math4Econ/matrix_application/', 'C:/Users/fan/Math4Econ/']
    bl_delete_src_u = True
    bl_test_u = False
    verbose_u = True
    fp_agg_move_subfiles(spt_root_src=spt_root_src_u,
                         st_srt_srh=st_srt_srh_u,
                         st_fle_srh=st_fle_srh_u,
                         srt_agg=srt_agg_u,
                         ls_srt_dest=ls_srt_dest_u,
                         bl_delete_src=bl_delete_src_u,
                         bl_test=bl_test_u,
                         verbose=verbose_u)
