.. _ansible_collections.felixfontein.acme.docsite.general_role_parameters:

General Role Parameters
=======================

These are the main variables used by the roles:

- ``acme_certificate_acme_account``: Path to the private ACME account key. Either this or ``acme_certificate_acme_account_content`` must always be specified. See :ref:`ansible_collections.felixfontein.acme.docsite.acme_account` for information on creating one.
- ``acme_certificate_acme_account_content``: Content of the private ACME account key. Either this or ``acme_certificate_acme_account`` must always be specified.
- ``acme_certificate_acme_account_uri``: Instead of determining the account URI from the account key, assumes the given account URI. Optional.
- ``acme_certificate_acme_directory``: The ACME directory to use. Default is ``https://acme-v02.api.letsencrypt.org/directory``, which is the current production ACME v2 endpoint of Let's Encrypt.
- ``acme_certificate_acme_version``: The ACME directory's version. Default is 2.

Role parameters for challenges
------------------------------

These are needed by :ref:`ansible_collections.felixfontein.acme.docsite.acme_certificate_role`.

HTTP Challenges
^^^^^^^^^^^^^^^

For HTTP challenges, the following variables define how the challenges can be put onto the (remote) webserver:

- ``acme_certificate_server_location``: Location where ``.well-known/acme-challenge/`` will be served from. Default is ``/var/www/challenges``.
- ``acme_certificate_http_become``: Argument for ``become:`` for the ``file`` and ``copy`` tasks. Default value is ``false``.
- ``acme_certificate_http_challenge_user``: The user the challenge files are owned by. Default value is ``root``.
- ``acme_certificate_http_challenge_group``: The group the challenge files are owned by. Default value is ``http``.
- ``acme_certificate_http_challenge_folder_mode``: The mode to use for the challenge folder. Default value is ``'0750'`` (octal string).
- ``acme_certificate_http_challenge_file_mode``: The mode to use for the challenge files. Default value is ``'0640'`` (octal string).

The following subsection shows how to configure `nginx <https://nginx.org/>`_ for HTTP challenges. Configuring other webservers can be done in a similar way.

Nginx configuration
~~~~~~~~~~~~~~~~~~~

Assume that for one of your TLS/SSL protected domains, you use a HTTP-to-HTTPS redirect. Let's assume it looks like this:

.. code-block:: nginx

    server {
        listen       example.com:80;
        server_name  example.com *.example.com;
        return 301   https://www.example.com$request_uri;
    }

To allow the :ref:`ansible_collections.felixfontein.acme.docsite.acme_certificate_role` role to put something at ``http://*.example.com/.well-known/acme-challenge/``, you can change this to:

.. code-block:: nginx

    server {
        listen       example.com:80;
        server_name  example.com *.example.com;
        location /.well-known/acme-challenge/ {
            alias /var/www/challenges/;
            try_files $uri =404;
        }
        location / {
            return 301   https://www.example.com$request_uri;
        }
    }

With this nginx config, all other URLs on ``*.example.com`` and ``example.com`` are still redirected, while everything in ``*.example.com/.well-known/acme-challenge/`` is served from ``/var/www/challenges``. When adjusting the location of ``/var/www/challenges``, you must also change ``acme_certificate_server_location``.

You can even improve on this by redirecting all URLs in ``*.example.com/.well-known/acme-challenge/`` which do not resolve to a valid file in ``/var/www/challenges`` to your HTTPS server as well. One way to do this is:

.. code-block:: nginx

    server {
        listen       example.com:80;
        server_name  example.com *.example.com;
        location /.well-known/acme-challenge/ {
            alias /var/www/lechallenges/;
            try_files $uri @forward_https;
        }
        location @forward_https {
            return 301   https://www.example.com$request_uri;
        }
        location / {
            return 301   https://www.example.com$request_uri;
        }
    }

With this config, if ``/var/www/challenges/`` is empty, your HTTP server will behave as if the ``/.well-known/acme-challenge/`` location isn't specified.

DNS Challenges
^^^^^^^^^^^^^^

If DNS challenges are used, the following variables define how the challenges can be fulfilled:

- ``acme_certificate_dns_provider``: must be one of ``route53``, ``hosttech``, ``ns1``, and ``inwx``. Each needs more information:
  - For ``route53`` (`Amazon Route 53 <https://aws.amazon.com/route53/>`_), the credentials must be passed as ``acme_certificate_aws_access_key`` and ``acme_certificate_aws_secret_key``.
  - For ``hosttech`` (`hosttech GmbH <https://www.hosttech.ch/>`_), the credentials have to be passed as ``acme_certificate_hosttech_username`` and ``acme_certificate_hosttech_password`` for using the old WSDL API, and ``acme_certificate_hosttech_token`` for the new JSON API.
  - For ``ns1`` (`ns1.com <https://ns1.com>`_) the key for your API account must be passed as ``acme_certificate_ns1_secret_key``. Also it depends on external module ``ns1_record``. See below for instructions on how to install these modules.
  - For ``inwx`` (`inwx.de <https://inwx.de>`_) the credentials have to be passed as ``acme_certificate_inwx_username`` and ``acme_certificate_inwx_password``. Please keep in mind that 2FA (two factor authentication) is currently not supported and needs do be disabled. Related Issue: (`inwx/ansible-collection#3 <https://github.com/inwx/ansible-collection/issues/3>`_)

Please note that the DNS challenge code is not perfect. The Route 53, Hosttech, NS1, and INWX functionality has been tested.

Setting up NS1 modules
~~~~~~~~~~~~~~~~~~~~~~

For ``ns1`` (`ns1.com <https://ns1.com>`_) the external ``ns1_record`` module needs to be installed. Assuming default directory structure and settings, you may need to download two files into machine where the playbook is executed:

.. code-block:: bash

    curl --create-dirs -L -o ~/.ansible/plugins/module_utils/ns1.py https://github.com/ns1/ns1-ansible-modules/raw/master/module_utils/ns1.py
    curl --create-dirs -L -o ~/.ansible/plugins/modules/ns1_record.py https://github.com/ns1/ns1-ansible-modules/raw/master/library/ns1_record.py

Once NS1 converts their `set of modules <https://github.com/ns1/ns1-ansible-modules>`_ into a `collection <https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html>`_, it will become a lot easier to install and use them (`NS1 tracking issue <https://github.com/ns1/ns1-ansible-modules/issues/32>`_).

Setting up INWX modules
~~~~~~~~~~~~~~~~~~~~~~~

For ``inwx`` (`inwx.de <https://inwx.de>`_) the available Ansible Galaxy collection ``inwx.collection`` (`galaxy.ansible.com <https://galaxy.ansible.com/inwx/collection>`_) needs to be installed.
  
It is as simple as: ``ansible-galaxy collection install inwx.collection``
