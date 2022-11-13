# -*- coding: utf-8 -*-

# Copyright (c) 2022, Felix Fontein <felix.fontein@alemira.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
  name: _substitute_dns
  short_description: "[INTERNAL] Convert a list of tuples into a dictionary"
  version_added: 0.6.0
  author: Felix Fontein (@felixfontein)
  description:
    - B(This is an internal tool and must not be used outside this collection!)
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
- name: Simple replace
  ansible.builtin.set_fact:
    name: "{{ 'www.example.com' | felixfontein.acme._substitute_dns({'www.example.com': 'www.com.example.org'}) }}"
    # Result is 'www.com.example.org'

- name: Replace with wildcard
  ansible.builtin.set_fact:
    name: "{{ 'foo.example.com' | felixfontein.acme._substitute_dns({'*.example.com': '*.com.example.org'}) }}"
    # Result is '*.com.example.org'

- name: Replace (not) with wildcard
  ansible.builtin.set_fact:
    name: "{{ 'www.foo.example.com' | felixfontein.acme._substitute_dns({'*.example.com': '*.com.example.org'}) }}"
    # Result is 'www.foo.example.com' (the wildcard does not match because there is more than one component)
'''

RETURN = '''
  _value:
    description: The transformed input.
    type: string
'''

from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.six import string_types
from ansible.module_utils.common._collections_compat import Mapping
from ansible.module_utils.common.text.converters import to_text, to_native


def substitute_dns(name, substitution_map):
    if not isinstance(name, string_types):
        raise AnsibleFilterTypeError("The DNS name is of type %s, and not text" % type(name))
    if not isinstance(substitution_map, Mapping):
        raise AnsibleFilterTypeError("The substitution map type %s, and not a dictionary" % type(substitution_map))
    name = to_text(name)
    if len(name) > 1 and (name.startswith(u'.') or u'..' in name):
        raise AnsibleFilterError("Invalid DNS name %r" % to_native(name))

    suffix = u''
    if name.endswith(u'.'):
        suffix = u'.'
        name = name[:-1]

    result = name
    result_wc = True
    for src, dst in substitution_map.items():
        if not isinstance(src, string_types) or not isinstance(dst, string_types):
            raise AnsibleFilterTypeError("Key or value of dictionary entry are of type {0} resp. {1}, but both must be text".format(type(src), type(dst)))
        src = to_text(src)
        dst = to_text(dst)
        src_wildcard = False
        if src.startswith(u'*.'):
            src_wildcard = True
            src = src[1:]
        if src_wildcard:
            if name.endswith(src) and u'.' not in name[:-len(src)] and result_wc:
                result = dst
                result_wc = True
        else:
            if src == name:
                result = dst
                result_wc = False
                break

    return result + suffix


class FilterModule(object):
    '''Ansible jinja2 filters'''

    def filters(self):
        return {
            '_substitute_dns': substitute_dns,
        }
