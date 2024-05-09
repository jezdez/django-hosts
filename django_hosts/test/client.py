from urllib.parse import urlparse

from django.test import AsyncClient, Client


class HostClientMixin:
    """Test client to help work with django-hosts in tests."""

    def generic(self, method, path, *args, **extra):
        if path.startswith('http'):
            # Populate the host header from the URL host
            _scheme, host, *_others = urlparse(path)
            if extra.get('headers') is None:
                extra['headers'] = {}
            if extra['headers'].get('host') is None:
                extra['headers']['host'] = host
        return super().generic(method, path, *args, **extra)


class HostsClient(HostClientMixin, Client):
    pass


class AsyncHostsClient(HostClientMixin, AsyncClient):
    pass
