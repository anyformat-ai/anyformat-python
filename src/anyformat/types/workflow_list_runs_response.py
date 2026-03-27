# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WorkflowListRunsResponse", "Result"]


class Result(BaseModel):
    """Item in GET /workflows/{id}/runs/ paginated list."""

    id: str

    status: str

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None


class WorkflowListRunsResponse(BaseModel):
    """GET /workflows/{id}/runs/ — paginated run list."""

    count: int

    page: int

    page_size: int

    results: List[Result]
