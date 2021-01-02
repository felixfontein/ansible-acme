# Role felixfontein.acme.revoke_old_certificates

This is an [Ansible](https://github.com/ansible/ansible) role which can use any CA supporting the ACME protocol, such as [Let's Encrypt](https://letsencrypt.org/), [Buypass](https://www.buypass.com/ssl/products/acme) or [ZeroSSL](https://zerossl.com/features/acme/), to revoke issued TLS/SSL certificates for your server.

This role assumes that `felixfontein.acme.acme_certificate` has been used with `acme_certificate_keys_old_store` set to `true`. It copies the old certificate into `keys/old/` (or the path configured by `acme_certificate_keys_old_path`) before renewal. This role iterates over all certificates (resp. their private keys) in this directory and revokes them all with the given reason. This role supports both plaintext private keys and sops-encrypted private keys (see `acme_certificate_use_sops_for_key` option of `felixfontein.acme.acme_certificate`).

Make sure that you first replace all usages of the old certificates by the new ones before revokation!

## Parameters

See [here](./README.general-parameters.md) for general parameters, and for challenge-specific parameters. Please note that this role does **not** need an ACME account if not explicitly configured to use it, and relies on the private key of the certificates to revoke them.

These are the main variables used by the `felixfontein.acme.revoke_old_certificates` role:

- `acme_certificate_keys_old_path`: Where old keys and certificates should be copied to; used in case `acme_certificate_keys_old_store` is true. Default value is `"keys/old/"`.
- `acme_certificate_revoke_reason`: which reason to use for revocation. The default value is `4` (superseeded, i.e. you issued a new certificate for the same set of domains, this is an old one). Other sensible values are `5` (cessation of operation, i.e. you don't want to use this set of domain names in a certificate anymore). See [here](https://docs.ansible.com/ansible/latest/collections/community/crypto/acme_certificate_revoke_module.html#parameter-revoke_reason) for a full list of reasons.
- `acme_certificate_revoke_with_acme_account`: if set to `true`, will not use the private key of the certificate to revoke, but the account key. This is needed for ACME providers which do not support revocation by private certificate key, like BuyPass.

## Example playbook

This role can be used as follows. Note that it obtains several certificates, and defines variables used for all certificates globally:
```.yaml
---
- name: revoking old certificates
  hosts: webserver
  roles:
    - role: felixfontein.acme.revoke_old_certificates
      acme_certificate_revoke_reason: 4
```
