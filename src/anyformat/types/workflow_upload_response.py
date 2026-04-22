# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WorkflowUploadResponse"]


class WorkflowUploadResponse(BaseModel):
    """
    Confirmation that a file was uploaded successfully without triggering extraction.
    """

    status: str
    """Upload result: `uploaded` on success."""

    filename: Optional[str] = None
    """Name of the uploaded file."""
