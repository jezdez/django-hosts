import importlib.metadata

try:
    from django_hosts.defaults import host, patterns
    from django_hosts.resolvers import reverse, reverse_host, reverse_host_lazy, reverse_lazy
except ImportError:
    pass

__version__ = importlib.metadata.version("django-hosts")
__author__ = "Jazzband members (https://jazzband.co/)"
