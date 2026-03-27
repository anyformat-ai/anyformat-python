# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .workflow import Workflow

__all__ = ["WorkflowListResponse"]


class WorkflowListResponse(BaseModel):
    """GET /workflows/ — paginated workflow list."""

    count: int

    page: int

    page_size: int

    results: List[Workflow]
