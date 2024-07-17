from urllib.parse import urlparse

from django.test import AsyncClient, Client


class HostClientMixin:
    """Test client to help work with django-hosts in tests."""

    def generic(self, method, path, *args, **extra):
        scheme, netloc, *_others = urlparse(path)
        if scheme:
            extra["wsgi.url_scheme"] = scheme
        if netloc:
            # Populate the host header from the URL host
            extra["headers"] = extra["headers"] or {}
            if extra["headers"].get("host") is None:
                extra["headers"]["host"] = netloc
        return super().generic(method, path, *args, **extra)


class HostsClient(HostClientMixin, Client):
    pass


class AsyncHostsClient(HostClientMixin, AsyncClient):
    pass
