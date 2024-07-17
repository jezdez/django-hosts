from django.test import (
    SimpleTestCase as DjangoSimpleTestCase,
    TestCase as DjangoTestCase,
    TransactionTestCase as DjangoTransactionTestCase
)

from .client import HostsClient, AsyncHostsClient


class HostsTestCaseMixin:
    client_class = HostsClient
    async_client_class = AsyncHostsClient


class SimpleTestCase(HostsTestCaseMixin, DjangoSimpleTestCase):
    pass


class TransactionTestCase(HostsTestCaseMixin, DjangoTransactionTestCase):
    pass


class TestCase(HostsTestCaseMixin, DjangoTestCase):
    pass
