# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["WorkflowRunParams"]


class WorkflowRunParams(TypedDict, total=False):
    content_type: Optional[str]

    file: Optional[str]

    file_base64: Optional[str]

    filename: Optional[str]

    text: Optional[str]
