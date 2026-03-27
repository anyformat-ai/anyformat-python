# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["WebhookListResponse", "WebhookListResponseItem"]


class WebhookListResponseItem(BaseModel):
    """Response schema for listing webhooks (excludes secret)"""

    id: str

    created_at: str

    events: List[str]

    is_active: bool

    url: str


WebhookListResponse: TypeAlias = List[WebhookListResponseItem]
