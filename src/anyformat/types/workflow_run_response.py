# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WorkflowRunResponse"]


class WorkflowRunResponse(BaseModel):
    """Response for workflow run endpoint (v2) — collection UUID as identifier."""

    id: str

    status: str

    workflow_id: str
