"""Fan Rmd Fronter Matter Core Parser

In mine Rmd files front matter, there are some special parameters that
provide summaries for the key contents in the code, and also provide
key programs and dependencies that were used. The information can be parsed
to string lists. The special strings are meant to be used with a special
README.md github pages file. The goal is to automatically gather meta-data
across RMD files within folders in a package to prepare data needed to provide
a detailed table of content type contents needed for a README.md file.
"""

import frontmatter
import os


# sfc_prj='R4Econ'
# sph_prj='C:/Users/fan/R4Econ'
# spn_prj_rmd='/summarize/aggregate/fs_group_unique_agg.Rmd'
# sph_gitpages_root='https://fanwangecon.github.io/'
# sph_github_root='https://github.com/FanWangEcon/'
# sph_branch='/master'
# sph_pdf='/htmlpdfr'
# sph_html='/htmlpdfr'
# sph_r='/htmlpdfr'

def fs_rmd_yml_parse(sfc_prj='R4Econ',
                     sph_prj='C:/Users/fan/R4Econ',
                     spn_prj_rmd='/summarize/aggregate/fs_group_unique_agg.Rmd',
                     sph_gitpages_root='https://fanwangecon.github.io/',
                     sph_github_root='https://github.com/FanWangEcon/',
                     sph_branch='/master',
                     sph_pdf='htmlpdfr',
                     sph_html='htmlpdfr',
                     sph_r='htmlpdfr'):
    """Parse Yaml Frontmatter to get list of paths, summaries, dependencies

    Parameters
    ----------
    sfc_prj : string
        The git project name
    sph_prj : string
        the local path to the git project
    spn_prj_rmd : string
        the path (within project) to the Rmd file
    sph_gitpages_root : string
        github pages site url root
    sph_github_root : string
        github project page url
    sph_branch : string
        which branch
    sph_pdf : string
        subfolder to store pdf files in the rmd folder
    sph_html : string
        subfolder to store html files in the rmd folder
    sph_r : string
        subfolder to store r files in the rmd folder
    """

    # 1. [Count Unique Groups and Mean within Groups](
    # https://fanwangecon.github.io/R4Econ/summarize/aggregate/fs_group_unique_agg.html): r \| ref \| [**rmd**](
    # https://github.com/FanWangEcon/R4Econ/blob/master/summarize/aggregate/fs_group_unique_agg.Rmd ) \| [**pdf**](
    # https://github.com/FanWangEcon/R4Econ/blob/master/summarize/aggregate/fs_group_unique_agg.pdf) \| [**html**](
    # https://fanwangecon.github.io/R4Econ/summarize/aggregate/fs_group_unique_agg.html)

    spn_rmd = sph_prj + spn_prj_rmd
    ob_yml_rmd = frontmatter.load(spn_rmd)
    ls_front_keys = ob_yml_rmd.keys()

    # Construct RMD R PDF HTML Path
    sfc_rmd_file = os.path.basename(spn_rmd)
    sfc_file_base = os.path.splitext(sfc_rmd_file)[0]
    spt_rmd_path = os.path.dirname(spn_prj_rmd)
    if 'titleshort' in ls_front_keys:
        st_title = ob_yml_rmd['titleshort']
    elif 'title' in ls_front_keys:
        st_title = ob_yml_rmd['title']
    else:
        st_title = sfc_file_base

    sph_source_blob_root = sph_github_root + sfc_prj + '/blob' + sph_branch + '/' + spt_rmd_path + '/'
    sph_rmd_pdf = sph_source_blob_root + sph_pdf + '/' + sfc_file_base + '.pdf'
    sph_rmd_r = sph_source_blob_root + sph_r + '/' + sfc_file_base + '.R'
    sph_rmd_rmd = sph_source_blob_root + '/' + sfc_file_base + '.Rmd'

    sph_source_web_root = sph_gitpages_root + sfc_prj + '/' + spt_rmd_path + '/'
    sph_rmd_html = sph_source_web_root + sph_html + '/' + sfc_file_base + '.html'

    st_head_link = '[' + st_title + '](' + sph_rmd_html + '):'
    st_head_link = st_head_link + ' [**rmd**](' + sph_rmd_rmd + ')'
    st_head_link = st_head_link + ' \\| [**r**](' + sph_rmd_r + ')'
    st_head_link = st_head_link + ' \\| [**pdf**](' + sph_rmd_pdf + ')'
    st_head_link = st_head_link + ' \\| [**html**](' + sph_rmd_html + ')'

    # Function Details Bullet Points
    if 'description' in ls_front_keys:
        st_desc = ob_yml_rmd['description']
        ls_st_desc = st_desc.split('\n', 4)[:-1]
        ls_desc_out = [None] * len(ls_st_desc)
        for ctr in range(0, len(ls_st_desc)):
            st_ful = '\t+ ' + ls_st_desc[ctr]
            ls_desc_out[ctr] = st_ful
    else:
        ls_desc_out = []

    # Construct R Functions used string
    if 'core' in ls_front_keys:
        ls_summary = ob_yml_rmd['core']
        ls_code_out = [None] * len(ls_summary)
        for ctr in range(0, len(ls_summary)):
            st_str = '**' + ls_summary[ctr]['package'] + '**'
            st_end = '*' + " + ".join(ls_summary[ctr]['code'].split('\n')[:-1]) + '*'
            st_ful = '\t+ ' + st_str + ': ' + st_end
            ls_code_out[ctr] = st_ful
    else:
        ls_code_out = []

    # print(st_head_link)
    # print(ls_desc_out)
    # print(ls_code_out)

    return st_head_link, ls_desc_out, ls_code_out


if __name__ == '__main__':
    spn_prj_rmd = '/summarize/aggregate/fs_group_summ_wide.Rmd'
    spn_prj_rmd = '/summarize/aggregate/fs_group_unique_agg.Rmd'
    st_head_link_a, ls_desc_out_a, ls_code_out_a = fs_rmd_yml_parse(spn_prj_rmd=spn_prj_rmd)
    print(st_head_link_a)
    print(ls_desc_out_a)
    print(ls_code_out_a)
