# Copyright 2013 New Dream Network, LLC (DreamHost)
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import re
import six
from six.moves.urllib import parse
import string
import subprocess


CGIT_BASE = 'http://git.openstack.org/cgit/'


def _guess_cgit_link():
    try:
        git_remote = subprocess.check_output(
            ['git', 'config', '--local', '--get', 'remote.origin.url']
        )
    except Exception:
        # git is not present or the command failed
        return None
    else:
        if six.PY3:
            git_remote = os.fsdecode(git_remote)
        parsed = parse.urlparse(git_remote)
        parsed = '/'.join(parsed.path.rstrip('/').split('/')[-2:])
        parsed = re.sub(r'\.git$', '', parsed)
        return CGIT_BASE + parsed


def _html_page_context(app, pagename, templatename, context, doctree):
    # Insert the cgit link into the template context.
    context['cgit_link'] = app.config.oslosphinx_cgit_link
    context['other_versions'] = _get_other_versions(app)
    return None


def _get_other_versions(app):
    if not app.config.html_theme_options.get('show_other_versions', False):
        return []

    git_cmd = ["git", "tag"]
    try:
        raw_version_list = subprocess.Popen(
            git_cmd, stdout=subprocess.PIPE).communicate()[0]
        raw_version_list = raw_version_list.decode("utf8")
    except OSError:
        app.warn('Cannot get tags from git repository. '
                 'Not setting "other_versions".')
        raw_version_list = u''

    # grab last five that start with a number and reverse the order
    _tags = [t.strip("'") for t in raw_version_list.split('\n')]
    other_versions = [
        t for t in _tags if t and t[0] in string.digits
        # Don't show alpha, beta or release candidate tags
        and 'rc' not in t and 'a' not in t and 'b' not in t
    ][:-5:-1]
    return other_versions


def builder_inited(app):
    theme_dir = os.path.join(os.path.dirname(__file__), 'theme')
    app.info('Using openstack theme from %s' % theme_dir)
    # Insert our theme directory at the front of the search path and
    # force the theme setting to use the one in the package unless
    # another openstack theme is already selected. This is done here,
    # instead of in setup(), because conf.py is read after setup()
    # runs, so if the conf contains these values the user values
    # overwrite these. That's not bad for the theme, but it breaks the
    # search path.
    app.config.html_theme_path.insert(0, theme_dir)
    # Set the theme name
    if not app.config.html_theme.startswith('openstack'):
        app.config.html_theme = 'openstack'
    # Re-initialize the builder, if it has the method for setting up
    # the templates and theme.
    if hasattr(app.builder, 'init_templates'):
        app.builder.init_templates()
    # Register our page context additions
    app.connect('html-page-context', _html_page_context)


def setup(app):
    app.connect('builder-inited', builder_inited)
    # Try to guess at the default value for where the cgit repository
    # is.
    cgit_link = _guess_cgit_link()
    app.add_config_value('oslosphinx_cgit_link', cgit_link, 'env')
