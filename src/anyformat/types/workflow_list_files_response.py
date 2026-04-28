# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WorkflowListFilesResponse", "Result"]


class Result(BaseModel):
    """A file collection entry in list responses.

    Each collection groups one or more uploaded files and tracks their extraction status.
    """

    id: str
    """Unique identifier of the file collection."""

    status: str
    """Processing status: `pending`, `processing`, `completed`, or `failed`."""

    created_at: Optional[datetime] = None
    """Timestamp when the collection was created (ISO 8601)."""

    name: Optional[str] = None
    """Human-readable name for the collection."""

    updated_at: Optional[datetime] = None
    """Timestamp when the collection was last updated (ISO 8601)."""


class WorkflowListFilesResponse(BaseModel):
    count: int
    """Total number of items matching the query."""

    page: int
    """Current page number."""

    page_size: int
    """Number of results per page."""

    results: List[Result]
    """List of items for the current page."""
