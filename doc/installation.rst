Installation
============

Using github
------------

The easiest way to install ``pyfan`` is probably via ``github``:

.. code-block:: bash

    pip uninstall pyfan -y
    pip install git+https://github.com/fanwangecon/pyfan.git#egg=pyfan

This should also install dependencies if any are missing.

Using PyPI
----------

This should also work fine, version might be slightly behind:

.. code-block:: bash

    pip uninstall pyfan -y
    pip install pyfan

Other requirements
------------------

``pyfan`` builds on (and hence depends on) numpy`` and
``scipy`` libraries other packages shown in the
`toml file <https://github.com/FanWangEcon/pyfan/blob/master/doc/pyproject.toml>`_
