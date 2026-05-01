# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "WorkflowGetFileResultsResponse",
    "Extraction",
    "ExtractionExtractedField",
    "ExtractionExtractedFieldEvidence",
    "ExtractionUnionMember1ExtractionUnionMember1Item",
    "ExtractionUnionMember1ExtractionUnionMember1ItemEvidence",
    "Parse",
]


class ExtractionExtractedFieldEvidence(BaseModel):
    """
    A snippet of source text supporting an extracted value, with the page it came from.
    """

    page_number: int
    """1-indexed page number where the snippet was found."""

    text: str
    """The exact source-text snippet that supports the extracted value."""


class ExtractionExtractedField(BaseModel):
    """One extracted field's value, confidence, and supporting evidence."""

    value: object
    """The extracted value.

    Type depends on the field's `data_type` (string, number, date, etc.). `null`
    when extraction could not produce a value.
    """

    confidence: Optional[float] = None
    """Model confidence in the extracted value, on a 0-100 scale.

    `null` when the backend did not produce a confidence (e.g. manual entry).
    """

    evidence: Optional[List[ExtractionExtractedFieldEvidence]] = None
    """Source-text snippets the model used to derive this value."""

    value_override: Optional[object] = None
    """
    A human-supplied override of the extracted `value`, if one was set during
    verification. `null` when no override exists.
    """

    verification_status: Optional[str] = None
    """Verification state for this datapoint (e.g.

    `not_verified`, `verified`). `null` when not yet reviewed.
    """


class ExtractionUnionMember1ExtractionUnionMember1ItemEvidence(BaseModel):
    """
    A snippet of source text supporting an extracted value, with the page it came from.
    """

    page_number: int
    """1-indexed page number where the snippet was found."""

    text: str
    """The exact source-text snippet that supports the extracted value."""


class ExtractionUnionMember1ExtractionUnionMember1Item(BaseModel):
    """One extracted field's value, confidence, and supporting evidence."""

    value: object
    """The extracted value.

    Type depends on the field's `data_type` (string, number, date, etc.). `null`
    when extraction could not produce a value.
    """

    confidence: Optional[float] = None
    """Model confidence in the extracted value, on a 0-100 scale.

    `null` when the backend did not produce a confidence (e.g. manual entry).
    """

    evidence: Optional[List[ExtractionUnionMember1ExtractionUnionMember1ItemEvidence]] = None
    """Source-text snippets the model used to derive this value."""

    value_override: Optional[object] = None
    """
    A human-supplied override of the extracted `value`, if one was set during
    verification. `null` when no override exists.
    """

    verification_status: Optional[str] = None
    """Verification state for this datapoint (e.g.

    `not_verified`, `verified`). `null` when not yet reviewed.
    """


Extraction: TypeAlias = Union[
    ExtractionExtractedField, List[Dict[str, ExtractionUnionMember1ExtractionUnionMember1Item]]
]


class Parse(BaseModel):
    """Parsed markdown for a file."""

    markdown: Optional[str] = None
    """
    Document content rendered as structured markdown (with `<DOCUMENT>` /
    `<section>` tags, embedded images for the `visual` variant). `null` if parsing
    failed.
    """


class WorkflowGetFileResultsResponse(BaseModel):
    """Canonical response shape for the file-collection results endpoint.

    Returned with HTTP 200 once processing completes. Returns 412 while processing is
    in progress; poll until 200, or use webhooks.
    """

    collection_id: str
    """The file collection's UUID.

    Same value as the `id` returned by `POST /v2/workflows/{wid}/run/`.
    """

    extraction: Optional[Dict[str, Extraction]] = None
    """Extracted fields keyed by field name.

    `null` for parse-only workflows. Always present in the response. Each value is
    either a scalar field (`ExtractedField`) or a list of object-field rows
    (`list[dict[str, ExtractedField]]`) for compound fields like line items.
    """

    parse: Optional[Parse] = None
    """Parsed markdown for a file."""

    verification_url: Optional[str] = None
    """Link to the AnyFormat dashboard for human review of this collection's results.

    `null` if the dashboard URL cannot be constructed (e.g. no files in the
    collection, or the deployment has no frontend URL configured).
    """
