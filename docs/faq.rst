FAQ
===

Does django-hosts work with the Django Debug Toolbar?
-----------------------------------------------------

Yes, django-hosts works with `Django Debug toolbar`_ with the only
limitation that the toolbar's middleware has to be come *after*
django-hosts' ``HostsRequestMiddleware`` middleware, e.g.:

.. code-block:: python

    MIDDLEWARE = [
        'django_hosts.middleware.HostsRequestMiddleware',
        # your other middlewares..
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django_hosts.middleware.HostsResponseMiddleware',
    ]

Also, you have to install `django-debug-toolbar 0.9.X`_ or higher.

.. _`Django Debug toolbar`: https://github.com/django-debug-toolbar/django-debug-toolbar/
.. _`django-debug-toolbar 0.9.X`: https://pypi.org/project/django-debug-toolbar/


My tests using client.post(...) are failing now, what should I do?
------------------------------------------------------------------

Yes, django-hosts might make your existing pytest tests fail if you are using
client.post(...). All you need to do is to set the correct SERVER_NAME on that call
depending on the host that should handle the call

.. code-block:: python

    client.post(..., SERVER_NAME='api-server.something')
