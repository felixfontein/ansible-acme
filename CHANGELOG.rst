============================
Tools for ACME Release Notes
============================

.. contents:: Topics

v0.10.1
=======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- Avoid deprecation message with ansible-core 2.19 when creating or removing DNS entries (https://github.com/felixfontein/ansible-acme/pull/100).
- acme_certificate role - if ``acme_certificate_dns_provider=cloudflare``, DNS entries were created on all targets instead of only on localhost (https://github.com/felixfontein/ansible-acme/pull/97).

v0.10.0
=======

Release Summary
---------------

Feature release.

Minor Changes
-------------

- The collection now depends on community.crypto 2.24.0 or newer (https://github.com/felixfontein/ansible-acme/pull/86).
- acme_certificate role - add support for Hetzner's DNS (https://github.com/felixfontein/ansible-acme/pull/87).
- acme_certificate role - now uses the new ``community.crypto.acme_account_order_*`` modules added in community.crypto 2.24.0 (https://github.com/felixfontein/ansible-acme/pull/86).
- acme_certificate role - support ACME profile selection with the ``acme_certificate_profile`` parameter (https://github.com/felixfontein/ansible-acme/pull/86).
- acme_certificate role - support determining whether to renew by remaining percentage of the validity period (``acme_certificate_renewal_on_remaining_percentage`` option) or ARI information (``acme_certificate_use_ari`` option) (https://github.com/felixfontein/ansible-acme/pull/86).

Breaking Changes / Porting Guide
--------------------------------

- acme_certificate role - the role no longer supports ``acme_certificate_acme_version == 1``. ACME v2 must always be used (https://github.com/felixfontein/ansible-acme/pull/86).

Security Fixes
--------------

- acme_certificate role - properly apply ``no_log: true`` to task that reads private key file for backup. When not using SOPS encrypted private keys, the private key was visible in verbose mode or in the logs in plain text (https://github.com/felixfontein/ansible-acme/pull/86).

v0.9.0
======

Release Summary
---------------

Feature release.

Minor Changes
-------------

- The dependency on community.dns has been bumped to >= 2.9.0 to be able to use the ``community.dns.quote_txt`` filter when using the Route53 module (https://github.com/felixfontein/ansible-acme/pull/76).
- acme_certificate role - allow to configure the timeout and the DNS servers to use for validating DNS entry propagation for ``dns-01`` challenges (https://github.com/felixfontein/ansible-acme/issues/79, https://github.com/felixfontein/ansible-acme/pull/80).

v0.8.1
======

Release Summary
---------------

Maintenance release with slightly updated documentation and no functional changes.

v0.8.0
======

Release Summary
---------------

Feature release with improved creation of DNS records for Route53 and Hosttech.

Major Changes
-------------

- The collection now depends on community.aws >= 6.3.0 and amazon.aws >= 6.3.0 to improve stability of the acme_certificate role with Amazon's Route 53 DNS (https://github.com/felixfontein/ansible-acme/pull/62).

Minor Changes
-------------

- acme_certificate role - increase maximum wait for Hosttech DNS records from 2 to 5 minutes (https://github.com/felixfontein/ansible-acme/pull/64).
- acme_certificate role - use community.aws.route53_wait instead of community.dns.wait_for_txt when using Amazon's Route 53 DNS to improve stability (https://github.com/felixfontein/ansible-acme/issues/57, https://github.com/felixfontein/ansible-acme/pull/62).

v0.7.0
======

Release Summary
---------------

New major release dropping compatibility with old Ansible versions, namely Ansible 2.9 and ansible-base 2.10.

Minor Changes
-------------

- acme_certificate role - add Cloudflare DNS support (https://github.com/felixfontein/ansible-acme/pull/55).

Breaking Changes / Porting Guide
--------------------------------

- Drop compatibility for Ansible 2.9 and ansible-base 2.10. These versions of Ansible/ansible-base have been End of Life for some time now. If you are still using them, either stick to an older version of this collection, or upgrade to a newer version of ansible-core/Ansible (https://github.com/felixfontein/ansible-acme/pull/54).

v0.6.0
======

Release Summary
---------------

Collection dependency update with bugfixes and new features.

Minor Changes
-------------

- acme_certificate role - add new option ``acme_certificate_dns_substitution`` to allow substituting DNS names during DNS record creation for use with CNAMEs (https://github.com/felixfontein/ansible-acme/pull/41).
- acme_certificate role - added new option ``acme_certificate_verify_auth`` which allows to turn of validation that credentials for DNS modules are passed as role arguments. When disabled, you are responsible to pass credentials with module defaults or in other ways supported by the specific modules (https://github.com/felixfontein/ansible-acme/issues/40, https://github.com/felixfontein/ansible-acme/pull/42).

Breaking Changes / Porting Guide
--------------------------------

- The collection no longer depends on community.aws >= 1.0.0, but on amazon.aws >= 5.0.0. The community.aws.route53 module was migrated to amazon.aws, which allows us to depend on one collection less. Note that if you use this collection with Ansible, you need Ansible 7.0.0 or newer; also note that Ansible 6.x.0 and before are End of Life by now (https://github.com/felixfontein/ansible-acme/pull/39).

Bugfixes
--------

- Avoid double failure of acme_certificate rescue task when first task in block fails (https://github.com/felixfontein/ansible-acme/pull/38).

New Plugins
-----------

Filter
~~~~~~

- felixfontein.acme._substitute_dns - [INTERNAL] Adjust DNS name according to a CNAME substitution map

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

Initial release of my `acme_certificate <https://galaxy.ansible.com/ui/repo/published/felixfontein/acme_certificate>`_ role converted to a collection, with two new roles `revoke_old_certificates` and `account_key_rollover`.

New Roles
---------

- felixfontein.acme.account_key_rollover - Rollover for the ACME account key
- felixfontein.acme.acme_certificate - Retrieve a certificate for a set of domains and/or IP addresses
- felixfontein.acme.revoke_old_certificates - Revoke old certificates copied aside by acme_certificate
