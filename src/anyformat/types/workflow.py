# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Workflow"]


class Workflow(BaseModel):
    """Workflow detail — used for get, create, and list items."""

    id: str

    name: str

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    fields: Optional[List[Dict[str, object]]] = None

    updated_at: Optional[datetime] = None
