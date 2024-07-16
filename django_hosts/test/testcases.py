from django.test import SimpleTestCase, TestCase, TransactionTestCase

from .client import HostsClient, AsyncHostsClient


class HostsTestCaseMixin:
    client_class = HostsClient
    async_client_class = AsyncHostsClient


class SimpleHostsTestCase(HostsTestCaseMixin, SimpleTestCase):
    pass


class TransactionHostsTestCase(HostsTestCaseMixin, TransactionTestCase):
    pass


class HostsTestCase(HostsTestCaseMixin, TestCase):
    pass
