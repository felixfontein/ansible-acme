# (c) 2021, Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
name: check_collection
author: Felix Fontein (@felixfontein)
version_added: "0.4.0"
short_description: Check whether a collection is installed and retrieve its version
description:
  - This lookup allows to query whether a collection is installed, and if it is installed returns the collection version.
options:
  _terms:
    description:
      - The collections to look for.
      - For example C(community.general).
    type: list
    elements: str
    required: true
"""

EXAMPLES = """
- name: Check version of community.general
  ansible.builtin.debug:
    msg: "community.general version {{ lookup('felixfontein.acme.check_collection', 'community.general) }}"
"""

RETURN = """
  _raw:
    description:
      - The version number of the collections listed as input.
      - If a collection can not be found, it will return C(none).
      - If a collection can be found, but the version not identified, it will return C(*).
        This can happen for collections installed from git which do not have a version number
        in C(galaxy.yml).
    type: list
    elements: str
"""

import os
import re

import yaml

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils._text import to_text
from ansible.utils.display import Display

from ansible.utils.collection_loader._collection_finder import _get_collection_metadata

from ansible.module_utils.compat.importlib import import_module

display = Display()


FQCN_RE = re.compile(r'^[A-Za-z0-9_]+\.[A-Za-z0-9_]+$')


def load_collection_meta_manifest(manifest_path):
    with open(manifest_path, 'rb') as f:
        meta = json.load(f)
    return {
        'version': meta['collection_info']['version'],
    }


def load_collection_meta_galaxy(galaxy_path):
    with open(galaxy_path, 'rb') as f:
        meta = yaml.safe_load(f)
    return {
        'version': meta.get('version') or '*',
    }


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        result = []
        self.set_options(var_options=variables, direct=kwargs)

        for term in terms:
            if not FQCN_RE.match(term):
                raise AnsibleLookupError('"{term}" is not a FQCN'.format(term=term))

            try:
                collection_pkg = import_module('ansible_collections.{fqcn}'.format(fqcn=term))
                if not collection_pkg:
                    raise Exception('collection not found')
            except Exception:
                # Collection not found
                result.append(None)
                continue

            try:
                path = os.path.dirname(collection_pkg.__file__)
                manifest_path = os.path.join(path, 'MANIFEST.json')
                if os.path.exists(manifest_path):
                    data = load_collection_meta_manifest(manifest_path)
                else:
                    data = {}
                    galaxy_path = os.path.join(path, 'galaxy.yml')
                    galaxy_alt_path = os.path.join(path, 'galaxy.yaml')
                    for path in (galaxy_path, galaxy_alt_path):
                        if os.path.exists(path):
                            data = load_collection_meta_galaxy(path)
                            break
            except Exception as exc:
                raise AnsibleLookupError('Error while loading metadata for {fqcn}: {error}'.format(fqcn=term, error=exc))

            result.append(data.get('version', '*'))

        return result
