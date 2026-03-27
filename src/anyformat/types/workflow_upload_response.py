# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WorkflowUploadResponse"]


class WorkflowUploadResponse(BaseModel):
    """POST /workflows/{id}/upload/ — upload confirmation."""

    status: str

    filename: Optional[str] = None
