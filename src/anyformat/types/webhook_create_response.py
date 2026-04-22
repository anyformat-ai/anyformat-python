# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    """Webhook subscription details including the signing secret.

    The secret is only returned at creation time.
    """

    id: str
    """Unique identifier of the webhook."""

    created_at: str
    """Timestamp when the webhook was created (ISO 8601)."""

    events: List[str]
    """Event types this webhook is subscribed to."""

    is_active: bool
    """Whether the webhook is currently active and receiving events."""

    secret: str
    """Webhook signing secret.

    Use this to verify that incoming webhook requests are authentic. **Store
    securely — this value is only shown once at creation time.**
    """

    url: str
    """The URL receiving webhook events."""
