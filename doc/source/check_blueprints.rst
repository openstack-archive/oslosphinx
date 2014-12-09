===========================================================
 Using oslosphinx.check_blueprints with Specs Repositories
===========================================================

The ``oslosphinx.check_blueprints`` extension verifies that the
filenames in spec repositories match a blueprint under a given
launchpad project.

Enabling
========

Add ``'oslosphinx.check_blueprints'`` to the ``extensions`` list in
the ``conf.py`` file in your Sphinx project.

Specifying the Launchpad Project
================================

Most projects should set ``check_blueprints_project`` to the name of
their launchpad project. This limits the search to the single project
named.

::

  check_blueprints_project = 'nova'

Projects with multiple launchpad projects under their own project
group (such as Oslo), should instead set
``check_blueprints_project_group``. All projects in the group will be
scanned for each spec/blueprint name.

::

  check_blueprints_project_group = 'oslo'

Checking Only the Current Release
=================================

By default, all files under ``specs/`` are checked. For large specs
repositories, this can take a long time. To limit the checks to a
subdirectory for the current release, set
``check_blueprints_release``.

For example::

  check_blueprints_release = 'kilo'

will cause files under ``specs/kilo`` to be checked, and other files
to be ignored.
