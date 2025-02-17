Template tags
=============

.. currentmodule:: django_hosts.templatetags.hosts

.. function:: host_url(view_name, [view_args, view_kwargs], host_name, [host_args, host_kwargs, as_var, scheme])

Now if you want to actually refer to the full URLs in your templates
you can use the included ``host_url`` template tag. So imagine having a
host pattern of:

.. code-block:: python

    from django.conf import settings
    from django_hosts import host, patterns

    host_patterns = patterns("",
        host(r"admin", settings.ROOT_URLCONF, name="our-admin"),
    )

and a ``ROOT_URLCONF`` of:

.. code-block:: python

    from django.urls import path

    urlpatterns = [
        path("dashboard/", "dashboard", name="dashboard"),
    ]

then this example will create a link to the admin dashboard:

.. code-block:: html+django

    {% load hosts %}

    <a href="{% host_url 'dashboard' host 'our-admin' %}">Admin dashboard</a>

which will be rendered as:

.. code-block:: html+django

    <a href="//admin/dashboard/">Admin dashboard</a>

.. note::

    The double slash at the beginning of the href is an easy way
    to not have to worry about which scheme (http or https) is used.
    Your browser will automatically choose the currently used scheme.
    If you're on ``https://mysite.com/`` a link with an href
    of ``//mysite.com/about/`` would actually point to
    ``https://mysite.com/about/``.

    For more information see the `The protocol-relative URL`_ article
    by Paul Irish or the appropriate `section in RFC 3986`_.

    .. versionchanged:: 0.5

    You can override the used default scheme with the
    :attr:`~django.conf.settings.HOST_SCHEME` setting.

    .. versionchanged:: 1.0

    You can override the individually used scheme with the
    :ref:`scheme<scheme>` parameter.

.. _url_override:

Override the default url template tag
-------------------------------------

.. versionadded:: 1.0

In case you don't like adding ``{% load hosts %}`` to each and every template
that you reverse an URL in you can automatically override the url template tag
that is built into Django by adding
``"django_hosts.templatetags.hosts_override"`` to the
``TEMPLATES["OPTIONS"]["builtins"]`` list.

It won't hurt to have some ``{% load hosts %}`` in some templates and the
:func:`~django_hosts.templatetags.hosts.host_url` template tag will also still
work. But that will at least enable the use of templates in 3rd party apps,
for example.

.. _fqdn:

Fully qualified domain names (FQDN)
-----------------------------------

In case you want to append a default domain name to the domain part of
the rendered URL you can simply set the
:attr:`~django.conf.settings.PARENT_HOST`, e.g:

.. code-block:: python

    PARENT_HOST = "example.com"

This would render the link of the previous section as:

.. code-block:: html+django

    <a href="//admin.example.com/dashboard/">Admin dashboard</a>

Alternatively -- in case you don't want to append this parent domain
to all URLs you can also spell out the domain in the host pattern:

.. code-block:: python

    from django.conf import settings
    from django_hosts import host, patterns

    host_patterns = patterns(",
        host(r"admin\.example\.com", settings.ROOT_URLCONF, name="admin"),
    )

Host and URL pattern parameters
-------------------------------

If your host pattern contains an parameter (or keyed parameter), like:

.. code-block:: python

    from django.conf import settings
    from django_hosts import host, patterns

    host_patterns = patterns("",
        host(r"www", settings.ROOT_URLCONF, name="homepage"),
        host(r"(\w+)", "path.to.support_urls", name="wildcard"),
        host(r"(?P<username>\w+).users", "path.to.user_urls", name="user-area"),
    )

you can also easily pass parameters to the
:func:`~django_hosts.templatetags.hosts.host_url` template tag:

.. code-block:: html+django

    {% load hosts %}

    <a href="{% host_url 'user-dashboard' host 'user-area' username='johndoe' %}">John's dashboard</a>
    <a href="{% host_url 'faq-index' host 'wildcard' 'help' %}">FAQ</a>

Which will be rendered (with a :attr:`~django.conf.settings.PARENT_HOST` of
``"example.com"``) as:

.. code-block:: html+django

    <a href="//johndoe.users.example.com/">John's dashboard</a>
    <a href="//help.example.com/faq/">FAQ</a>

.. _scheme:

Changing the scheme individually
--------------------------------

.. versionadded: 1.0

It's not only possible to define the scheme in the hostconf but also on a
case-by-case basis using the template tag:

.. code-block:: html+django

    {% load hosts %}

    <a href="{% host_url 'user-dashboard' host 'user-area' username='johndoe' scheme 'https' %}">John's dashboard</a>
    <a href="//help.example.com/faq/">FAQ</a>

Which will be rendered (with a :attr:`~django.conf.settings.PARENT_HOST` of
``'example.com'`` and a :attr:`~django.conf.settings.HOST_SCHEME` setting
defaulting to ``'//'``) as:

.. code-block:: html+django

    <a href="https://johndoe.users.example.com/">John's dashboard</a>
    <a href="//help.example.com/faq/">FAQ</a>

.. _asvar:

Storing the url in a context variable
-------------------------------------

.. versionadded:: 0.4

If you'd like to retrieve a URL without displaying it, you can save the
result of the template tag in a template variable and use it later on, e.g.:

.. code-block:: html+django

    {% load hosts %}

    {% host_url 'homepage' as homepage_url %}
    <a href="{{ homepage_url }}" title="Go back to {{ homepage_url }}">Home</a>


.. _The protocol-relative URL: https://www.paulirish.com/2010/the-protocol-relative-url/
.. _section in RFC 3986: https://datatracker.ietf.org/doc/html/rfc3986#section-4.2
