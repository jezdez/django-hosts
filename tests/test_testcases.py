from django_hosts.test import TestCase, HostsClient, AsyncHostsClient, SimpleTestCase, TransactionTestCase


class TestHostsTestCase(TestCase):
    def test_client_class_instances(self):
        assert isinstance(self.client, HostsClient)
        assert isinstance(self.async_client, AsyncHostsClient)


class TestSimpleHostsTestCase(SimpleTestCase):
    def test_client_class_instances(self):
        assert isinstance(self.client, HostsClient)
        assert isinstance(self.async_client, AsyncHostsClient)


class TestTransactionHostsTestCase(TransactionTestCase):
    def test_client_class_instances(self):
        assert isinstance(self.client, HostsClient)
        assert isinstance(self.async_client, AsyncHostsClient)
