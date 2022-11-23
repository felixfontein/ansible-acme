<!--
GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
SPDX-License-Identifier: GPL-3.0-or-later
SPDX-FileCopyrightText: 2020, Felix Fontein
-->

# Tools for ACME
[![Doc](https://img.shields.io/badge/docs-brightgreen.svg)](https://ansible.fontein.de/collections/felixfontein/acme/)
[![CI](https://github.com/felixfontein/ansible-acme/workflows/CI/badge.svg?branch=main)](https://github.com/felixfontein/ansible-acme/actions?query=workflow%3A%22CI%22+branch%3Amain)

This collection provides some useful roles for retrieving ACME certificates.

## Tested with Ansible

Tested with the current Ansible 2.9, ansible-base 2.10, ansible-core 2.11, ansible-core 2.12, ansible-core 2.13, and ansible-core 2.14 releases and the current development version of ansible-core. Ansible versions before 2.9.17 are not supported, and ansible-base versions before 2.10.4 are also not supported.

## External requirements

Requires the Python [cryptography](https://pypi.org/project/cryptography/) library installed on the controller, available to the Python version used to execute the playbook. If `cryptography` is not installed, a recent enough version of [PyOpenSSL](https://pypi.org/project/pyOpenSSL/) is currently supported as a fallback by the `community.crypto.openssl_privatekey` and `community.crypto.openssl_csr` modules.

The `openssl` binary must also be available in the executable path on the controller. It is needed by the `acme_certificate` module in case `cryptography` is not installed, and it is used for certificate chain validation by the `felixfontein.acme.acme_certificate` role.

If DNS challenges are used, there can be other requirements depending on the DNS provider. For example, for Amazon's Route 53, the Ansible `amazon.aws.route53` module requires the Python [`boto3`](https://pypi.org/project/boto3/) package. If DNS challenges with NS1 are used, the NS1 modules must be installed. See below for more information.

## Included content

- Role [felixfontein.acme.acme_certificate](https://ansible.fontein.de/collections/felixfontein/acme/docsite/acme_certificate_role.html).
- Role [felixfontein.acme.revoke_old_certificates](https://ansible.fontein.de/collections/felixfontein/acme/docsite/revoke_old_certificates_role.html).
- Role [felixfontein.acme.account_key_rollover](https://ansible.fontein.de/collections/felixfontein/acme/docsite/account_key_rollover_role.html).

## Using this collection

Before using the `felixfontein.acme` collection, you need to install the collection with the `ansible-galaxy` CLI:
```
ansible-galaxy collection install felixfontein.acme
```

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: felixfontein.acme
```

See [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

For using this collection, you always also need an ACME account. See [the documentation on ACME accounts](https://ansible.fontein.de/collections/felixfontein/acme/docsite/acme_account.html) on how to create one.

## Release notes

See [the changelog](https://github.com/felixfontein/ansible-acme/tree/main/CHANGELOG.rst).

## Releasing, Deprecation and Versioning

We release new versions once there are new features or bugfixes. Deprecations can happen, and we try to announce them a long time in advance. We currently do not plan breaking changes, so there will be no new major release anytime soon.

## Contributing

Please create issues to report problems or request new features, and create PRs to fix bugs or add new features. If you want to do a refactoring PR, please create an issue first to discuss the refactoring.

Please follow the general Ansible contributor guidelines; see the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html).

## More information

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
