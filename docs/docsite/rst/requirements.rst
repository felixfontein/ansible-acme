..
  GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
  SPDX-License-Identifier: GPL-3.0-or-later
  SPDX-FileCopyrightText: 2020, Felix Fontein

.. _ansible_collections.felixfontein.acme.docsite.requirements:

Requirements
============

The collection requires the Python `cryptography <https://pypi.org/project/cryptography/>`_ library installed on the controller, available to the Python version used to execute the playbook. If ``cryptography`` is not installed, a recent enough version of `PyOpenSSL <https://pypi.org/project/pyOpenSSL/>`_ is currently supported as a fallback by the :ansplugin:`community.crypto.openssl_privatekey <community.crypto.openssl_privatekey#module>` and :ansplugin:`community.crypto.openssl_csr <community.crypto.openssl_csr#module>` modules.

The ``openssl`` binary must also be available in the executable path on the controller. It is needed by the :ansplugin:`community.crypto.acme_certificate <community.crypto.acme_certificate#module>` module in case ``cryptography`` is not installed, and it is used for certificate chain validation.

If DNS challenges are used, there can be other requirements depending on the DNS provider. For example, for Amazon's Route 53, the Ansible :ansplugin:`amazon.aws.route53 module <amazon.aws.route53#module>` requires the Python `boto <https://pypi.org/project/boto/>`_ package. If Hosttech DNS challenges are used, the `lxml <https://pypi.org/project/lxml/>`_ package needs to be installed. If DNS challenges with NS1 or INWX are used, the corresponding modules respectively collections must be installed. See below for more information.
