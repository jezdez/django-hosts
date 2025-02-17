Callbacks
=========

Parsing the host from
:meth:`request.get_host() <django.http.HttpRequest.get_host>` and lookup
its corresponding object instance (e.g. site) in every view violates DRY_.
If these dynamic hosts had a lot of views this would become particularly
unwieldy.

To remedy this, you can optionally specify a callback method to be called
if your host matches.

Simply define a callback function:

.. code-block:: python

    from django.shortcuts import get_object_or_404
    from django.contrib.auth.models import User

    def custom_fn(request, username):
        request.viewing_user = get_object_or_404(User, username=username)

..and pass it as the ``callback`` parameter to the ``host`` object:

.. code-block:: python

    from django.conf import settings
    from django_hosts import host, patterns

    host_patterns = patterns("",
        host(r"www", settings.ROOT_URLCONF, name="www"),
        host(r"(?P<username>\w+)", "path.to.custom_urls",
             callback="path.to.custom_fn", name="with-callback"),
    )

This example avoids the duplicated work in every view by attaching a
``viewing_user`` instance to the request object. Views referenced by the
"dynamic" URLconf can now assume that this object exists.

The custom method is called with the ``request`` object and any named
captured arguments, similar to regular Django url processing.

Callbacks may return either ``None`` or an
:class:`~django:django.http.HttpResponse` object.

- If it returns ``None``, the request continues to be processed and the
  appropriate view is eventually called.

- If a callback returns an :class:`~django:django.http.HttpResponse` object,
  that :class:`~django:django.http.HttpResponse` is returned to the client
  without any further processing.

.. note::

    There are a few things to keep in mind when using the callbacks:

    - Callbacks are executed with the URLconf set to the second argument in
      the ``host_patterns`` list. For example, in the example above, the
      callback will be executed with the URLconf as ``path.to.custom_urls``
      and not the default URLconf.

    - This can cause problems when reversing URLs within your callback as
      they may not be "visible" to :func:`django.core.urlresolvers.reverse`
      as they are specified in (eg.) the default URLconf.

    - To remedy this, specify the ``urlconf`` parameter when calling
      :func:`~django.core.urlresolvers.reverse`.

    - When using dynamic hosts based on user input, ensure users cannot
      specify names that conflict with static subdomains such as "www" or
      their subdomain will not be accessible.

    - Don't forget to add :data:`~django.conf.urls.handler404` and
      :data:`~django.conf.urls.handler500` entries for your custom URLconfs.

Included callbacks
------------------

``django-hosts`` includes the following callbacks for use with the Django
contrib app ``django.contrib.sites``:

.. autofunction:: django_hosts.callbacks.host_site(request, *args, **kwargs)

.. autofunction:: django_hosts.callbacks.cached_host_site(request, *args, **kwargs)

.. _DRY: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
