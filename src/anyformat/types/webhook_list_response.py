# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["WebhookListResponse", "WebhookListResponseItem"]


class WebhookListResponseItem(BaseModel):
    """Webhook subscription details (secret excluded for security)."""

    id: str
    """Unique identifier of the webhook."""

    created_at: str
    """Timestamp when the webhook was created (ISO 8601)."""

    events: List[str]
    """Event types this webhook is subscribed to."""

    is_active: bool
    """Whether the webhook is currently active."""

    url: str
    """The URL receiving webhook events."""


WebhookListResponse: TypeAlias = List[WebhookListResponseItem]
