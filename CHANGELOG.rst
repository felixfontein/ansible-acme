============================
Tools for ACME Release Notes
============================

.. contents:: Topics


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
