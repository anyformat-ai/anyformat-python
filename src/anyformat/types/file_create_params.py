# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    files: Required[SequenceNotStr[str]]

    workflow_id: Required[str]
