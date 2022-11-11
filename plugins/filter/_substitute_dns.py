# -*- coding: utf-8 -*-

# Copyright (c) 2022, Felix Fontein <felix.fontein@alemira.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
  name: _substitute_dns
  short_description: Convert a list of tuples into a dictionary
  version_added: 3.0.0
  author: Felix Fontein (@felixfontein)
  description:
    - Convert a list of tuples into a dictionary. This is a filter version of the C(dict) function.
  options:
    _input:
      description: A list of tuples (with exactly two elements).
      type: string
      required: true
    substitution_map:
      description:
        - A map mapping DNS names to other DNS names.
        - You can use a single wildcard C(*) as the first component of a DNS name.
        - Trailing dots are ignored.
      type: dict
      required: true
'''

EXAMPLES = '''
- name: Convert list of tuples into dictionary
  ansible.builtin.set_fact:
    name: "{{ 'foo.example.com' | felixfontein.acme._substitute_dns({'*.example.com': '*.com.example.org'}) }}"
    # Result is 'foo.com.example.org'
'''

RETURN = '''
  _value:
    description: The transformed input.
    type: string
'''

from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.six import text_type
from ansible.module_utils.common._collections_compat import Mapping


def substitute_dns(name, substitution_map):
    if not isinstance(name, text_type):
        raise AnsibleFilterTypeError("The DNS name is of type %s, and not text" % type(name))
    if not isinstance(substitution_map, Mapping):
        raise AnsibleFilterTypeError("The substitution map type %s, and not a dictionary" % type(substitution_map))

    suffix = ''
    if name.endswith('.'):
        suffix = '.'
        name = name[:-1]
        
    longest_result = ''
    for src, dst in substitution_map.items():
        if not isinstance(src, text_type) or not isinstance(dst, text_type):
            raise AnsibleFilterTypeError("Key or value of dictionary entry are of type %s resp. %s, and not both are text" % (type(src), type(dst)))
        src_wildcard = False
        if src.startswith('*.'):
            src_wildcard = True
            src = src[1:]
        dst_wildcard = False
        if dst.startswith('*.'):
            if not src_wildcard:
                raise AnsibleFilterError('Non-wildcard key %s has wildcard value %s'.format(src, dst))
            dst_wildcard = True
            dst = dst[1:]
        if src_wildcard:
            if name.endswith(src):
                prefix = name[:-len(src)] if dst_wildcard else ''
                if len(dst) + len(prefix) > len(longest_result):
                    longest_result = prefix + dst
        else:
            if src == name and len(dst) > len(longest_result):
                longest_result = dst

    return (longest_result or name) + suffix


class FilterModule(object):
    '''Ansible jinja2 filters'''

    def filters(self):
        return {
            '_substitute_dns': substitute_dns,
        }
