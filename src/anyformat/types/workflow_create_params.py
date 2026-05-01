# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["WorkflowCreateParams"]


class WorkflowCreateParams(TypedDict, total=False):
    fields: Required[Iterable[Dict[str, object]]]
    """Field definitions"""

    name: Required[str]
    """Workflow name"""

    description: Optional[str]
    """Workflow description"""
