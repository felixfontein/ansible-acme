# Tools for ACME Release Notes

**Topics**

- <a href="#v0-9-0">v0\.9\.0</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#minor-changes">Minor Changes</a>
- <a href="#v0-8-1">v0\.8\.1</a>
    - <a href="#release-summary-1">Release Summary</a>
- <a href="#v0-8-0">v0\.8\.0</a>
    - <a href="#release-summary-2">Release Summary</a>
    - <a href="#major-changes">Major Changes</a>
    - <a href="#minor-changes-1">Minor Changes</a>
- <a href="#v0-7-0">v0\.7\.0</a>
    - <a href="#release-summary-3">Release Summary</a>
    - <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
- <a href="#v0-6-0">v0\.6\.0</a>
    - <a href="#release-summary-4">Release Summary</a>
    - <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-1">Breaking Changes / Porting Guide</a>
    - <a href="#bugfixes">Bugfixes</a>
    - <a href="#new-plugins">New Plugins</a>
        - <a href="#filter">Filter</a>
- <a href="#v0-5-2">v0\.5\.2</a>
    - <a href="#release-summary-5">Release Summary</a>
- <a href="#v0-5-1">v0\.5\.1</a>
    - <a href="#release-summary-6">Release Summary</a>
    - <a href="#bugfixes-1">Bugfixes</a>
- <a href="#v0-5-0">v0\.5\.0</a>
    - <a href="#release-summary-7">Release Summary</a>
    - <a href="#minor-changes-4">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-2">Breaking Changes / Porting Guide</a>
- <a href="#v0-4-0">v0\.4\.0</a>
    - <a href="#release-summary-8">Release Summary</a>
    - <a href="#minor-changes-5">Minor Changes</a>
- <a href="#v0-3-1">v0\.3\.1</a>
    - <a href="#release-summary-9">Release Summary</a>
    - <a href="#bugfixes-2">Bugfixes</a>
- <a href="#v0-3-0">v0\.3\.0</a>
    - <a href="#release-summary-10">Release Summary</a>
    - <a href="#minor-changes-6">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-3">Breaking Changes / Porting Guide</a>
    - <a href="#bugfixes-3">Bugfixes</a>
- <a href="#v0-2-0">v0\.2\.0</a>
    - <a href="#release-summary-11">Release Summary</a>
    - <a href="#minor-changes-7">Minor Changes</a>
- <a href="#v0-1-0">v0\.1\.0</a>
    - <a href="#release-summary-12">Release Summary</a>
    - <a href="#new-roles">New Roles</a>

<a id="v0-9-0"></a>
## v0\.9\.0

<a id="release-summary"></a>
### Release Summary

Feature release\.

<a id="minor-changes"></a>
### Minor Changes

