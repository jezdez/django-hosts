.. include:: ../README.rst

Usage
-----

Patterns being regular expressions allows setups to feature dynamic (or
"wildcard") host schemes:

.. code-block:: python

    from django.conf import settings
    from django_hosts import patterns, host

    host_patterns = patterns('',
        host(r'www', settings.ROOT_URLCONF, name='www'),
        host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
    )

Here, requests to ``www.example.com`` will be routed as normal but a
request to ``admin.example.com`` is routed to ``path.to.custom_urls``.

As patterns are matched in order, we placed ``www`` first as it otherwise
would have matched against ``\w+`` and thus routed to the wrong
destination.

Alternatively, we could have used negative lookahead, given the value
of the ``ROOT_URLCONF`` setting:

.. code-block:: python

    from django_hosts import patterns, host

    host_patterns = patterns('',
        host(r'(?!www)\w+', 'path.to.custom_urls', name='wildcard'),
    )

In your templates you can use the
:func:`~django_hosts.templatetags.hosts.host_url` template tag to reverse
a URL the way you're used to it with Django's url template tag:

.. code-block:: html+django

    {% load hosts %}
    <a href="{% host_url 'homepage' host 'www' %}">Home</a> |
    <a href="{% host_url 'account' host 'wildcard' request.user.username %}">Your Account</a> |

Since the template tag will always automatically fall back to your default
host (as defined by :attr:`~django.conf.settings.DEFAULT_HOST`) you can leave
off the ``host`` parameter as well.

You can even :ref:`override the url tag<url_override>` that comes with Django
to simplify reversing URLs in your templates:

.. code-block:: html+django

    <a href="{% url 'homepage' %}">Home</a> |
    <a href="{% url 'account' host 'wildcard' request.user.username %}">Your Account</a> |

On the Python side of things like your views you can easily do the same as
with Django's own reverse function. Simply use the
:func:`~django_hosts.resolvers.reverse` function for that:

.. code-block:: python

    from django.shortcuts import render
    from django_hosts.resolvers import reverse

    def homepage(request):
        homepage_url = reverse('homepage', host='www')
        return render(request, 'homepage.html', {'homepage_url': homepage_url})

Settings
--------

.. currentmodule:: django.conf.settings


.. attribute:: ROOT_HOSTCONF (required)

    The dotted Python import path of the module containing your host
    patterns. Similar to ``ROOT_URLCONF``.

.. attribute:: DEFAULT_HOST (required)

    The *name* of the host pattern you want to refer to as the default
    pattern. Used if no other host pattern matches or no host name is
    passed to the :func:`~django_hosts.templatetags.hosts.host_url`
    template tag.

.. attribute:: PARENT_HOST (optional)

    The parent domain name to be :ref:`appended to the reversed domain <fqdn>`
    (e.g. using the :func:`~django_hosts.templatetags.hosts.host_url`
    template tag).

.. attribute:: HOST_SCHEME (optional)

    The scheme to prepend host names with during reversing, e.g. when
    using the :func:`~django_hosts.templatetags.hosts.host_url` template tag.
    Defaults to ``'//'``.

.. attribute:: HOST_PORT (optional)

    .. versionadded:: 1.0

    The port to append to host names during reversing, e.g. when
    using the :func:`~django_hosts.templatetags.hosts.host_url` template tag.
    Defaults to ``''`` (empty string).

.. attribute:: HOST_SITE_TIMEOUT (optional)

    The time to cache the host in the default cache backend, in seconds,
    when using the :func:`~django_hosts.callbacks.cached_host_site` callback.
    Defaults to ``3600``.

More docs
---------

.. toctree::
   :maxdepth: 2

   templatetags
   reference
   callbacks
   testing
   faq
   changelog

Issues
------

For any bug reports and feature requests, please use the
`Github issue tracker`_.

Thanks
------

Many thanks to the folks at playfire_ for releasing their
django-dynamic-subdomains_ app, which was the inspiration for this app.

.. _playfire: http://code.playfire.com/
.. _django-dynamic-subdomains: https://github.com/playfire/django-dynamic-subdomains/
.. _`Github issue tracker`: https://github.com/jazzband/django-hosts/issues
