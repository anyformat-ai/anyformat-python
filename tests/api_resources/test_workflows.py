# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from anyformat import Anyformat, AsyncAnyformat
from tests.utils import assert_matches_type
from anyformat.types import (
    Workflow,
    WorkflowRunResponse,
    WorkflowListResponse,
    WorkflowUploadResponse,
    WorkflowListRunsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Anyformat) -> None:
        workflow = client.workflows.create()
        assert_matches_type(Workflow, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Anyformat) -> None:
        response = client.workflows.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(Workflow, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Anyformat) -> None:
        with client.workflows.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(Workflow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Anyformat) -> None:
        workflow = client.workflows.retrieve(
            "workflow_id",
        )
        assert_matches_type(Workflow, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Anyformat) -> None:
        response = client.workflows.with_raw_response.retrieve(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(Workflow, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Anyformat) -> None:
        with client.workflows.with_streaming_response.retrieve(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(Workflow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Anyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.workflows.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Anyformat) -> None:
        workflow = client.workflows.list()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Anyformat) -> None:
        workflow = client.workflows.list(
            order="order",
            page=1,
            page_size=1,
            sort_by="sort_by",
            status="status",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Anyformat) -> None:
        response = client.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Anyformat) -> None:
        with client.workflows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowListResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Anyformat) -> None:
        workflow = client.workflows.delete(
            "workflow_id",
        )
        assert workflow is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Anyformat) -> None:
        response = client.workflows.with_raw_response.delete(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Anyformat) -> None:
        with client.workflows.with_streaming_response.delete(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Anyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.workflows.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_runs(self, client: Anyformat) -> None:
        workflow = client.workflows.list_runs(
            workflow_id="workflow_id",
        )
        assert_matches_type(WorkflowListRunsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_runs_with_all_params(self, client: Anyformat) -> None:
        workflow = client.workflows.list_runs(
            workflow_id="workflow_id",
            page=1,
            page_size=1,
        )
        assert_matches_type(WorkflowListRunsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_runs(self, client: Anyformat) -> None:
        response = client.workflows.with_raw_response.list_runs(
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowListRunsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_runs(self, client: Anyformat) -> None:
        with client.workflows.with_streaming_response.list_runs(
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowListRunsResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_runs(self, client: Anyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.workflows.with_raw_response.list_runs(
                workflow_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_results(self, client: Anyformat) -> None:
        workflow = client.workflows.results(
            workflow_id="workflow_id",
        )
        assert_matches_type(object, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_results_with_all_params(self, client: Anyformat) -> None:
        workflow = client.workflows.results(
            workflow_id="workflow_id",
            as_lists="as_lists",
            output_format="jsonl",
        )
        assert_matches_type(object, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_results(self, client: Anyformat) -> None:
        response = client.workflows.with_raw_response.results(
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(object, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_results(self, client: Anyformat) -> None:
        with client.workflows.with_streaming_response.results(
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(object, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_results(self, client: Anyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.workflows.with_raw_response.results(
                workflow_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Anyformat) -> None:
        workflow = client.workflows.run(
            workflow_id="workflow_id",
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Anyformat) -> None:
        workflow = client.workflows.run(
            workflow_id="workflow_id",
            content_type="content_type",
            file="file",
            file_base64="file_base64",
            filename="filename",
            text="text",
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Anyformat) -> None:
        response = client.workflows.with_raw_response.run(
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Anyformat) -> None:
        with client.workflows.with_streaming_response.run(
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_run(self, client: Anyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.workflows.with_raw_response.run(
                workflow_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Anyformat) -> None:
        workflow = client.workflows.upload(
            workflow_id="workflow_id",
        )
        assert_matches_type(WorkflowUploadResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Anyformat) -> None:
        workflow = client.workflows.upload(
            workflow_id="workflow_id",
            content_type="content_type",
            file="file",
            file_base64="file_base64",
            filename="filename",
            text="text",
        )
        assert_matches_type(WorkflowUploadResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Anyformat) -> None:
        response = client.workflows.with_raw_response.upload(
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowUploadResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Anyformat) -> None:
        with client.workflows.with_streaming_response.upload(
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowUploadResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Anyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.workflows.with_raw_response.upload(
                workflow_id="",
            )


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.create()
        assert_matches_type(Workflow, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAnyformat) -> None:
        response = await async_client.workflows.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(Workflow, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAnyformat) -> None:
        async with async_client.workflows.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(Workflow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.retrieve(
            "workflow_id",
        )
        assert_matches_type(Workflow, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAnyformat) -> None:
        response = await async_client.workflows.with_raw_response.retrieve(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(Workflow, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAnyformat) -> None:
        async with async_client.workflows.with_streaming_response.retrieve(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(Workflow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAnyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.workflows.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.list()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.list(
            order="order",
            page=1,
            page_size=1,
            sort_by="sort_by",
            status="status",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAnyformat) -> None:
        response = await async_client.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAnyformat) -> None:
        async with async_client.workflows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowListResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.delete(
            "workflow_id",
        )
        assert workflow is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAnyformat) -> None:
        response = await async_client.workflows.with_raw_response.delete(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAnyformat) -> None:
        async with async_client.workflows.with_streaming_response.delete(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAnyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.workflows.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_runs(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.list_runs(
            workflow_id="workflow_id",
        )
        assert_matches_type(WorkflowListRunsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_runs_with_all_params(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.list_runs(
            workflow_id="workflow_id",
            page=1,
            page_size=1,
        )
        assert_matches_type(WorkflowListRunsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_runs(self, async_client: AsyncAnyformat) -> None:
        response = await async_client.workflows.with_raw_response.list_runs(
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowListRunsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_runs(self, async_client: AsyncAnyformat) -> None:
        async with async_client.workflows.with_streaming_response.list_runs(
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowListRunsResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_runs(self, async_client: AsyncAnyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.workflows.with_raw_response.list_runs(
                workflow_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_results(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.results(
            workflow_id="workflow_id",
        )
        assert_matches_type(object, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_results_with_all_params(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.results(
            workflow_id="workflow_id",
            as_lists="as_lists",
            output_format="jsonl",
        )
        assert_matches_type(object, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_results(self, async_client: AsyncAnyformat) -> None:
        response = await async_client.workflows.with_raw_response.results(
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(object, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_results(self, async_client: AsyncAnyformat) -> None:
        async with async_client.workflows.with_streaming_response.results(
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(object, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_results(self, async_client: AsyncAnyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.workflows.with_raw_response.results(
                workflow_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.run(
            workflow_id="workflow_id",
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.run(
            workflow_id="workflow_id",
            content_type="content_type",
            file="file",
            file_base64="file_base64",
            filename="filename",
            text="text",
        )
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncAnyformat) -> None:
        response = await async_client.workflows.with_raw_response.run(
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncAnyformat) -> None:
        async with async_client.workflows.with_streaming_response.run(
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowRunResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_run(self, async_client: AsyncAnyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.workflows.with_raw_response.run(
                workflow_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.upload(
            workflow_id="workflow_id",
        )
        assert_matches_type(WorkflowUploadResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncAnyformat) -> None:
        workflow = await async_client.workflows.upload(
            workflow_id="workflow_id",
            content_type="content_type",
            file="file",
            file_base64="file_base64",
            filename="filename",
            text="text",
        )
        assert_matches_type(WorkflowUploadResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncAnyformat) -> None:
        response = await async_client.workflows.with_raw_response.upload(
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowUploadResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncAnyformat) -> None:
        async with async_client.workflows.with_streaming_response.upload(
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowUploadResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncAnyformat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.workflows.with_raw_response.upload(
                workflow_id="",
            )
