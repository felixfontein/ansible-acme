============================
Tools for ACME Release Notes
============================

.. contents:: Topics


v0.5.2
======

Release Summary
---------------

Maintenance release.

v0.5.1
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- When cleaning up after failures in the ``acme_certificate`` role, make sure that an undefined ``ansible_failed_task`` does not cause another error (https://github.com/felixfontein/ansible-acme/pull/32).

v0.5.0
======

Release Summary
---------------

Feature release dropping support for some specific old Ansible/ansible-base versions.

Minor Changes
-------------

- In case an error happens before a certificate is issued, restore private key, and remove certificate and key backups if these were made (``acme_certificate_keys_old_store`` option) (https://github.com/felixfontein/ansible-acme/pull/30).
- The collection repository conforms to the `REUSE specification <https://reuse.software/spec/>`__ (https://github.com/felixfontein/ansible-acme/pull/30).
- Use FQCN for builtin actions and lookup plugins (https://github.com/felixfontein/ansible-acme/pull/23).
- acme_certificate role - add ``acme_certificate_renewal_on_remaining_days`` option which allows to only renew certificates that expire in a certain amount of days (https://github.com/felixfontein/ansible-acme/pull/28).

Breaking Changes / Porting Guide
--------------------------------

- Officially drop support for Ansible 2.9.10 to 2.9.16, and ansible-base 2.10.0 to 2.10.3. These versions did not work with the ``felixfontein.acme.acme_certificate`` role for some time now, so this should not really affect any regular user of this collection (https://github.com/felixfontein/ansible-acme/pull/23).

v0.4.0
======

Release Summary
---------------

This release bumps some requirements and adds some features.

Minor Changes
-------------

- The collection now requires community.dns >= 2.0.0 for Hosttech DNS support.
- The collection now requires community.general >= 4.0.0.
- acme_certificate role - an alternative root certificate URL can be specified in ``acme_certificate_root_certificate_for_verification`` that is only used for validating the retrieved chain (https://github.com/felixfontein/ansible-acme/pull/22).
- acme_certificate role - the role can now handle the DNS provider INWX (https://github.com/felixfontein/ansible-acme/pull/19).

v0.3.1
======

Release Summary
---------------

Update dependencies.

Bugfixes
--------

- Hosttech DNS support: restrict required version of community.dns to < 2.0.0. A later version will bump the requirement to >= 2.0.0 and switch to the new API.

v0.3.0
======

Release Summary
---------------

Major revamp of the collection with new dependencies, better documentation, and several features and bugfixes.

Minor Changes
-------------

- Add documentation for the roles to the `collection's docsite <https://ansible.fontein.de/collections/felixfontein/acme/>`_ (https://github.com/felixfontein/ansible-acme/pull/9).
- Adding support for ansible-core's new role argument spec feature. This makes ansible-core 2.11.1 or newer validate the parameters passed to the roles in this collection (https://github.com/felixfontein/ansible-acme/pull/13).
- Use ``community.dns.wait_for_txt`` to speed up waiting for DNS challenges to propagate.
- acme_certificate - add ``acme_certificate_hosttech_token`` option to use HostTech's new JSON API instead of old WSDL API (https://github.com/felixfontein/ansible-acme/pull/12).
- acme_certificate - check whether credentials for DNS provider are set before starting certificate retrieval (https://github.com/felixfontein/ansible-acme/pull/12).

Breaking Changes / Porting Guide
--------------------------------

- Replace ``felixfontein.hosttech_dns`` and ``felixfontein.tools`` collection dependencies by ``community.dns >= 1.0.0`` and ``community.general >= 2.5.0``.
- acme_certificate role - remove usage of tags ``issue-tls-certs``, ``issue-tls-certs-newkey`` and ``verify-tls-certs``. By default, new private keys are generated. This can be disabled by setting ``acme_certificate_regenerate_private_keys`` to ``false`` (https://github.com/felixfontein/ansible-acme/pull/15).

Bugfixes
--------

- account_key_rollover role - when using sops-encrypted keys, ``community.sops.sops_encrypt`` was run on the remote node and not the controller node (https://github.com/felixfontein/ansible-acme/pull/7).

v0.2.0
======

Release Summary
---------------

Feature and repository maintenance release.

Minor Changes
-------------

- revoke_old_certificates role - allow to revoke by ACME account key instead of certificate private key by setting ``acme_certificate_revoke_with_acme_account`` to ``true``. This allows to revoke certificates with BuyPass, which does not support revocation by certificate private key.

v0.1.0
======

Release Summary
---------------

Initial release of my `acme_certificate <https://galaxy.ansible.com/felixfontein/acme_certificate>`_ role converted to a collection, with two new roles `revoke_old_certificates` and `account_key_rollover`.

New Roles
---------

- felixfontein.acme.account_key_rollover - Rollover for the ACME account key
- felixfontein.acme.acme_certificate - Retrieve a certificate for a set of domains and/or IP addresses
- felixfontein.acme.revoke_old_certificates - Revoke old certificates copied aside by acme_certificate
