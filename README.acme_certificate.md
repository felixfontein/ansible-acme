# Role felixfontein.acme.acme_certificate

This is an [Ansible](https://github.com/ansible/ansible) role which can use any CA supporting the ACME protocol, such as [Let's Encrypt](https://letsencrypt.org/), [Buypass](https://www.buypass.com/ssl/products/acme) or [ZeroSSL](https://zerossl.com/features/acme/), to issue TLS/SSL certificates for your server.

The main advantage of this approach over others is that *almost no code is executed on your webserver*: only when you use HTTP challenges, files need to be copied onto your webserver, and afterwards deleted from it. Everything else is executed on your local machine! In particular, the account key is *never* sent to another machine.

This role does not cover installing the certificates, you have to do that yourself in another role.

## Parameters

See [here](./README.general-parameters.md) for general parameters, and for challenge-specific parameters.

These are the main variables used by the `felixfontein.acme.acme_certificate` role:

- `acme_certificate_acme_email`: Your email address which shall be associated to the ACME account.
- `acme_certificate_algorithm`: The algorithm used for creating private keys. The default is `"rsa"`; other choices are `"p-256"`, `"p-384"` or `"p-521"` for the NIST elliptic curves `prime256v1`, `secp384r1` and `secp521r1`, respectively.
- `acme_certificate_key_length`: The bitlength to use for RSA private keys. The default is 4096.
- `acme_certificate_key_name`: The basename for storing the keys and certificates. The default is the first domain specified, with `*` replaced by `_`.
- `acme_certificate_keys_path`: Where the keys and certificates are stored. Default value is `"keys/"`.
- `acme_certificate_keys_old_path`: Where old keys and certificates should be copied to; used in case `acme_certificate_keys_old_store` is true. Default value is `"keys/old/"`.
- `acme_certificate_keys_old_store`: If set to `true`, will make copies of old keys and certificates. The copies will be stored in the directory specified by `acme_certificate_keys_old_store`. Default value is `false`.
- `acme_certificate_keys_old_prepend_timestamp`: Whether copies of old keys and certificates should be prepended by the current date and time. Default value is `false`.
- `acme_certificate_ocsp_must_staple`: Whether a certificate with the OCSP Must Staple extension is requested. Default value is `false`.
- `acme_certificate_terms_agreed`: Whether the terms of services are accepted or not. Default value is `false`, usually needs to be set explicitly to `true` to allow creating an ACME account. This is only used for ACME v2.
- `acme_certificate_challenge`: The challenge type to use. Should be `http-01` for HTTP challenges (needs access to web server) or `dns-01` for DNS challenges (needs access to DNS provider).
- `acme_certificate_root_certificate`: The root certificate for the ACME directory. Default value is `https://letsencrypt.org/certs/isrgrootx1.pem` for the root certificate of Let's Encrypt.
- `acme_certificate_deactivate_authzs`: Whether `authz`s (authorizations) should be deactivated afterwards. Default value is `true`. Set to `false` to be able to re-use `authz`s.
- `acme_certificate_modify_account`: Whether the ACME account should be created (if it doesn't exist) and the contact data (email address) should be updated. Default value is `true`. Set to `false` if you want to use the `community.crypto.acme_account` module to manage your ACME account (not done by this role).
- `acme_certificate_privatekey_mode`: Which file mode to use for the private key file. Default value is `"0600"`, which means read- and writeable by the owner, but not accessible by anyone else (except possibly `root`).
- `acme_certificate_select_chain`: Must be in the format described [here](https://docs.ansible.com/ansible/latest/collections/community/crypto/acme_certificate_module.html#parameter-select_chain). Allows to select the certificate chain to be used; `acme_certificate_root_certificate` must be used in conjunction. This can be used for example with [Let's Encrypt](https://community.letsencrypt.org/t/transition-to-isrgs-root-delayed-until-sep-29/125516) to select which root certificate to use. See below for concrete examples how to choose between the Let's Encrypt roots.

## Selecting which root to use with Let's Encrypt

The following configuration makes sure that the IdenTrust cross-signed intermediate is used, which is more compatible for example for older Android versions than the new IRSG root:
```.yaml
acme_certificate_root_certificate: https://letsencrypt.org/certs/trustid-x3-root.pem.txt
acme_certificate_select_chain:
  - test_certificates: last
    issuer:
      CN: DST Root CA X3
      O: Digital Signature Trust Co.
```
The following configuration selects the new IRSG X1 root:
```.yaml
acme_certificate_root_certificate: https://letsencrypt.org/certs/isrgrootx1.pem
acme_certificate_select_chain:
  - test_certificates: last
    issuer:
      CN: ISRG Root X1
      O: Internet Security Research Group
```

## Generated files

Let's assume you created TLS keys for `www.example.com`. You have to copy the relevant files to your webserver. The ansible role created the following files:

  * `keys/www.example.com.key`: this is the private key for the certificate. Ensure nobody can access it.
  * `keys/www.example.com.pem`: this is the certificate itself.
  * `keys/www.example.com-chain.pem`: this is the intermediate certificate(s) needed for a trust path.
  * `keys/www.example.com-fullchain.pem`: this is the certificate combined with the intermediate certificate(s).
  * `keys/www.example.com-rootchain.pem`: this is the intermediate certificate(s) combined with the root certificate. You might need this for OCSP stapling.
  * `keys/www.example.com-root.pem`: this is the root certificate of Let's Encrypt.

For configuring your webserver, you need the private key (`keys/www.example.com.key`), and either the certificate with intermediate certificate(s) combined in one file (`keys/www.example.com-fullchain.pem`), or the certificate and the intermediate certificate(s) as two separate files (`keys/www.example.com.pem` and `keys/www.example.com-chain.pem`). If you want to use [OCSP stapling](https://en.wikipedia.org/wiki/OCSP_stapling), you will also need `keys/www.example.com-rootchain.pem`.

To get these files onto your web server, you could add tasks as follows:
```.yaml
- name: copy private keys
  copy:
    src: keys/{{ item }}
    dest: /etc/ssl/private/
    owner: root
    group: root
    mode: "0400"
  with_items:
  - www.example.com.key
  notify: reload webserver

- name: copy certificates
  copy:
    src: keys/{{ item }}
    dest: /etc/ssl/server-certs/
    owner: root
    group: root
    mode: "0444"
  with_items:
  - www.example.com-rootchain.pem
  - www.example.com-fullchain.pem
  - www.example.com.pem
  notify: reload webserver
```

The webserver configuration could look as follows (for nginx):
```
server {
    listen www.example.com:443 ssl;  # IPv4: listen to IP www.example.com points to
    listen [::]:443 ssl;             # IPv6: listen to localhost
    server_name www.example.com;
    
    # Allowing only TLS 1.0 and 1.2, with a very selective amount of ciphers.
    # According to SSL Lab's SSL server test, this will block:
    #   - Android 2.3.7
    #   - IE 6 and 8 under Windows XP
    #   - Java 6, 7 and 8
    # If that's not acceptable for you, choose other cipher lists. Look for
    # example at https://wiki.mozilla.org/Security/Server_Side_TLS
    ssl_protocols TLSv1.2 TLSv1;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "-ALL !ADH !aNULL !EXP !EXPORT40 !EXPORT56 !RC4 !3DES !eNULL !NULL !DES !MD5 !LOW ECDHE-ECDSA-AES256-GCM-SHA384 ECDHE-RSA-AES256-GCM-SHA384 DHE-RSA-AES256-GCM-SHA384 ECDHE-ECDSA-AES256-SHA384 ECDHE-RSA-AES256-SHA384 DHE-RSA-AES256-SHA256 ECDHE-ECDSA-AES256-SHA ECDHE-RSA-AES256-SHA DHE-RSA-AES256-SHA";
    
    # The certificate chain sent to the browser, as well as the private key.
    # Make sure your private key is only accessible by the webserver during
    # configuration loading (which by default is done with user root).
    ssl_certificate /etc/ssl/server-certs/www.example.com-fullchain.pem;
    ssl_certificate_key /etc/ssl/private/www.example.com.key;
    
    # For OCSP stapling, we need a DNS resolver. Here only public Quad9 and
    # Google DNS servers are specified; I would prepent them by your hoster's
    # DNS servers. You can usually find their IPs in /etc/resolv.conf on your
    # webserver.
    resolver 9.9.9.9 8.8.8.8 8.8.4.4 valid=300s;
    resolver_timeout 10s;
    
    # Enabling OCSP stapling. Nginx will take care of retrieving the OCSP data
    # automatically. See https://wiki.mozilla.org/Security/Server_Side_TLS#OCSP_Stapling
    # for details on OCSP stapling.
    ssl_stapling on;
    ssl_stapling_verify on;
    ssl_trusted_certificate /etc/ssl/server-certs/www.example.com-rootchain.pem;
    
    # Enables a SSL session cache. Adjust the numbers depending on your site's usage.
    ssl_session_cache shared:SSL:50m;
    ssl_session_timeout 30m;
    ssl_session_tickets off;
    
    # You should only use HSTS with proper certificates; the ones from Let's Encrypt
    # are fine for this, self-signed ones are not. See MozillaWiki for more details:
    # https://wiki.mozilla.org/Security/Server_Side_TLS#HSTS:_HTTP_Strict_Transport_Security
    add_header Strict-Transport-Security "max-age=3155760000;";
    
    charset utf-8;
    
    access_log  /var/log/nginx/www.example.com.log combined;
    error_log  /var/log/nginx/www.example.com.log error;
    
    location / {
        root   /var/www/www.example.com;
        index  index.html;
    }
}
```

## Example playbook

This role can be used as follows. Note that it obtains several certificates, and defines variables used for all certificates globally:
```.yaml
---
- name: getting certificates for webserver
  hosts: webserver
  vars:
    acme_certificate_acme_account: 'keys/acme-account.key'
    acme_certificate_acme_email: 'mail@example.com'
    # For HTTP challenges:
    acme_certificate_server_location: '/var/www/challenges/'
    acme_certificate_http_challenge_user: root
    acme_certificate_http_challenge_group: http
    acme_certificate_http_challenge_folder_mode: "0750"
    acme_certificate_http_challenge_file_mode: "0640"
    # For DNS challenges with route53:
    acme_certificate_dns_provider: route53
    acme_certificate_aws_access_key: REPLACE_WITH_YOUR_ACCESS_KEY
    acme_certificate_aws_secret_key: REPLACE_WITH_YOUR_SECRET_KEY
    # For DNS challenges with ns1:
    # acme_certificate_dns_provider: ns1
    # acme_certificate_ns1_secret_key: REPLACE_WITH_YOUR_SECRET_KEY
  roles:
    - role: felixfontein.acme.acme_certificate
      acme_certificate_domains: ['example.com', 'www.example.com']
      # Use DNS challenges:
      acme_certificate_challenge: dns-01
      # The certificate files will be stored at:
      #    keys/example.com.key  (private key)
      #    keys/example.com.pem  (certificate)
      #    keys/example.com-chain.pem  (intermediate certificate)
      #    keys/example.com-fullchain.pem  (certificate with intermediate certificate)
      #    keys/example.com-root.pem  (root certificate)
      #    keys/example.com-rootchain.pem  (intermediate certificate with root certificate)
    - role: felixfontein.acme.acme_certificate
      acme_certificate_domains: ['another.example.com']
      acme_certificate_key_name: 'another.example.com-rsa'
      acme_certificate_key_length: 4096
      # Use HTTP challenges:
      acme_certificate_challenge: http-01
      # The certificate files will be stored at:
      #    keys/another.example.com-rsa.key  (private key)
      #    keys/another.example.com-rsa.pem  (certificate)
      #    keys/another.example.com-rsa-chain.pem  (intermediate certificate)
      #    keys/another.example.com-rsa-fullchain.pem  (certificate with intermediate certificate)
      #    keys/another.example.com-rsa-root.pem  (root certificate)
      #    keys/another.example.com-rsa-rootchain.pem  (intermediate certificate with root certificate)
    - role: felixfontein.acme.acme_certificate
      acme_certificate_domains: ['another.example.com']
      acme_certificate_key_name: 'another.example.com-ecc'
      acme_certificate_algorithm: 'p-256'
      # Use HTTP challenges (default for challenge is http-01).
      # The certificate files will be stored at:
      #    keys/another.example.com-ecc.key  (private key)
      #    keys/another.example.com-ecc.pem  (certificate)
      #    keys/another.example.com-ecc-chain.pem  (intermediate certificate)
      #    keys/another.example.com-ecc-fullchain.pem  (certificate with intermediate certificate)
      #    keys/another.example.com-ecc-root.pem  (root certificate)
      #    keys/another.example.com-ecc-rootchain.pem  (intermediate certificate with root certificate)
```
