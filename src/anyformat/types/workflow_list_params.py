# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["WorkflowListParams"]


class WorkflowListParams(TypedDict, total=False):
    order: Optional[str]

    page: int

    page_size: int

    sort_by: Optional[str]

    status: Optional[str]
