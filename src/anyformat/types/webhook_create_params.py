# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    url: Required[str]
    """The HTTPS URL to receive webhook events. Must be publicly accessible."""

    events: SequenceNotStr[str]
    """List of event types to subscribe to.

    Available events: `extraction.completed`, `extraction.failed`.
    """
