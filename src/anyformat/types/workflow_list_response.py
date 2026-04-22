# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .workflow import Workflow

__all__ = ["WorkflowListResponse"]


class WorkflowListResponse(BaseModel):
    """Paginated list of workflows."""

    count: int
    """Total number of workflows matching the query."""

    page: int
    """Current page number."""

    page_size: int
    """Number of results per page."""

    results: List[Workflow]
    """List of workflows for the current page."""
