============================
Tools for ACME Release Notes
============================

.. contents:: Topics


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
