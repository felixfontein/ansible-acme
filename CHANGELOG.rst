============================
Tools for ACME Release Notes
============================

.. contents:: Topics


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
