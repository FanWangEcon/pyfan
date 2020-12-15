"""
The :mod:`pyfan.stats.markov.transprobcheck` checks markov transition row sums.

A markov transition matrix where each row does not
sum up to 1 due to simulation errors. Check if the gap between 1 and the row
values are too big, and then normalize.

import pyfan.stats.markov.transprobcheck as pyfan_stats_transprobcheck

Includes method :func:`markov_trans_prob_check` and :func:`markov_condi_prob2one`.
"""

import os
import numpy as np
from pathlib import Path
import pyfan.util.path.getfiles as getfiles
import pyfan.amto.numeric.round as pyfan_amto_round


def tab_txt2tex_f2f(spt_root="", st_rglob='tab_*_fmd.md', **kwargs):
    # 1. Find txt files in folder
    ls_spn_found_fmd_txt = getfiles.fp_search_rglob(spt_root=spt_root, st_rglob=st_rglob)

    # 2. Loop over all FMD text files
    ls_spn_generated_tex = []
    for spn_found_fmd_txt in ls_spn_found_fmd_txt:

        # 3. Open file and read in all lines
        fl_txt_reg_contents = open(spn_found_fmd_txt)
        ls_st_txt_regs = fl_txt_reg_contents.readlines()
        fl_txt_reg_contents.close()

        # 4. Convert FMD lines to TEX table lines
        ls_st_tex_returns = tab_txt2tex(ls_st_txt_regs, **kwargs)

        # 5. Construct TEX File name same name, different suffix, TXT to TEX
        snm_file_name_stem_tex = Path(spn_found_fmd_txt).stem + '.tex'
        path_no_file, __ = os.path.split(spn_found_fmd_txt)
        spn_tex_file = os.path.join(path_no_file, snm_file_name_stem_tex)
        ls_spn_generated_tex.append(spn_tex_file)

        # 6. Write to tex
        fl_tex = open(spn_tex_file, "w")
        # Read list of strings line by line and write to tex
        for st_tex_return in ls_st_tex_returns:
            fl_tex.write(st_tex_return)
        # close tex file
        fl_tex.close()

    return ls_spn_generated_tex


