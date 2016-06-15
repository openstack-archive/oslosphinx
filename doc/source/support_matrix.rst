==================================================
Using oslosphinx.support_matrix for Support Matrix
==================================================

The ``oslosphinx.support_matrix`` extension provides
the framework required to build a project's feature
matrix. This framework will build a matrix similar
to Nova's implementation:
http://docs.openstack.org/developer/nova/support-matrix.html


Enabling
========

Add ``oslosphinx.support_matrix`` to the ``extensions`` list
in the ``conf.py`` file in your Sphinx project.


Building Matrix
===============

The Sphinx project will also need the appropriate support_matrix.rst
file to provide the user with enough background of the purpose of the
matrix.

The matrix itself is built using the support_matrix.ini file which
specifies the hypervisors, backends, or plugins the matrix will describe.

Examples to come
