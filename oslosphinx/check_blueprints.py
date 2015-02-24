# All Rights Reserved.
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
"""Ensure that the name of the spec file matches the name of a blueprint.
"""

import requests


class BlueprintChecker(object):

    def __init__(self, app):
        self.app = app
        self.project_names = []
        self._good_bps = set()
        self._prefix = None
        self._warn_search = 'unset'

    BP_URL_TEMPLATE = 'https://api.launchpad.net/devel/%s/+spec/%s'
    PROJ_LIST_URL_TEMPLATE = 'https://api.launchpad.net/1.0/%s/projects'

    def _load_project_settings(self):
        if self.project_names:
            return
        # If a project_name is set in the configuration, use
        # that. Otherwise, allow any project in the project group.
        project_name = self.app.config.check_blueprints_project
        pg_name = self.app.config.check_blueprints_project_group
        if project_name:
            self.project_names = [project_name]
            self._warn_search = 'the %s project' % project_name
        else:
            proj_list_response = requests.get(self.PROJ_LIST_URL_TEMPLATE
                                              % pg_name)
            projects = proj_list_response.json()['entries']
            self.project_names = [p['name'] for p in projects]
            self._warn_search = ('any projects in the %s project group'
                                 % pg_name)

    @property
    def desired_prefix(self):
        """Determine the prefix for files we care to check.

        We only care about blueprints in the current release, if the
        check_blueprints_release option is set.

        """
        if self._prefix is None:
            release = self.app.config.check_blueprints_release
            if release:
                self._prefix = 'specs/%s/' % release
            else:
                self._prefix = 'specs/'
        return self._prefix

    def doctree_resolved(self, app, doctree, docname):
        """Hook registered as event handler."""
        if not docname.startswith(self.desired_prefix):
            return
        bp_name = docname.split('/')[-1]
        if bp_name == 'index':
            return
        self.check(bp_name)

    def blueprint_exists(self, project_name, bp_name):
        """Return boolean indicating whether the blueprint exists."""
        self.app.info('Checking for %s in %s' % (bp_name, project_name))
        url = self.BP_URL_TEMPLATE % (project_name, bp_name)
        response = requests.get(url)
        if response.status_code == 200:
            self.app.info('Found %s in %s' % (bp_name, project_name))
            return True
        return False

    def check(self, bp_name):
        """Given one blueprint name, check to see if it is valid."""
        if bp_name in self._good_bps:
            return True
        self._load_project_settings()
        self.app.info('')  # emit newline
        candidate_project, dash, bp_name_to_find = bp_name.partition('-')
        if candidate_project in self.project_names:
            # First check the shortened name of the blueprint in the project.
            if self.blueprint_exists(candidate_project, bp_name_to_find):
                return
            # Then check the full name of the blueprint in the project.
            if self.blueprint_exists(candidate_project, bp_name):
                return
            self.app.info(
                ('Blueprint name %r looks like it starts with a project '
                 'name, but %r was not found in project %r') %
                (bp_name, bp_name_to_find, candidate_project)
            )
        else:
            self.app.info(
                'Blueprint checking is faster if the file names '
                'start with the launchpad project name.'
            )
        for project_name in self.project_names:
            if self.blueprint_exists(project_name, bp_name):
                self._good_bps.add(bp_name)
                break
        else:
            self.app.warn(
                'Could not find a blueprint called %r in %s'
                % (bp_name, self._warn_search),
                location=(bp_name, 0),
            )
            raise ValueError(
                'Document %s does not match any blueprint name in %s'
                % (bp_name, self._warn_search))


def setup(app):
    app.info('Initializing %s' % __name__)
    checker = BlueprintChecker(app)
    app.connect('doctree-resolved', checker.doctree_resolved)
    app.add_config_value('check_blueprints_project_group', 'openstack', 'env')
    app.add_config_value('check_blueprints_project', '', 'env')
    app.add_config_value('check_blueprints_release', '', 'env')
