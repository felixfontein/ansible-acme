# (c) 2021, Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
name: check_collection
author: Felix Fontein (@felixfontein)
version_added: "0.4.0"
short_description: Check whether a module or action plugin is available
description:
  - This lookup allows to query whether a module or action plugin is available under a given name.
  - Please note that this lookup does B(not) use the C(collections) keyword.
options:
  _terms:
    description:
      - The short names or FQCNs for the modules or action plugins to check for.
      - For example C(file) or C(community.general.cobbler_system).
    type: list
    elements: str
    required: true
"""

EXAMPLES = """
- name: Check whether community.general.cobbler_system is available.
  ansible.builtin.debug:
    msg: "We can use cobbler_system: {{ lookup('felixfontein.acme.check_action', 'community.general.cobbler_system') }}"
"""

RETURN = """
  _raw:
    description:
      - C(true) indicates the action is available, C(false) indicates it is not available.
    type: list
    elements: bool
"""

from ansible.plugins.loader import action_loader, module_loader
from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        result = []
        self.set_options(var_options=variables, direct=kwargs)

        for term in terms:
            found = False
            for loader in (action_loader, module_loader):
                data = loader.find_plugin(term)
                # Ansible 2.9 returns a tuple
                if isinstance(data, tuple):
                    data = data[0]
                if data is not None:
                    found = True
                    break
            result.append(found)

        return result
