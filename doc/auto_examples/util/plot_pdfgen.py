# -*- coding: utf-8 -*-
"""
Generate PDFs and Clean
========================================================================

In this example, we generate PDFs in one location from tex files in possibly
various other locations, and clean.

"""

# Author: Fan Wang (fanwangecon.github.io)
import pyfan.util.pdf.pdfgen as pyfan_pdfgen
import pprint
import matplotlib.pyplot as plt
import textwrap
import json

# %%
# Generate PDF for one specific file and clean afterwards
# -------------------------------------------------------

# spt_loc = 'C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/Tex4Econ/_other/equation/'
spt_loc = 'G:/Dropbox (UH-ECON)/repos/Tex4Econ/_other/equation/'
spt_loc_output = 'C:/Users/fan/Documents/'
spn_file = 'cases.tex'
spn_pdf_exe = 'C:/texlive/2020/bin/win32/pdflatex.exe'
dc_tex_pdf_a = pyfan_pdfgen.ff_pdf_gen_clean(ls_spt_srh=[spt_loc], spt_out=spt_loc_output,
                                             spn_pdf_exe=spn_pdf_exe, ls_st_contain=[spn_file],
                                             bl_clean=True)
print(dc_tex_pdf_a)

# %%
# Generate PDF from all tex files in all subfolders of a main folder, output PDF store in one location
# ----------------------------------------------------------------------------------------------------
#
# 1. spt_loc_search_root: Tex Search folder
# 2. spt_loc_output: only consider files with this in name
# 3. st_search_string: include in one of the element in list
# 4. ls_st_ignore: ignore files with this in name
# 5. PDF Destination Folder: same root path earlier folder to store possibly
#

# spt_loc_search_root = 'C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/Tex4Econ/_other/'
spt_loc_search_root = 'G:/Dropbox (UH-ECON)/repos/Tex4Econ/_other/'
spt_loc_output = 'C:/Users/fan/Documents/'
st_search_string = ['fs_', 'cases']
ls_st_ignore = ['tikz', 'pandoc']
spn_pdf_exe = 'C:/texlive/2020/bin/win32/pdflatex.exe'
dc_tex_pdf_b = pyfan_pdfgen.ff_pdf_gen_clean(ls_spt_srh=[spt_loc_search_root], spt_out=spt_loc_output,
                                             spn_pdf_exe=spn_pdf_exe,
                                             ls_st_contain=st_search_string, ls_st_ignore=ls_st_ignore,
                                             bl_recursive=True, bl_clean=True)
print(dc_tex_pdf_b)

# %%
# perl latexpand example
# ----------------------
#
# use latexpand
# conda activate wk_perl
# cd "C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/HgtOptiAlloDraft/zmain/"
# perl "C:/Users/fan/.conda/envs/wk_perl/latexpand/latexpand" draft_main_s1.tex > draft_main_s1_flat.tex
# perl "C:/ProgramData/Anaconda3/envs/wk_perl/latexpand/latexpand" draft_main_s1.tex > draft_main_s1_flat.tex
# pandoc --bibliography=C:/Users/fan/HgtOptiAlloDraft/_bib/zoteroref.bib -o draft_main_s1_flat.docx draft_main_s1_flat.tex
#
# cd "C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/HgtOptiAlloDraft/beamer/"
# perl "C:/Users/fan/.conda/envs/wk_perl/latexpand/latexpand" present.tex > present_flat.tex
# perl "C:/ProgramData/Anaconda3/envs/wk_perl/latexpand/latexpand" present.tex > present_flat.tex
#
# pandoc --bibliography=C:/Users/fan/HgtOptiAlloDraft/_bib/zoteroref.bib -o present_flat.docx present_flat.tex


# %%
# Plot String as Figure
# ---------------------

# Dict of String to String
str_dc_records = 'One Tex to Root PDF:'.upper() + '\n' + \
                 textwrap.fill(json.dumps(dc_tex_pdf_a), width=70) + '\n' + \
                 'Recursive Search Tex to PDF Folder:'.upper() + '\n' + \
                 textwrap.fill(json.dumps(dc_tex_pdf_b), width=70)
# Start Plot
fig, ax = plt.subplots()

# Text Plot
ax.text(0.5, 0.5, str_dc_records,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=14, color='black',
        transform=ax.transAxes)

# Labeling
ax.set_axis_off()
plt.show()
