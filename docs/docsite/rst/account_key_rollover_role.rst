.. _ansible_collections.felixfontein.acme.docsite.account_key_rollover_role:

felixfontein.acme.account_key_rollover role
===========================================

This is a role which can use any CA supporting the ACME protocol, such as `Let's Encrypt <https://letsencrypt.org/>`_, `Buypass <https://www.buypass.com/ssl/products/acme>`_ or `ZeroSSL <https://zerossl.com/features/acme/>`_, to rekey ACME account keys.

This role will create a backup copy of the existing account key if requested to do so, re-create the account key, and then roll over the ACME account to the new key.

Parameters
----------

See :ref:`ansible_collections.felixfontein.acme.docsite.general_role_parameters` for general parameters. Note that for this role, ``acme_certificate_acme_account_content`` is **not** supported.

These are the main variables used by this role:

- ``acme_certificate_account_algorithm``: The algorithm used for creating private keys. The default is ``"rsa"``; other choices are ``"p-256"``, ``"p-384"`` or ``"p-521"`` for the NIST elliptic curves ``prime256v1``, ``secp384r1`` and ``secp521r1``, respectively.
- ``acme_certificate_account_key_length``: The bitlength to use for RSA private keys. The default is 4096.
- ``acme_certificate_account_key_backup``: Whether to create a backup of the old account key before rolling over. Default value is ``true``.
- ``acme_certificate_account_key_sops_encrypted``: Use `Mozilla sops <https://github.com/mozilla/sops>`_ to encrypt private key. Needs ``.sops.yaml`` file inside the keys directory or somewhere up the directory chain. Default value is ``false``.

Example playbook
----------------

This role can be used as follows. Note that it obtains several certificates, and defines variables used for all certificates globally:

.. code-block:: yaml+jinja

    ---
    - name: account key rollover
      hosts: webserver
      vars:
        acme_certificate_acme_account: 'keys/acme-account.key'
      roles:
        - role: felixfontein.acme.account_key_rollover
          acme_certificate_account_key_backup: false