* The dependency on community\.dns has been bumped to \>\= 2\.9\.0 to be able to use the <code>community\.dns\.quote\_txt</code> filter when using the Route53 module \([https\://github\.com/felixfontein/ansible\-acme/pull/76](https\://github\.com/felixfontein/ansible\-acme/pull/76)\)\.
* acme\_certificate role \- allow to configure the timeout and the DNS servers to use for validating DNS entry propagation for <code>dns\-01</code> challenges \([https\://github\.com/felixfontein/ansible\-acme/issues/79](https\://github\.com/felixfontein/ansible\-acme/issues/79)\, [https\://github\.com/felixfontein/ansible\-acme/pull/80](https\://github\.com/felixfontein/ansible\-acme/pull/80)\)\.

<a id="v0-8-1"></a>
## v0\.8\.1

<a id="release-summary-1"></a>
### Release Summary

Maintenance release with slightly updated documentation and no functional changes\.

<a id="v0-8-0"></a>
## v0\.8\.0

<a id="release-summary-2"></a>
### Release Summary

Feature release with improved creation of DNS records for Route53 and Hosttech\.

<a id="major-changes"></a>
### Major Changes

* The collection now depends on community\.aws \>\= 6\.3\.0 and amazon\.aws \>\= 6\.3\.0 to improve stability of the acme\_certificate role with Amazon\'s Route 53 DNS \([https\://github\.com/felixfontein/ansible\-acme/pull/62](https\://github\.com/felixfontein/ansible\-acme/pull/62)\)\.

<a id="minor-changes-1"></a>
### Minor Changes

* acme\_certificate role \- increase maximum wait for Hosttech DNS records from 2 to 5 minutes \([https\://github\.com/felixfontein/ansible\-acme/pull/64](https\://github\.com/felixfontein/ansible\-acme/pull/64)\)\.
* acme\_certificate role \- use community\.aws\.route53\_wait instead of community\.dns\.wait\_for\_txt when using Amazon\'s Route 53 DNS to improve stability \([https\://github\.com/felixfontein/ansible\-acme/issues/57](https\://github\.com/felixfontein/ansible\-acme/issues/57)\, [https\://github\.com/felixfontein/ansible\-acme/pull/62](https\://github\.com/felixfontein/ansible\-acme/pull/62)\)\.

<a id="v0-7-0"></a>
## v0\.7\.0

<a id="release-summary-3"></a>
### Release Summary

New major release dropping compatibility with old Ansible versions\, namely Ansible 2\.9 and ansible\-base 2\.10\.

<a id="minor-changes-2"></a>
### Minor Changes

* acme\_certificate role \- add Cloudflare DNS support \([https\://github\.com/felixfontein/ansible\-acme/pull/55](https\://github\.com/felixfontein/ansible\-acme/pull/55)\)\.

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

* Drop compatibility for Ansible 2\.9 and ansible\-base 2\.10\. These versions of Ansible/ansible\-base have been End of Life for some time now\. If you are still using them\, either stick to an older version of this collection\, or upgrade to a newer version of ansible\-core/Ansible \([https\://github\.com/felixfontein/ansible\-acme/pull/54](https\://github\.com/felixfontein/ansible\-acme/pull/54)\)\.

<a id="v0-6-0"></a>
## v0\.6\.0

<a id="release-summary-4"></a>
### Release Summary

Collection dependency update with bugfixes and new features\.

<a id="minor-changes-3"></a>
### Minor Changes

* acme\_certificate role \- add new option <code>acme\_certificate\_dns\_substitution</code> to allow substituting DNS names during DNS record creation for use with CNAMEs \([https\://github\.com/felixfontein/ansible\-acme/pull/41](https\://github\.com/felixfontein/ansible\-acme/pull/41)\)\.
* acme\_certificate role \- added new option <code>acme\_certificate\_verify\_auth</code> which allows to turn of validation that credentials for DNS modules are passed as role arguments\. When disabled\, you are responsible to pass credentials with module defaults or in other ways supported by the specific modules \([https\://github\.com/felixfontein/ansible\-acme/issues/40](https\://github\.com/felixfontein/ansible\-acme/issues/40)\, [https\://github\.com/felixfontein/ansible\-acme/pull/42](https\://github\.com/felixfontein/ansible\-acme/pull/42)\)\.

<a id="breaking-changes--porting-guide-1"></a>
### Breaking Changes / Porting Guide

* The collection no longer depends on community\.aws \>\= 1\.0\.0\, but on amazon\.aws \>\= 5\.0\.0\. The community\.aws\.route53 module was migrated to amazon\.aws\, which allows us to depend on one collection less\. Note that if you use this collection with Ansible\, you need Ansible 7\.0\.0 or newer\; also note that Ansible 6\.x\.0 and before are End of Life by now \([https\://github\.com/felixfontein/ansible\-acme/pull/39](https\://github\.com/felixfontein/ansible\-acme/pull/39)\)\.

<a id="bugfixes"></a>
### Bugfixes

* Avoid double failure of acme\_certificate rescue task when first task in block fails \([https\://github\.com/felixfontein/ansible\-acme/pull/38](https\://github\.com/felixfontein/ansible\-acme/pull/38)\)\.

<a id="new-plugins"></a>
### New Plugins

<a id="filter"></a>
#### Filter

* felixfontein\.acme\.\_substitute\_dns \- \[INTERNAL\] Adjust DNS name according to a CNAME substitution map

<a id="v0-5-2"></a>
## v0\.5\.2

<a id="release-summary-5"></a>
### Release Summary

Maintenance release\.

<a id="v0-5-1"></a>
## v0\.5\.1

<a id="release-summary-6"></a>
### Release Summary

Bugfix release\.

<a id="bugfixes-1"></a>
### Bugfixes

* When cleaning up after failures in the <code>acme\_certificate</code> role\, make sure that an undefined <code>ansible\_failed\_task</code> does not cause another error \([https\://github\.com/felixfontein/ansible\-acme/pull/32](https\://github\.com/felixfontein/ansible\-acme/pull/32)\)\.

<a id="v0-5-0"></a>
## v0\.5\.0

<a id="release-summary-7"></a>
### Release Summary

Feature release dropping support for some specific old Ansible/ansible\-base versions\.

<a id="minor-changes-4"></a>
### Minor Changes

* In case an error happens before a certificate is issued\, restore private key\, and remove certificate and key backups if these were made \(<code>acme\_certificate\_keys\_old\_store</code> option\) \([https\://github\.com/felixfontein/ansible\-acme/pull/30](https\://github\.com/felixfontein/ansible\-acme/pull/30)\)\.
* The collection repository conforms to the [REUSE specification](https\://reuse\.software/spec/) \([https\://github\.com/felixfontein/ansible\-acme/pull/30](https\://github\.com/felixfontein/ansible\-acme/pull/30)\)\.
* Use FQCN for builtin actions and lookup plugins \([https\://github\.com/felixfontein/ansible\-acme/pull/23](https\://github\.com/felixfontein/ansible\-acme/pull/23)\)\.
* acme\_certificate role \- add <code>acme\_certificate\_renewal\_on\_remaining\_days</code> option which allows to only renew certificates that expire in a certain amount of days \([https\://github\.com/felixfontein/ansible\-acme/pull/28](https\://github\.com/felixfontein/ansible\-acme/pull/28)\)\.

<a id="breaking-changes--porting-guide-2"></a>
### Breaking Changes / Porting Guide

* Officially drop support for Ansible 2\.9\.10 to 2\.9\.16\, and ansible\-base 2\.10\.0 to 2\.10\.3\. These versions did not work with the <code>felixfontein\.acme\.acme\_certificate</code> role for some time now\, so this should not really affect any regular user of this collection \([https\://github\.com/felixfontein/ansible\-acme/pull/23](https\://github\.com/felixfontein/ansible\-acme/pull/23)\)\.

<a id="v0-4-0"></a>
## v0\.4\.0

<a id="release-summary-8"></a>
### Release Summary

This release bumps some requirements and adds some features\.

<a id="minor-changes-5"></a>
### Minor Changes

* The collection now requires community\.dns \>\= 2\.0\.0 for Hosttech DNS support\.
* The collection now requires community\.general \>\= 4\.0\.0\.
* acme\_certificate role \- an alternative root certificate URL can be specified in <code>acme\_certificate\_root\_certificate\_for\_verification</code> that is only used for validating the retrieved chain \([https\://github\.com/felixfontein/ansible\-acme/pull/22](https\://github\.com/felixfontein/ansible\-acme/pull/22)\)\.
* acme\_certificate role \- the role can now handle the DNS provider INWX \([https\://github\.com/felixfontein/ansible\-acme/pull/19](https\://github\.com/felixfontein/ansible\-acme/pull/19)\)\.

<a id="v0-3-1"></a>
## v0\.3\.1

<a id="release-summary-9"></a>
### Release Summary

Update dependencies\.

<a id="bugfixes-2"></a>
### Bugfixes

* Hosttech DNS support\: restrict required version of community\.dns to \< 2\.0\.0\. A later version will bump the requirement to \>\= 2\.0\.0 and switch to the new API\.

<a id="v0-3-0"></a>
## v0\.3\.0

<a id="release-summary-10"></a>
### Release Summary

Major revamp of the collection with new dependencies\, better documentation\, and several features and bugfixes\.

<a id="minor-changes-6"></a>
### Minor Changes

* Add documentation for the roles to the [collection\'s docsite](https\://ansible\.fontein\.de/collections/felixfontein/acme/) \([https\://github\.com/felixfontein/ansible\-acme/pull/9](https\://github\.com/felixfontein/ansible\-acme/pull/9)\)\.
* Adding support for ansible\-core\'s new role argument spec feature\. This makes ansible\-core 2\.11\.1 or newer validate the parameters passed to the roles in this collection \([https\://github\.com/felixfontein/ansible\-acme/pull/13](https\://github\.com/felixfontein/ansible\-acme/pull/13)\)\.
* Use <code>community\.dns\.wait\_for\_txt</code> to speed up waiting for DNS challenges to propagate\.
* acme\_certificate \- add <code>acme\_certificate\_hosttech\_token</code> option to use HostTech\'s new JSON API instead of old WSDL API \([https\://github\.com/felixfontein/ansible\-acme/pull/12](https\://github\.com/felixfontein/ansible\-acme/pull/12)\)\.
* acme\_certificate \- check whether credentials for DNS provider are set before starting certificate retrieval \([https\://github\.com/felixfontein/ansible\-acme/pull/12](https\://github\.com/felixfontein/ansible\-acme/pull/12)\)\.

<a id="breaking-changes--porting-guide-3"></a>
### Breaking Changes / Porting Guide

* Replace <code>felixfontein\.hosttech\_dns</code> and <code>felixfontein\.tools</code> collection dependencies by <code>community\.dns \>\= 1\.0\.0</code> and <code>community\.general \>\= 2\.5\.0</code>\.
* acme\_certificate role \- remove usage of tags <code>issue\-tls\-certs</code>\, <code>issue\-tls\-certs\-newkey</code> and <code>verify\-tls\-certs</code>\. By default\, new private keys are generated\. This can be disabled by setting <code>acme\_certificate\_regenerate\_private\_keys</code> to <code>false</code> \([https\://github\.com/felixfontein/ansible\-acme/pull/15](https\://github\.com/felixfontein/ansible\-acme/pull/15)\)\.

<a id="bugfixes-3"></a>
### Bugfixes

* account\_key\_rollover role \- when using sops\-encrypted keys\, <code>community\.sops\.sops\_encrypt</code> was run on the remote node and not the controller node \([https\://github\.com/felixfontein/ansible\-acme/pull/7](https\://github\.com/felixfontein/ansible\-acme/pull/7)\)\.

<a id="v0-2-0"></a>
## v0\.2\.0

<a id="release-summary-11"></a>
### Release Summary

Feature and repository maintenance release\.

<a id="minor-changes-7"></a>
### Minor Changes

* revoke\_old\_certificates role \- allow to revoke by ACME account key instead of certificate private key by setting <code>acme\_certificate\_revoke\_with\_acme\_account</code> to <code>true</code>\. This allows to revoke certificates with BuyPass\, which does not support revocation by certificate private key\.

<a id="v0-1-0"></a>
## v0\.1\.0

<a id="release-summary-12"></a>
### Release Summary

Initial release of my [acme\_certificate](https\://galaxy\.ansible\.com/ui/repo/published/felixfontein/acme\_certificate) role converted to a collection\, with two new roles <em class="title-reference">revoke\_old\_certificates</em> and <em class="title-reference">account\_key\_rollover</em>\.

<a id="new-roles"></a>
### New Roles

* felixfontein\.acme\.account\_key\_rollover \- Rollover for the ACME account key
* felixfontein\.acme\.acme\_certificate \- Retrieve a certificate for a set of domains and/or IP addresses
* felixfontein\.acme\.revoke\_old\_certificates \- Revoke old certificates copied aside by acme\_certificate
