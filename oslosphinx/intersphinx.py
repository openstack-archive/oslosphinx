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

"""Intersphinx mapping file for the OpenStack projects.

To use this mapping in a project, first add 'sphinx.ext.intersphinx' to
your extensions list in conf.py. Then::

   from oslosphinx import intersphinx
   intersphinx_mapping = intersphinx.mapping

You'll be able to link to other project's documentation, such as:

    :ref:`virtual-environments <nova:virtual-environments>`
"""

mapping = dict(
    # OpenStack Projects
    ceilometer=('http://docs.openstack.org/developer/ceilometer/', None),
    cinder=('http://docs.openstack.org/developer/cinder/', None),
    glance=('http://docs.openstack.org/developer/glance/', None),
    heat=('http://docs.openstack.org/developer/heat/', None),
    horizon=('http://docs.openstack.org/developer/horizon/', None),
    ironic=('http://docs.openstack.org/developer/ironic/', None),
    keystone=('http://docs.openstack.org/developer/keystone/', None),
    nova=('http://docs.openstack.org/developer/nova/', None),
    oslo_config=('http://docs.openstack.org/developer/oslo.config/', None),
    oslo_messaging=(
        'http://docs.openstack.org/developer/oslo.messaging/', None),
    ceilometerclient=(
        'http://docs.openstack.org/developer/python-ceilometerclient/', None),
    cinderclient=(
        'http://docs.openstack.org/developer/python-cinderclient/', None),
    glanceclient=(
        'http://docs.openstack.org/developer/python-glanceclient/', None),
    heatclient=(
        'http://docs.openstack.org/developer/python-heatclient/', None),
    ironicclient=(
        'http://docs.openstack.org/developer/python-ironicclient/', None),
    keystoneclient=(
        'http://docs.openstack.org/developer/python-keystoneclient/', None),
    novaclient=(
        'http://docs.openstack.org/developer/python-novaclient/', None),
    openstackclient=(
        'http://docs.openstack.org/developer/python-openstackclient/', None),
    neutronclient=(
        'http://docs.openstack.org/developer/python-neutronclient/', None),
    swiftclient=(
        'http://docs.openstack.org/developer/python-swiftclient/', None),
    troveclient=(
        'http://docs.openstack.org/developer/python-troveclient/', None),
    neutron=('http://docs.openstack.org/developer/neutron/', None),
    swift=('http://docs.openstack.org/developer/swift/', None),
    trove=('http://docs.openstack.org/developer/trove/', None),
    # Other things of note
    python=('http://docs.python.org/', None),
    infra=('http://docs.openstack.org/infra/system-config/', None),
    zuul=('http://docs.openstack.org/infra/zuul/', None),
)
