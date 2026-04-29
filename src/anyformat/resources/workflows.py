# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..types import (
    workflow_run_params,
    workflow_list_params,
    workflow_create_params,
    workflow_upload_params,
    workflow_list_runs_params,
    workflow_list_files_params,
    workflow_create_file_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.workflow import Workflow
from ..types.workflow_run_response import WorkflowRunResponse
from ..types.workflow_list_response import WorkflowListResponse
from ..types.workflow_upload_response import WorkflowUploadResponse
from ..types.workflow_list_runs_response import WorkflowListRunsResponse
from ..types.workflow_list_files_response import WorkflowListFilesResponse
from ..types.workflow_create_file_response import WorkflowCreateFileResponse
from ..types.workflow_get_file_results_response import WorkflowGetFileResultsResponse

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]


class WorkflowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/anyformat-ai/anyformat-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/anyformat-ai/anyformat-python#with_streaming_response
        """
        return WorkflowsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        fields: Iterable[Dict[str, object]],
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workflow:
        """
        Create a new extraction workflow.

        Workflows define what data to extract from documents. After creating a workflow,
        configure its extraction fields in the
        [AnyFormat dashboard](https://app.anyformat.ai).

        Args:
          fields: Field definitions

          name: Workflow name

          description: Workflow description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/workflows/",
            body=maybe_transform(
                {
                    "fields": fields,
                    "name": name,
                    "description": description,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Workflow,
        )

    def retrieve(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workflow:
        """
        Retrieve a single workflow by its ID, including its configured extraction
        fields.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._get(
            path_template("/v2/workflows/{workflow_id}/", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Workflow,
        )

    def list(
        self,
        *,
        order: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowListResponse:
        """
        List all workflows in your organization with pagination.

        Workflows can be filtered by status and sorted by any field.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/workflows/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "status": status,
                    },
                    workflow_list_params.WorkflowListParams,
                ),
                security={},
            ),
            cast_to=WorkflowListResponse,
        )

    def delete(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a workflow and all associated file collections and extraction results.

        This action is irreversible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v2/workflows/{workflow_id}/", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )

    def create_file(
        self,
        workflow_id: str,
        *,
        files: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowCreateFileResponse:
        """
        Upload one or more files to a workflow, creating a new file collection.

        Use this when you want to upload files without immediately running extraction.
        To upload and extract in one step, use `POST /v2/workflows/{workflow_id}/run/`
        instead.

        Supported file types: PDF, PNG, JPG, TIFF, TXT, DOCX, XLSX, CSV, and more.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/v2/workflows/{workflow_id}/files/", workflow_id=workflow_id),
            body=maybe_transform({"files": files}, workflow_create_file_params.WorkflowCreateFileParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=WorkflowCreateFileResponse,
        )

    def get_file_results(
        self,
        collection_id: str,
        *,
        workflow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowGetFileResultsResponse:
        """
        Retrieve the extraction results for a file collection.

        Returns the structured data extracted from each file, including field values,
        confidence scores, and source evidence (text excerpts and page numbers). Also
        includes a `verification_url` linking to the AnyFormat dashboard for human
        review.

        Returns **412 Precondition Failed** if the extraction is still in progress. Poll
        this endpoint until you receive a 200 response, or use webhooks
        (`extraction.completed` event) to be notified when processing finishes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._get(
            path_template(
                "/v2/workflows/{workflow_id}/files/{collection_id}/results/",
                workflow_id=workflow_id,
                collection_id=collection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=WorkflowGetFileResultsResponse,
        )

    def list_files(
        self,
        workflow_id: str,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowListFilesResponse:
        """
        List file collections for a workflow.

        A file collection groups one or more uploaded files together. Each collection
        has a status indicating the extraction progress: `pending`, `processing`,
        `completed`, or `failed`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._get(
            path_template("/v2/workflows/{workflow_id}/files/", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    workflow_list_files_params.WorkflowListFilesParams,
                ),
                security={},
            ),
            cast_to=WorkflowListFilesResponse,
        )

    def list_runs(
        self,
        workflow_id: str,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowListRunsResponse:
        """
        List all extraction runs for a workflow with pagination.

        Each run corresponds to a file collection that was processed by the workflow.
        Use the run's `id` (collection UUID) with
        `GET /v2/workflows/{workflow_id}/files/{id}/results/` to fetch detailed results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._get(
            path_template("/v2/workflows/{workflow_id}/runs/", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    workflow_list_runs_params.WorkflowListRunsParams,
                ),
                security={},
            ),
            cast_to=WorkflowListRunsResponse,
        )

    def run(
        self,
        workflow_id: str,
        *,
        file: Optional[str] | Omit = omit,
        text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRunResponse:
        """
        Upload a file and immediately run the extraction workflow on it.

        This is the primary endpoint for document extraction. It creates a file
        collection, uploads the file, and starts extraction in one step. The response
        includes a collection `id` that you can use to poll for results via
        `GET /v2/workflows/{workflow_id}/files/{collection_id}/results/`.

        Provide the file as a binary upload in the `file` field, or send raw text in the
        `text` field for text-only extraction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/v2/workflows/{workflow_id}/run/", workflow_id=workflow_id),
            body=maybe_transform(
                {
                    "file": file,
                    "text": text,
                },
                workflow_run_params.WorkflowRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=WorkflowRunResponse,
        )

    def upload(
        self,
        workflow_id: str,
        *,
        file: Optional[str] | Omit = omit,
        text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowUploadResponse:
        """
        Upload a file to a workflow without running extraction.

        Use this when you want to stage files for later processing. For
        upload-and-extract in one step, use `POST /v2/workflows/{workflow_id}/run/`
        instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/v2/workflows/{workflow_id}/upload/", workflow_id=workflow_id),
            body=maybe_transform(
                {
                    "file": file,
                    "text": text,
                },
                workflow_upload_params.WorkflowUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=WorkflowUploadResponse,
        )


class AsyncWorkflowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/anyformat-ai/anyformat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/anyformat-ai/anyformat-python#with_streaming_response
        """
        return AsyncWorkflowsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        fields: Iterable[Dict[str, object]],
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workflow:
        """
        Create a new extraction workflow.

        Workflows define what data to extract from documents. After creating a workflow,
        configure its extraction fields in the
        [AnyFormat dashboard](https://app.anyformat.ai).

        Args:
          fields: Field definitions

          name: Workflow name

          description: Workflow description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/workflows/",
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "name": name,
                    "description": description,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Workflow,
        )

    async def retrieve(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workflow:
        """
        Retrieve a single workflow by its ID, including its configured extraction
        fields.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return await self._get(
            path_template("/v2/workflows/{workflow_id}/", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=Workflow,
        )

    async def list(
        self,
        *,
        order: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowListResponse:
        """
        List all workflows in your organization with pagination.

        Workflows can be filtered by status and sorted by any field.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/workflows/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "status": status,
                    },
                    workflow_list_params.WorkflowListParams,
                ),
                security={},
            ),
            cast_to=WorkflowListResponse,
        )

    async def delete(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a workflow and all associated file collections and extraction results.

        This action is irreversible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v2/workflows/{workflow_id}/", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )

    async def create_file(
        self,
        workflow_id: str,
        *,
        files: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowCreateFileResponse:
        """
        Upload one or more files to a workflow, creating a new file collection.

        Use this when you want to upload files without immediately running extraction.
        To upload and extract in one step, use `POST /v2/workflows/{workflow_id}/run/`
        instead.

        Supported file types: PDF, PNG, JPG, TIFF, TXT, DOCX, XLSX, CSV, and more.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/v2/workflows/{workflow_id}/files/", workflow_id=workflow_id),
            body=await async_maybe_transform({"files": files}, workflow_create_file_params.WorkflowCreateFileParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=WorkflowCreateFileResponse,
        )

    async def get_file_results(
        self,
        collection_id: str,
        *,
        workflow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowGetFileResultsResponse:
        """
        Retrieve the extraction results for a file collection.

        Returns the structured data extracted from each file, including field values,
        confidence scores, and source evidence (text excerpts and page numbers). Also
        includes a `verification_url` linking to the AnyFormat dashboard for human
        review.

        Returns **412 Precondition Failed** if the extraction is still in progress. Poll
        this endpoint until you receive a 200 response, or use webhooks
        (`extraction.completed` event) to be notified when processing finishes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._get(
            path_template(
                "/v2/workflows/{workflow_id}/files/{collection_id}/results/",
                workflow_id=workflow_id,
                collection_id=collection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=WorkflowGetFileResultsResponse,
        )

    async def list_files(
        self,
        workflow_id: str,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowListFilesResponse:
        """
        List file collections for a workflow.

        A file collection groups one or more uploaded files together. Each collection
        has a status indicating the extraction progress: `pending`, `processing`,
        `completed`, or `failed`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return await self._get(
            path_template("/v2/workflows/{workflow_id}/files/", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    workflow_list_files_params.WorkflowListFilesParams,
                ),
                security={},
            ),
            cast_to=WorkflowListFilesResponse,
        )

    async def list_runs(
        self,
        workflow_id: str,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowListRunsResponse:
        """
        List all extraction runs for a workflow with pagination.

        Each run corresponds to a file collection that was processed by the workflow.
        Use the run's `id` (collection UUID) with
        `GET /v2/workflows/{workflow_id}/files/{id}/results/` to fetch detailed results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return await self._get(
            path_template("/v2/workflows/{workflow_id}/runs/", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    workflow_list_runs_params.WorkflowListRunsParams,
                ),
                security={},
            ),
            cast_to=WorkflowListRunsResponse,
        )

    async def run(
        self,
        workflow_id: str,
        *,
        file: Optional[str] | Omit = omit,
        text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRunResponse:
        """
        Upload a file and immediately run the extraction workflow on it.

        This is the primary endpoint for document extraction. It creates a file
        collection, uploads the file, and starts extraction in one step. The response
        includes a collection `id` that you can use to poll for results via
        `GET /v2/workflows/{workflow_id}/files/{collection_id}/results/`.

        Provide the file as a binary upload in the `file` field, or send raw text in the
        `text` field for text-only extraction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/v2/workflows/{workflow_id}/run/", workflow_id=workflow_id),
            body=await async_maybe_transform(
                {
                    "file": file,
                    "text": text,
                },
                workflow_run_params.WorkflowRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=WorkflowRunResponse,
        )

    async def upload(
        self,
        workflow_id: str,
        *,
        file: Optional[str] | Omit = omit,
        text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowUploadResponse:
        """
        Upload a file to a workflow without running extraction.

        Use this when you want to stage files for later processing. For
        upload-and-extract in one step, use `POST /v2/workflows/{workflow_id}/run/`
        instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/v2/workflows/{workflow_id}/upload/", workflow_id=workflow_id),
            body=await async_maybe_transform(
                {
                    "file": file,
                    "text": text,
                },
                workflow_upload_params.WorkflowUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=WorkflowUploadResponse,
        )


class WorkflowsResourceWithRawResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.create = to_raw_response_wrapper(
            workflows.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.list = to_raw_response_wrapper(
            workflows.list,
        )
        self.delete = to_raw_response_wrapper(
            workflows.delete,
        )
        self.create_file = to_raw_response_wrapper(
            workflows.create_file,
        )
        self.get_file_results = to_raw_response_wrapper(
            workflows.get_file_results,
        )
        self.list_files = to_raw_response_wrapper(
            workflows.list_files,
        )
        self.list_runs = to_raw_response_wrapper(
            workflows.list_runs,
        )
        self.run = to_raw_response_wrapper(
            workflows.run,
        )
        self.upload = to_raw_response_wrapper(
            workflows.upload,
        )


class AsyncWorkflowsResourceWithRawResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.create = async_to_raw_response_wrapper(
            workflows.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            workflows.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workflows.delete,
        )
        self.create_file = async_to_raw_response_wrapper(
            workflows.create_file,
        )
        self.get_file_results = async_to_raw_response_wrapper(
            workflows.get_file_results,
        )
        self.list_files = async_to_raw_response_wrapper(
            workflows.list_files,
        )
        self.list_runs = async_to_raw_response_wrapper(
            workflows.list_runs,
        )
        self.run = async_to_raw_response_wrapper(
            workflows.run,
        )
        self.upload = async_to_raw_response_wrapper(
            workflows.upload,
        )


class WorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.create = to_streamed_response_wrapper(
            workflows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            workflows.list,
        )
        self.delete = to_streamed_response_wrapper(
            workflows.delete,
        )
        self.create_file = to_streamed_response_wrapper(
            workflows.create_file,
        )
        self.get_file_results = to_streamed_response_wrapper(
            workflows.get_file_results,
        )
        self.list_files = to_streamed_response_wrapper(
            workflows.list_files,
        )
        self.list_runs = to_streamed_response_wrapper(
            workflows.list_runs,
        )
        self.run = to_streamed_response_wrapper(
            workflows.run,
        )
        self.upload = to_streamed_response_wrapper(
            workflows.upload,
        )


class AsyncWorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.create = async_to_streamed_response_wrapper(
            workflows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            workflows.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workflows.delete,
        )
        self.create_file = async_to_streamed_response_wrapper(
            workflows.create_file,
        )
        self.get_file_results = async_to_streamed_response_wrapper(
            workflows.get_file_results,
        )
        self.list_files = async_to_streamed_response_wrapper(
            workflows.list_files,
        )
        self.list_runs = async_to_streamed_response_wrapper(
            workflows.list_runs,
        )
        self.run = async_to_streamed_response_wrapper(
            workflows.run,
        )
        self.upload = async_to_streamed_response_wrapper(
            workflows.upload,
        )
