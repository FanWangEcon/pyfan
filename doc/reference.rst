.. sectnum::

This page provides the API reference for `package <https://pyfan.readthedocs.io/en/latest/>`__. Modules and functions are listed below in different sections.

Data Structures
---------------

Various data structures.

Array
~~~~~

Functions to manipulate numpy arrays and other structures.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.amto.array.geomspace
   pyfan.amto.array.gridminmax
   pyfan.amto.array.mesh
   pyfan.amto.array.scalararray

JSON
~~~~~

Function to manipulate JSON Structures

.. currentmodule:: pyfan

.. autosummary::
  :toctree: gen_modules
  :template: module.rst

  pyfan.amto.json.json


List and Dict
~~~~~~~~~~~~~~

List and dictionary

.. currentmodule:: pyfan

.. autosummary::
  :toctree: gen_modules
  :template: module.rst

  pyfan.amto.lsdc.lsdcconvert


Numeric
~~~~~~~~

Numeric manipulations

.. currentmodule:: pyfan

.. autosummary::
  :toctree: gen_modules
  :template: module.rst

  pyfan.amto.numeric.round


Amazon Web Services
-------------------

Functions to support AWS service usages.

General
~~~~~~~~

AWS general functions.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.aws.general.credentials
   pyfan.aws.general.path

S3
~~~~~

Functions for S3 storage.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.aws.s3.pushsync



Development
-----------

Package and function development support functions.

Log Support
~~~~~~~~~~~~~~~

Log support functions.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.devel.flog.logsupport

Object
~~~~~~

Object support functions.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.devel.obj.classobjsupport




Generate
-----------

Generate specific data-structures.


Random
~~~~~~

Data structures based on random seed draws.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.gen.rand.randgrid




Graph
-----------

Graphing support tools.

Example
~~~~~~~

Graphing example functions.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.graph.exa.scatterline3

Generic
~~~~~~~

All purpose graph support functions

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.graph.generic.allpurpose

Tools
~~~~~

Some graphing tools.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.graph.tools.subplot




Pandas
-----------

Pandas related functions.

Categorical
~~~~~~~~~~~

Functions to handle categorical variables.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.panda.categorical.catevars
   pyfan.panda.categorical.strsvarskeys

In and Out
~~~~~~~~~~

Functions for combine, export, etc dataframes.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.panda.inout.combine
   pyfan.panda.inout.readexport

Stats
~~~~~

Stats operations on dataframes.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.panda.stats.cutting
   pyfan.panda.stats.mean_varcov
   pyfan.panda.stats.polynomial_regression




Statistics
-----------

Statistical functions.

Interpolate
~~~~~~~~~~~

Interpolation functions.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.stats.interpolate.interpolate2d

Markov
~~~~~~

Markov related functions.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.stats.markov.transprobcheck

Multinomial
~~~~~~~~~~~

Discrete choice multinomial functions.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.stats.multinomial.multilogit




Utilities
-----------

General support functions.

In and Out
~~~~~~~~~~

Export, import etc.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.util.inout.exportpanda
   pyfan.util.inout.iosupport

Path
~~~~~

Path and location related functions.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.util.path.getfiles
   pyfan.util.path.movefiles

PDF
~~~~~

PDF generation support functions

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.util.pdf.pdfgen

RMD
~~~~~

RMD and bookdown related functions.

.. currentmodule:: pyfan

.. autosummary::
   :toctree: gen_modules
   :template: module.rst

   pyfan.util.rmd.bookdownparse
   pyfan.util.rmd.mattexmd
   pyfan.util.rmd.rmdparse

Timer
~~~~~

Timer functions.

.. currentmodule:: pyfan

.. autosummary::
  :toctree: gen_modules
  :template: module.rst

  pyfan.util.timer.timer
