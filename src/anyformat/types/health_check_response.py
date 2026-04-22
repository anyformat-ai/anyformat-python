# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["HealthCheckResponse"]


class HealthCheckResponse(BaseModel):
    """Health check response confirming the API is operational."""

    message: str
    """Status message. Returns `"ok"` when the service is healthy."""