def tab_txt2tex(ls_st_txt_regs,
                it_col_count=6, fl_adj_box_maxwidth=1,
                it_or_dc_round_decimal=2,
                fl_col_label_width_cm=5, fl_col_coef_width_cm=2,
                fl_indent_pound1_mm=0, fl_indent_pound2_mm=0, fl_indent_pound3_mm=6):
    """Markov conditional transition probability check

    Parameters
    ----------
    it_col_count : int
        Number of latex table columns
    fl_atol_per_row : `float`, optional
        Tolerance for the difference between 1 and each row sum
    fl_atol_avg_row : `float`, optional
        Tolerance for the difference between 1 and average of row sums
    fl_sum_to_match : `float`, optional
        This should be 1, unless the function is not used to handle transition matrixes
    Returns
    -------
    list string formated to tex to return
        A tuple of booleans, the fiit element is if satisfies the overall criteria. Second
        is if satisifes the per_row condition. Third if satisfies the average criteria.

    Examples
    --------
    # >>> mt_ar1_trans = np.array([[0.4334, 0.5183, 0.0454],
    # >>>                          [0.2624, 0.5967, 0.1245],
    # >>>                          [0.1673, 0.5918, 0.2005]])
    # >>> bl_ar1_sum_pass, bl_per_row_pass, bl_avg_row_pass = markov_trans_prob_check(mt_ar1_trans)
    # >>> print(f'{bl_ar1_sum_pass=}')
    # bl_ar1_sum_pass=False
    # >>> print(f'{bl_per_row_pass=}')
    # bl_per_row_pass=False
    # >>> print(f'{bl_avg_row_pass=}')
    bl_avg_row_pass=False
    """

    # Return list
    ls_st_tex_returns = []
    # Parse lines one by one
    for st_txt_regq_line in ls_st_txt_regs:

        # delete linebreak at end of line
        st_txt_regq_line = st_txt_regq_line.replace("\n", "")

        # Check start of line for special characters
        st_N2_char = st_txt_regq_line[0:2]
        st_N3_char = st_txt_regq_line[0:3]
        st_N4_char = st_txt_regq_line[0:4]
        st_N5_char = st_txt_regq_line[0:5]

        # Conditional processing
        st_text_out = ''
        if st_N5_char == '###> ':
            # Variable heading, with 3rd level indent, to be connected with coefficients etc
            st_txt_regq_line = st_txt_regq_line.replace("###> ", "")
            st_text_out = "\hspace*{" + str(fl_indent_pound3_mm) + "mm}" + st_txt_regq_line
        elif st_N4_char == '##> ':
            # Variable heading, with 2nd level indent, to be connected with coefficients etc
            st_txt_regq_line = st_txt_regq_line.replace("##> ", "")
            st_text_out = "\hspace*{" + str(fl_indent_pound2_mm) + "mm}" + st_txt_regq_line
        elif st_N4_char == '### ':
            # Group heading, with 3nd level indent
            st_txt_regq_line = st_txt_regq_line.replace("### ", "")
            st_text_out = "\\addlinespace\n"
            st_text_out = st_text_out + "\multicolumn{" + str(it_col_count) + "}{l}{\hspace*{" + str(
                fl_indent_pound3_mm) + "mm}\\textit{" + st_txt_regq_line + "}}\\\\\n"
            st_text_out = st_text_out + '\\addlinespace\n'
        elif st_N3_char == '## ':
            # Group heading, with 2nd level indent
            st_txt_regq_line = st_txt_regq_line.replace("## ", "")
            st_text_out = "\\addlinespace\n"
            st_text_out = st_text_out + "\multicolumn{" + str(it_col_count) + "}{l}{\hspace*{" + str(
                fl_indent_pound2_mm) + "mm}" + st_txt_regq_line + "}\\\\\n"
            st_text_out = st_text_out + '\\addlinespace\n'
        elif st_N2_char == '# ':
            # title line and initialize file lines
            st_txt_regq_line = st_txt_regq_line.replace("# ", "")
            st_text_out = st_text_out + "\\begin{table}[htbp]\n"
            st_text_out = st_text_out + "\centering\n"
            st_text_out = st_text_out + "\caption{\hspace*{" + str(
                fl_indent_pound1_mm) + "mm}" + st_txt_regq_line + "}\n"
            st_text_out = st_text_out + "\\begin{adjustbox}{max width=" + str(
                fl_adj_box_maxwidth) + "\\textwidth}\n"
            st_text_out = st_text_out + \
                          "\\begin{tabular}{m{" + str(fl_col_label_width_cm) + "cm}" \
                                                                               "*{" + str(
                it_col_count - 1) + "}{>{\centering\\arraybackslash}" \
                                    "m{" + str(fl_col_coef_width_cm) + "cm}}}\n"

        elif st_N2_char == '> ':
            # latex code line, include as it appears
            st_txt_regq_line = st_txt_regq_line.replace("> ", "")
            st_text_out = st_txt_regq_line + "\n"
        else:
            # Assume no headline/code row is comma separated
            ls_st_estimates = st_txt_regq_line.split(",")

            # Loop over each value separated by commas
            for it_esti_ctr, st_esti in enumerate(ls_st_estimates):

                # Default update is to keep current
                st_esti_update = st_esti

                # If estimates, might have stars, first check star count
                # delete stars, for numeric conversion and rounding
                it_star_count = np.nan
                if "***" in st_esti:
                    it_star_count = 3
                    st_esti = st_esti.replace("***", "")
                elif "**" in st_esti:
                    it_star_count = 2
                    st_esti = st_esti.replace("**", "")
                elif "*" in st_esti:
                    it_star_count = 1
                    st_esti = st_esti.replace("*", "")
                else:
                    it_star_count = 0

                # Check if has brakcets
                it_bracket_count = np.nan
                if "(" in st_esti:
                    it_bracket_count = 1
                    st_esti = st_esti.replace("(", "")
                    if ")" in st_esti:
                        it_bracket_count = 2
                        st_esti = st_esti.replace(")", "")

                # Decimal Rounding
                try:
                    # numerical
                    # fl_esti_rounded = round(float(st_esti), it_round_decimal)
                    fl_esti_rounded = float(st_esti)
                    st_esti_rounded = pyfan_amto_round.ff_decimal_rounder(
                        ls_fl_num2format=[fl_esti_rounded],
                        it_or_dc_round_decimal=it_or_dc_round_decimal)[0]
                except Exception:
                    # Might be non-numeric
                    st_esti_rounded = st_esti

                # Conditional Processing for Point Estimates and SE
                if it_bracket_count is np.nan:

                    # A. No brackets, these are point estimates
                    # Convert Estimate
                    st_esti_starred = st_esti_rounded
                    if it_star_count == 3:
                        st_esti_starred = st_esti_rounded + "\sym{***}"
                    elif it_star_count == 2:
                        st_esti_starred = st_esti_rounded + "\sym{**}"
                    elif it_star_count == 1:
                        st_esti_starred = st_esti_rounded + "\sym{*}"

                    st_esti_update = st_esti_starred

                else:
                    # B. brackets, these are standard errors

                    if it_bracket_count == 2:
                        st_esti_update = "(" + st_esti_rounded + ")"
                    else:
                        raise TypeError(f'{ls_st_estimates=} and {st_esti=}, missing bracket')

                # Update List
                ls_st_estimates[it_esti_ctr] = st_esti_update

            # Flatten comman
            st_text_out = ' & '.join(ls_st_estimates)
            if len(st_text_out) > 0:
                # add ampersand front
                st_text_out = ' & ' + st_text_out + '\\\\\n\\addlinespace\n'

            # st_text_out = st_txt_regq_line
            # st_text_out = st_text_out.replace("***", "\sym{+++}")
            # st_text_out = st_text_out.replace("**", "\sym{==}")
            # st_text_out = st_text_out.replace("*", "\sym{*}")
            # st_text_out = st_text_out.replace("\sym{==}", "\sym{**}")
            # st_text_out = st_text_out.replace("\sym{+++}", "\sym{***}")

        if len(st_text_out) > 0:
            ls_st_tex_returns.append(st_text_out)

    # close connection
    ls_st_tex_returns.append("\\end{tabular}\n")
    ls_st_tex_returns.append("\\end{adjustbox}\n")
    ls_st_tex_returns.append("\\end{table}\n")

    # return
    return ls_st_tex_returns


