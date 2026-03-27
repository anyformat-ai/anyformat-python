# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileListResponse", "Result"]


class Result(BaseModel):
    """A single file collection entry in list responses."""

    id: str

    status: str

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    updated_at: Optional[datetime] = None


class FileListResponse(BaseModel):
    count: int

    page: int

    page_size: int

    results: List[Result]
