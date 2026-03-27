# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["FileCreateResponse", "File"]


class File(BaseModel):
    """A single file within a collection."""

    filename: str

    status: str


class FileCreateResponse(BaseModel):
    """Response from creating a file collection."""

    id: str

    files: List[File]

    workflow_id: str

    name: Optional[str] = None