if __name__ == '__main__':
    spt_root = 'C:/Users/fan/Box/Pollution and inequality/drafts/paper_final_tab/'

    ls_st_rglob = ['table_main1_fmd.md', 'table_main1_fmd_long.md']
    it_or_dc_round_decimal_tab1 = {100: 2, float("inf"): 0}
    for st_rglob in ls_st_rglob:
        tab_txt2tex_f2f(spt_root=spt_root, st_rglob=st_rglob,
                        it_col_count=8,
                        fl_col_coef_width_cm=1.5, fl_col_label_width_cm=7.75,
                        it_or_dc_round_decimal=it_or_dc_round_decimal_tab1,
                        fl_adj_box_maxwidth=1.1)

    ls_st_rglob = ['table_main2_fmd.md']
    for st_rglob in ls_st_rglob:
        tab_txt2tex_f2f(spt_root=spt_root, st_rglob=st_rglob,
                        it_col_count=7, fl_col_label_width_cm=2.5,
                        it_or_dc_round_decimal=2)

    ls_st_rglob = ['table_main4_fmd.md', 'table_main5_fmd.md',
                   'table_app2_fmd.md', 'table_app3_fmd.md']
    for st_rglob in ls_st_rglob:
        tab_txt2tex_f2f(spt_root=spt_root, st_rglob=st_rglob, it_col_count=6, fl_col_label_width_cm=5.2)

    ls_st_rglob = ['table_main3_fmd.md', 'table_app1_fmd.md']
    for st_rglob in ls_st_rglob:
        tab_txt2tex_f2f(spt_root=spt_root, st_rglob=st_rglob, it_col_count=5, fl_col_label_width_cm=5.2)
