# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Workflow"]


class Workflow(BaseModel):
    """
    A workflow defines the extraction template — what fields to extract from documents, their types, and validation rules.
    """

    id: str
    """Unique identifier of the workflow (UUID)."""

    name: str
    """Human-readable name of the workflow."""

    created_at: Optional[datetime] = None
    """Timestamp when the workflow was created (ISO 8601)."""

    description: Optional[str] = None
    """Optional description of what this workflow extracts."""

    fields: Optional[List[Dict[str, object]]] = None
    """List of extraction field definitions configured for this workflow.

    `null` if not yet configured.
    """

    updated_at: Optional[datetime] = None
    """Timestamp when the workflow was last modified (ISO 8601)."""
