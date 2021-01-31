# Tools for ACME
[![CI](https://github.com/felixfontein/ansible-acme/workflows/CI/badge.svg?event=push)](https://github.com/felixfontein/ansible-acme/actions)

This collection provides some useful roles for retrieving ACME certificates.

## Tested with Ansible

This collection is tested with Ansible 2.9, ansible-base 2.10 and ansible-core's `devel` branch.

## External requirements

Requires the Python [cryptography](https://pypi.org/project/cryptography/) library installed on the controller, available to the Python version used to execute the playbook. If `cryptography` is not installed, a recent enough version of [PyOpenSSL](https://pypi.org/project/pyOpenSSL/) is currently supported as a fallback by the `community.crypto.openssl_privatekey` and `community.crypto.openssl_csr` modules.

The `openssl` binary must also be available in the executable path on the controller. It is needed by the `acme_certificate` module in case `cryptography` is not installed, and it is used for certificate chain validation.

If DNS challenges are used, there can be other requirements depending on the DNS provider. For example, for Amazon's Route 53, the Ansible `route53` module requires the Python [`boto`](https://pypi.org/project/boto/) package. If Hosttech DNS challenges are used, the [`lxml`](https://pypi.org/project/lxml/) package needs to be installed. If DNS challenges with NS1 are used, the NS1 modules must be installed. See below for more information.

## Included content

- Role [felixfontein.acme.acme_certificate](https://github.com/felixfontein/ansible-acme/tree/main/README.acme_certificate.md).
- Role [felixfontein.acme.revoke_old_certificates](https://github.com/felixfontein/ansible-acme/tree/main/README.revoke_old_certificates.md).
- Role [felixfontein.acme.account_key_rollover](https://github.com/felixfontein/ansible-acme/tree/main/README.account_key_rollover.md).

## Using this collection

Before using the crypto community collection, you need to install the collection with the `ansible-galaxy` CLI:
```
ansible-galaxy collection install felixfontein.acme
```

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: felixfontein.acme
```

See [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

For using this collection, you always also need an ACME account. See [here](https://github.com/felixfontein/ansible-acme/tree/main/README.acme-account.md) on how to create one.

## Release notes

See [here](https://github.com/felixfontein/ansible-acme/tree/main/CHANGELOG.rst).

## Releasing, Deprecation and Versioning

We release new versions once there are new features or bugfixes. Deprecations can happen, and we try to announce them a long time in advance. We currently do not plan breaking changes, so there will be no new major release anytime soon.

## More information

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
