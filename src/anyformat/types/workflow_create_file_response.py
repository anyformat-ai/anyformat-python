# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WorkflowCreateFileResponse", "File"]


class File(BaseModel):
    """A single file within a collection, showing its name and upload status."""

    filename: str
    """Name of the uploaded file."""

    status: str
    """Upload status: `uploaded` or `failed`."""


class WorkflowCreateFileResponse(BaseModel):
    """Response from creating a file collection.

    Contains the collection ID and the status of each uploaded file.
    """

    id: str
    """Unique identifier of the newly created file collection."""

    files: List[File]
    """List of files included in the collection, with their upload status."""

    workflow_id: str
    """The UUID of the workflow this collection belongs to."""

    name: Optional[str] = None
    """Human-readable name for the collection."""
