# Role felixfontein.acme.account_key_rollover

This is an [Ansible](https://github.com/ansible/ansible) role which can use any CA supporting the ACME protocol, such as [Let's Encrypt](https://letsencrypt.org/), [Buypass](https://www.buypass.com/ssl/products/acme) or [ZeroSSL](https://zerossl.com/features/acme/), to rekey ACME account keys.

This role will create a backup copy of the existing account key if requested to do so, re-create the account key, and then roll over the ACME account to the new key.

## Parameters

See [here](./README.general-parameters.md) for general parameters. Note that for this role, `acme_certificate_acme_account_content` is **not** supported.

These are the main variables used by the `felixfontein.acme.account_key_rollover` role:

- `acme_certificate_account_algorithm`: The algorithm used for creating private keys. The default is `"rsa"`; other choices are `"p-256"`, `"p-384"` or `"p-521"` for the NIST elliptic curves `prime256v1`, `secp384r1` and `secp521r1`, respectively.
- `acme_certificate_account_key_length`: The bitlength to use for RSA private keys. The default is 4096.
- `acme_certificate_account_key_backup`: Whether to create a backup of the old account key before rolling over. Default value is `true`.
- `acme_certificate_account_key_sops_encrypted`: Use [Mozilla sops](https://github.com/mozilla/sops) to encrypt private key. Needs `.sops.yaml` file inside the keys directory or somewhere up the directory chain. Default value is `false`.

## Example playbook

This role can be used as follows. Note that it obtains several certificates, and defines variables used for all certificates globally:
```.yaml
---
- name: account key rollover
  hosts: webserver
  vars:
    acme_certificate_acme_account: 'keys/acme-account.key'
  roles:
    - role: felixfontein.acme.account_key_rollover
      acme_certificate_account_key_backup: false
```
