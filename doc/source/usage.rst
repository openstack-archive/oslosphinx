============================
 Using the oslosphinx Theme
============================

To use the theme, add ``'oslosphinx'`` to the ``extensions`` list in
the ``conf.py`` file in your Sphinx project.

Incubating Projects
===================

If you are an incubating project, set::

  html_theme_options = {'incubating': True}

in your conf.py as well, to enable the Incubation theme.

Linking to a Source Repository
==============================

``oslosphinx`` defines a configuration option ``oslosphinx_cgit_link``
which should be the URL to the git repository browser for the project
being documented. The default is a guess, and will be right for a lot
of projects, but to ensure that it is correct in all situations it is
best to set the value in conf.py::

  oslosphinx_cgit_link = 'http://git.openstack.org/cgit/openstack/oslosphinx'
