.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_auto_examples_plot_pdfgen.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_auto_examples_plot_pdfgen.py:


Generate PDFs and Clean
========================================================================

In this example, we generate PDFs in one location from tex files in possibly
various other locations, and clean.


.. code-block:: default


    # Author: Fan Wang (fanwangecon.github.io)
    import pyfan.util.pdf.pdfgen as pyfan_pdfgen
    import pprint
    import matplotlib.pyplot as plt
    import textwrap
    import json








Generate PDF for one specific file and clean afterwards
-------------------------------------------------------


.. code-block:: default


    spt_loc = 'C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/Tex4Econ/_other/equation/'
    spt_loc_output = 'C:/Users/fan/Documents/'
    spn_file = 'cases.tex'
    spn_pdf_exe = 'C:/texlive/2019/bin/win32/pdflatex.exe'
    dc_tex_pdf_a = pyfan_pdfgen.ff_pdf_gen_clean(ls_spt_srh=[spt_loc], spt_out=spt_loc_output,
                                                 spn_pdf_exe=spn_pdf_exe, ls_st_contain=[spn_file],
                                                 bl_clean=True)
    print(dc_tex_pdf_a)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    {'C:\\Users\\fan\\Documents\\Dropbox (UH-ECON)\\repos\\Tex4Econ\\_other\\equation\\cases.tex': 'C:/Users/fan/Documents/cases.pdf'}




Generate PDF from all tex files in all subfolders of a main folder, output PDF store in one location
----------------------------------------------------------------------------------------------------

1. spt_loc_search_root: Tex Search folder
2. spt_loc_output: only consider files with this in name
3. st_search_string: include in one of the element in list
4. ls_st_ignore: ignore files with this in name
5. PDF Destination Folder: same root path earlier folder to store possibly



.. code-block:: default


    spt_loc_search_root = 'C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/Tex4Econ/_other/'
    spt_loc_output = 'C:/Users/fan/Documents/'
    st_search_string = ['fs_', 'cases']
    ls_st_ignore = ['tikz', 'pandoc']
    spn_pdf_exe = 'C:/texlive/2019/bin/win32/pdflatex.exe'
    dc_tex_pdf_b = pyfan_pdfgen.ff_pdf_gen_clean(ls_spt_srh=[spt_loc_search_root], spt_out=spt_loc_output,
                                                 spn_pdf_exe=spn_pdf_exe,
                                                 ls_st_contain=st_search_string, ls_st_ignore=ls_st_ignore,
                                                 bl_recursive=True, bl_clean=True)
    print(dc_tex_pdf_b)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    {'C:\\Users\\fan\\Documents\\Dropbox (UH-ECON)\\repos\\Tex4Econ\\_other\\equation\\cases.tex': 'C:/Users/fan/Documents/cases.pdf', 'C:\\Users\\fan\\Documents\\Dropbox (UH-ECON)\\repos\\Tex4Econ\\_other\\symbols\\fs_symbols.tex': 'C:/Users/fan/Documents/fs_symbols.pdf'}




perl latexpand example
----------------------

use latexpand
conda activate wk_perl
cd "C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/HgtOptiAlloDraft/zmain/"
perl "C:/Users/fan/.conda/envs/wk_perl/latexpand/latexpand" draft_main_s1.tex > draft_main_s1_flat.tex
perl "C:/ProgramData/Anaconda3/envs/wk_perl/latexpand/latexpand" draft_main_s1.tex > draft_main_s1_flat.tex
pandoc --bibliography=C:/Users/fan/HgtOptiAlloDraft/_bib/zoteroref.bib -o draft_main_s1_flat.docx draft_main_s1_flat.tex

cd "C:/Users/fan/Documents/Dropbox (UH-ECON)/repos/HgtOptiAlloDraft/beamer/"
perl "C:/Users/fan/.conda/envs/wk_perl/latexpand/latexpand" present.tex > present_flat.tex
perl "C:/ProgramData/Anaconda3/envs/wk_perl/latexpand/latexpand" present.tex > present_flat.tex

pandoc --bibliography=C:/Users/fan/HgtOptiAlloDraft/_bib/zoteroref.bib -o present_flat.docx present_flat.tex

Plot String as Figure
---------------------


.. code-block:: default


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



.. image:: /auto_examples/images/sphx_glr_plot_pdfgen_001.svg
    :alt: plot pdfgen
    :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  4.999 seconds)


.. _sphx_glr_download_auto_examples_plot_pdfgen.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: plot_pdfgen.py <plot_pdfgen.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: plot_pdfgen.ipynb <plot_pdfgen.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
