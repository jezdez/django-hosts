from django.test import TestCase

from django_hosts.test import AsyncHostsClient, HostsClient


class TestHostsClient(TestCase):
    client_class = HostsClient

    def test_host_header_set_from_full_url(self):
        response = self.client.get('https://testserver.local/api/v1/users/')
        assert response.request['HTTP_HOST'] == 'testserver.local'

    def test_host_header_set_from_url_without_scheme(self):
        response = self.client.get('//testserver.local/api/v1/users/')
        assert response.request['HTTP_HOST'] == 'testserver.local'

    def test_host_header_from_user_is_not_overridden(self):
        response = self.client.get(
            'https://testserver.local/api/v1/users/', headers={'host': 'api.example.com'}
        )
        assert response.request['HTTP_HOST'] == 'api.example.com'

    def test_host_header_not_set_from_relative_url(self):
        response = self.client.get('/api/v1/users/')
        assert 'HTTP_HOST' not in response.request


class TestAsyncHostsClient(TestCase):
    async_client_class = AsyncHostsClient

    async def test_host_header_set_from_url(self):
        response = await self.async_client.get('https://testserver.local/api/v1/users/')
        assert (b'host', b'testserver.local') in response.request['headers']

    async def test_host_header_from_user_is_not_overridden(self):
        response = await self.async_client.get(
            'https://testserver.local/api/v1/users/', headers={'host': 'api.example.com'}
        )
        assert (b'host', b'api.example.com') in response.request['headers']

    async def test_host_header_not_set_from_relative_url(self):
        response = await self.async_client.get('/api/v1/users/')
        assert (b'host', b'testserver') in response.request['headers']
