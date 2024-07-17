Testing
=======

The problem
-----------

Testing with django-hosts can feel cumbersome if using the vanilla Django
testing toolbox. Here is how a typical test would look like:

.. code-block:: python

    from django.test import TestCase
    from django_hosts import reverse


    class UserViewTestCase(TestCase):
        def test_user_list(self):
            # Assuming the url looks like http://api.example.com/v1/users/
            url = reverse("list-user", host="api")

            # Pass the server name
            response = self.client.get(url, SERVER_NAME="api.example.com")
            assert response.status_code == 200

As you can see, you need to remember a few things:

1. Use the ``reverse`` function from django-hosts, as opposed to the one from Django
2. Pass the extra host when reversing
3. Pass the server name (or host header) as part of the request

As your codebase grows, you'll (hopefully) be adding more tests cases and you
may get tired of repeating this.

The solution
------------

Luckily django-hosts provides some testing tool to help you write tests with
less boilerplate, mainly using custom test cases ``SimpleTestCase``,
``TestCase``, ``TransactionTestCase``, all coming from ``django_hosts.test``,
and subclasses of their counterpart from Django.

For example the above test would be written as:

.. code-block:: python

    from django_hosts import reverse
    from django_hosts.test import TestCase


    @override_settings(DEFAULT_HOST="api")
    class UserViewTestCase(TestCase):
        def test_user_list(self):
            url = reverse("list-user")
            response = self.client.get(url)
            assert response.status_code == 200

Specifically:

- We swap the Django's ``TestCase`` for the django hosts equivalent by changing
the import statement. It's using a custom test client to set the host header
automatically on the request based on the absolute URL. As a result, the
``self.client.get(...)`` call no longer need the server name/host header.

- We set the default host at the class level, using ``override_settings``
(`from Django <https://docs.djangoproject.com/en/stable/topics/testing/tools/#django.test.override_settings>`_)
instead of repeating it in each ``reverse`` call. When a test class has lots
of methods, this can save a lot of typing and make your tests more readable.

Going further
-------------

This will hopefully cover the main cases, but should you want to reuse it and
combine it with your own client/test case classes, the base functionality is
provided as mixins: ``HostClientMixin`` and ``HostsTestCaseMixin``.
