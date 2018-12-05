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
    ceilometer=('http://docs.openstack.org/ceilometer/latest/', None),
    cinder=('http://docs.openstack.org/cinder/latest/', None),
    glance=('http://docs.openstack.org/glance/latest/', None),
    heat=('http://docs.openstack.org/heat/latest/', None),
    horizon=('http://docs.openstack.org/horizon/latest/', None),
    ironic=('http://docs.openstack.org/ironic/latest/', None),
    keystone=('http://docs.openstack.org/keystone/latest/', None),
    nova=('http://docs.openstack.org/nova/latest/', None),
    oslo_config=('http://docs.openstack.org/oslo.config/latest/', None),
    oslo_messaging=(
        'http://docs.openstack.org/oslo.messaging/latest/', None),
    ceilometerclient=(
        'http://docs.openstack.org/python-ceilometerclient/latest/', None),
    cinderclient=(
        'http://docs.openstack.org/python-cinderclient/latest/', None),
    glanceclient=(
        'http://docs.openstack.org/python-glanceclient/latest/', None),
    heatclient=(
        'http://docs.openstack.org/python-heatclient/latest/', None),
    ironicclient=(
        'http://docs.openstack.org/python-ironicclient/latest/', None),
    keystoneclient=(
        'http://docs.openstack.org/python-keystoneclient/latest/', None),
    novaclient=(
        'http://docs.openstack.org/python-novaclient/latest/', None),
    openstackclient=(
        'http://docs.openstack.org/python-openstackclient/latest/', None),
    neutronclient=(
        'http://docs.openstack.org/python-neutronclient/latest/', None),
    swiftclient=(
        'http://docs.openstack.org/python-swiftclient/latest/', None),
    troveclient=(
        'http://docs.openstack.org/python-troveclient/latest/', None),
    neutron=('http://docs.openstack.org/neutron/latest/', None),
    swift=('http://docs.openstack.org/swift/latest/', None),
    trove=('http://docs.openstack.org/trove/latest/', None),
    # Other things of note
    python=('http://docs.python.org/', None),
    infra=('http://docs.openstack.org/infra/system-config/', None),
    zuul=('http://docs.openstack.org/infra/zuul/', None),
)
