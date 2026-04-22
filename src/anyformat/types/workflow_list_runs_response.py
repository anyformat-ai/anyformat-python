# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WorkflowListRunsResponse", "Result"]


class Result(BaseModel):
    """
    An extraction run entry, representing one execution of a workflow on a file collection.
    """

    id: str
    """The collection UUID for this run.

    Use this ID with `GET /v2/workflows/{workflow_id}/files/{id}/results/` to fetch
    results.
    """

    status: str
    """Processing status: `pending`, `processing`, `completed`, or `failed`."""

    created_at: Optional[datetime] = None
    """Timestamp when the run started (ISO 8601)."""

    updated_at: Optional[datetime] = None
    """Timestamp when the run status was last updated (ISO 8601)."""


class WorkflowListRunsResponse(BaseModel):
    """Paginated list of workflow runs."""

    count: int
    """Total number of runs for this workflow."""

    page: int
    """Current page number."""

    page_size: int
    """Number of results per page."""

    results: List[Result]
    """List of runs for the current page."""
