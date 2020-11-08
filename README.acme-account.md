# ACME Accounts

To work with ACME servers, you need an account. For an account, you always need a private key. We always assume it is stored at a place where the `acme_certificate_acme_account` variable points to, or it is provided with the `acme_certificate_acme_account_content` variable ([more information on general parameters](./README.general-parameters.md)). The next subsections describe how to create or convert one.

For some ACME servers such as the ones by Let's Encrypt and Buypass, an account can be created on-the-fly while using for example the `felixfontein.acme.acme_certificate` role. The following options are of interest:
- `acme_certificate_acme_email`: Your email address which shall be associated to the ACME account.
- `acme_certificate_terms_agreed`: Whether the terms of services are accepted or not. Default value is `false`, usually needs to be set explicitly to `true` to allow creating an ACME account. This is only used for ACME v2.
- `acme_certificate_modify_account`: Whether the ACME account should be created (if it doesn't exist) and the contact data (email address) should be updated. Default value is `true`. Set to `false` if you want to use the `community.crypto.acme_account` module to manage your ACME account manually, and prevent accidental modification of the contact information.

The following shows how to create an account manually with two contact email addresses, which is not possible when using the role:
```.yaml
- name: Create ACME account
  community.crypto.acme_account:
    acme_directory: "{{ acme_certificate_acme_directory }}"
    acme_version: "{{ acme_certificate_acme_version }}"
    account_key: "{{ acme_certificate_acme_account | default(omit) }}"
    account_key_content: "{{ acme_certificate_acme_account_content | default(omit) }}"
    state: present
    contact:
    - "mailto:me@example.com"
    - "mailto:me@example.org"
    terms_agreed: yes
```

For ACME servers that need External Account Binding, for example for ZeroSSL or Sectigo, you must always use `community.crypto.acme_account` to set up the account manually. This can look for example like this:
```.yaml
- acme_account:
    acme_directory: "{{ acme_certificate_acme_directory }}"
    acme_version: "{{ acme_certificate_acme_version }}"
    account_key: "{{ acme_certificate_acme_account | default(omit) }}"
    account_key_content: "{{ acme_certificate_acme_account_content | default(omit) }}"
    state: present
    contact:
    - "mailto:me@example.com"
    - "mailto:me@example.org"
    terms_agreed: true
    external_account_binding:
      kid: abcdef0123456789abcdef
      alg: HS256
      key: aBzFf13298sadsfalkj345nnsfaflkj5lkj245lkj324lkjlkjasflklkjatlkj354lkj43lkj54
```
The values for `kid` and `key` will be provided by the ACME server operator, for example in the ZeroSSL account interface. The value for `alg` is usually `HS256` if not explicitly mentioned.

## Account Key Setup

You can create an account key using the `openssl` binary as follows:
```.sh
# RSA 4096 bit key
openssl genrsa 4096 -out keys/acme-account.key
# ECC 256 bit key (P-256)
openssl ecparam -name prime256v1 -genkey -out keys/acme-account.key
# ECC 384 bit key (P-384)
openssl ecparam -name secp384r1 -genkey -out keys/acme-account.key
```

With Ansible, you can use the `openssl_privatekey` module as follows:
```.yaml
- name: Generate RSA 4096 key
  openssl_privatekey:
    path: keys/acme-account.key
    type: RSA
    size: 4096
- name: Generate ECC 256 bit key (P-256)
  openssl_privatekey:
    path: keys/acme-account.key
    type: ECC
    curve: secp256r1
- name: Generate ECC 384 bit key (P-384)
  openssl_privatekey:
    path: keys/acme-account.key
    type: ECC
    curve: secp384r1
```

Make sure you store the account key safely. As opposed to certificate private keys, there is no need to regenerate it frequently, and it makes recovation of certificates issued with it very simple if you no longer have the certificate's private key.

## Account key conversion

Note that the Ansible ACME modules expect the Let's Encrypt account key to be in PEM format and not in JWK format, which is used by the [official Let's Encrypt client certbot](https://github.com/certbot/certbot). If you have created an account key with the official client and now want to use this key with this ansible role, you have to convert it. One tool which can do this is [pem-jwk](https://github.com/dannycoates/pem-jwk).
