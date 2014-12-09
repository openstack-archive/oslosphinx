============================
 Using the oslosphinx Theme
============================

To use the theme, add ``'oslosphinx'`` to the ``extensions`` list in
the ``conf.py`` file in your Sphinx project.

IMPORTANT Requirements Management Step
======================================

Some of the dependencies for ``launchpadlib`` are not available on
PyPI, so you must also edit ``tox.ini`` to allow them to be
installed::

  [testenv]
  install_command = pip install -U {opts} --allow-external lazr.authentication --allow-insecure lazr.authentication {packages}


Incubating Projects
===================

If you are an incubating project, set::

  html_theme_options = {'incubating': True}

in your conf.py as well, to enable the Incubation theme.
