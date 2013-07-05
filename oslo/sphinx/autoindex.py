# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

_rst_template = """%(heading)s
%(underline)s

.. automodule:: %(module)s
  :members:
  :undoc-members:
  :show-inheritance:
"""

_toctree_rst = """.. toctree::
  :maxdepth: 1

"""


def _find_modules(arg, dirname, files):
    for filename in files:
        if filename.endswith('.py') and filename != '__init__.py':
            arg["%s.%s" % (dirname.replace('/', '.'),
                           filename[:-3])] = True


def _builder_inited(app):
    app.info("[oslo.sphinx] Autodocumenting from %s"
             % os.path.abspath(os.curdir))
    source_dir = os.path.join(app.srcdir, 'api')
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)

    modules = {}
    for pkg in app.config.autoindex_packages:
        if '.' not in pkg:
            for dirpath, dirnames, files in os.walk(pkg):
                _find_modules(modules, dirpath, files)
    module_list = list(modules.keys())
    module_list.sort()
    autoindex_filename = os.path.join(source_dir, 'autoindex.rst')
    with open(autoindex_filename, 'w') as autoindex:
        autoindex.write(_toctree_rst)
        for module in module_list:
            output_filename = os.path.join(source_dir,
                                           "%s.rst" % module)
            heading = "The :mod:`%s` Module" % module
            underline = "=" * len(heading)
            values = dict(module=module, heading=heading,
                          underline=underline)

            app.info("[oslo.sphinx] Generating %s"
                     % output_filename)
            with open(output_filename, 'w') as output_file:
                output_file.write(_rst_template % values)
            autoindex.write("  %s\n" % module)


def setup(app):
    """Respond to Sphinx extension registration.

    Sphinx will call this method at setup time if this module is listed
    in extensions. `app` is an instance of sphinx.application.Sphinx.
    Primarily, this function should register expected config settings
    and register callback functions with sphinx hooks. In this case,
    we add autoinde_pacakges as a config value we want to respond to,
    and well tell sphinx to run _builder_inited on the builder-inited
    event.
    """
    app.add_config_value('autoindex_packages', [], True)
    app.connect('builder-inited', _builder_inited)
