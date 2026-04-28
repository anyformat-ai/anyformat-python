# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WorkflowRunResponse"]


class WorkflowRunResponse(BaseModel):
    """Response after triggering a workflow run.

    Contains the collection ID to use for polling extraction results.
    """

    id: str
    """The collection UUID for this run.

    Use this ID to poll for results via
    `GET /v2/workflows/{workflow_id}/files/{id}/results/`.
    """

    status: str
    """
    Initial status of the run, typically `success` (meaning the run was accepted,
    not that extraction is complete).
    """

    workflow_id: str
    """The UUID of the workflow that was executed."""
