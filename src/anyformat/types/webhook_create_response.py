# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    """Response schema for webhook subscription (includes secret)"""

    id: str

    created_at: str

    events: List[str]

    is_active: bool

    secret: str

    url: str
