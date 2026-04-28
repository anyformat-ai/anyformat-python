# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import files, health, webhooks, workflows
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.workflows import WorkflowsResource, AsyncWorkflowsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Anyformat",
    "AsyncAnyformat",
    "Client",
    "AsyncClient",
]


class Anyformat(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Anyformat client instance.

        This automatically infers the `api_key` argument from the `ANYFORMAT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ANYFORMAT_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ANYFORMAT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.anyformat.ai"

        custom_headers_env = os.environ.get("ANYFORMAT_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        """Health check endpoints to verify API availability."""
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Webhook subscriptions for asynchronous event notifications.

        Get notified when extractions complete or fail.
        """
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def files(self) -> FilesResource:
        """File collections group uploaded documents and track their extraction progress.

        Upload files, check status, and retrieve extraction results.
        """
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        from .resources.workflows import WorkflowsResource

        return WorkflowsResource(self)

    @cached_property
    def with_raw_response(self) -> AnyformatWithRawResponse:
        return AnyformatWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnyformatWithStreamedResponse:
        return AnyformatWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncAnyformat(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncAnyformat client instance.

        This automatically infers the `api_key` argument from the `ANYFORMAT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ANYFORMAT_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ANYFORMAT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.anyformat.ai"

        custom_headers_env = os.environ.get("ANYFORMAT_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        """Health check endpoints to verify API availability."""
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Webhook subscriptions for asynchronous event notifications.

        Get notified when extractions complete or fail.
        """
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        """File collections group uploaded documents and track their extraction progress.

        Upload files, check status, and retrieve extraction results.
        """
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        from .resources.workflows import AsyncWorkflowsResource

        return AsyncWorkflowsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncAnyformatWithRawResponse:
        return AsyncAnyformatWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnyformatWithStreamedResponse:
        return AsyncAnyformatWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AnyformatWithRawResponse:
    _client: Anyformat

    def __init__(self, client: Anyformat) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        """Health check endpoints to verify API availability."""
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        """Webhook subscriptions for asynchronous event notifications.

        Get notified when extractions complete or fail.
        """
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        """File collections group uploaded documents and track their extraction progress.

        Upload files, check status, and retrieve extraction results.
        """
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithRawResponse:
        from .resources.workflows import WorkflowsResourceWithRawResponse

        return WorkflowsResourceWithRawResponse(self._client.workflows)


class AsyncAnyformatWithRawResponse:
    _client: AsyncAnyformat

    def __init__(self, client: AsyncAnyformat) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        """Health check endpoints to verify API availability."""
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        """Webhook subscriptions for asynchronous event notifications.

        Get notified when extractions complete or fail.
        """
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        """File collections group uploaded documents and track their extraction progress.

        Upload files, check status, and retrieve extraction results.
        """
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithRawResponse:
        from .resources.workflows import AsyncWorkflowsResourceWithRawResponse

        return AsyncWorkflowsResourceWithRawResponse(self._client.workflows)


class AnyformatWithStreamedResponse:
    _client: Anyformat

    def __init__(self, client: Anyformat) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        """Health check endpoints to verify API availability."""
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        """Webhook subscriptions for asynchronous event notifications.

        Get notified when extractions complete or fail.
        """
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        """File collections group uploaded documents and track their extraction progress.

        Upload files, check status, and retrieve extraction results.
        """
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithStreamingResponse:
        from .resources.workflows import WorkflowsResourceWithStreamingResponse

        return WorkflowsResourceWithStreamingResponse(self._client.workflows)


class AsyncAnyformatWithStreamedResponse:
    _client: AsyncAnyformat

    def __init__(self, client: AsyncAnyformat) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        """Health check endpoints to verify API availability."""
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        """Webhook subscriptions for asynchronous event notifications.

        Get notified when extractions complete or fail.
        """
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        """File collections group uploaded documents and track their extraction progress.

        Upload files, check status, and retrieve extraction results.
        """
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithStreamingResponse:
        from .resources.workflows import AsyncWorkflowsResourceWithStreamingResponse

        return AsyncWorkflowsResourceWithStreamingResponse(self._client.workflows)


Client = Anyformat

AsyncClient = AsyncAnyformat
