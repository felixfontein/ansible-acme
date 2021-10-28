.. _ansible_collections.felixfontein.acme.docsite.requirements:

Requirements
============

The collection requires the Python `cryptography <https://pypi.org/project/cryptography/>`_ library installed on the controller, available to the Python version used to execute the playbook. If ``cryptography`` is not installed, a recent enough version of `PyOpenSSL <https://pypi.org/project/pyOpenSSL/>`_ is currently supported as a fallback by the :ref:`community.crypto.openssl_privatekey <ansible_collections.community.crypto.openssl_privatekey_module>` and :ref:`community.crypto.openssl_csr <ansible_collections.community.crypto.openssl_csr_module>` modules.

The ``openssl`` binary must also be available in the executable path on the controller. It is needed by the :ref:`community.crypto.acme_certificate <ansible_collections.community.crypto.acme_certificate_module>` module in case ``cryptography`` is not installed, and it is used for certificate chain validation.

If DNS challenges are used, there can be other requirements depending on the DNS provider. For example, for Amazon's Route 53, the Ansible :ref:`community.aws.route53 <ansible_collections.community.aws.route53_module>` requires the Python `boto <https://pypi.org/project/boto/>`_ package. If Hosttech DNS challenges are used, the `lxml <https://pypi.org/project/lxml/>`_ package needs to be installed. If DNS challenges with NS1 or INWX are used, the corrosponding modules must be installed. See below for more information.
