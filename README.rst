Test cases for Openstack-i18n

1. Command line I18n test
   Install a project with DevStack in an English environment, import mock translations, invoke command lines, verify:
   if the response messages are translated.
   if the command lines are successfully executed.
   if the log messages are translated.

2. API I18n test
   Install a project with DevStack in an English environment, import mock translations, invoke APIs with non-English inputs, verify:
   if the APIs are successfully executed.

3. Horizon test
   Use mock translations and manully check if there is no strings marked with translation tags.
   https://review.openstack.org/#/c/142239/

4. oslo.i18n test
   4.1 Lazy translation feature
   https://review.openstack.org/#/c/147262/
