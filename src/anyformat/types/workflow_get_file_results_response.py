# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "WorkflowGetFileResultsResponse",
    "Classification",
    "Extraction",
    "ExtractionExtractedField",
    "ExtractionExtractedFieldEvidence",
    "ExtractionUnionMember1ExtractionUnionMember1Item",
    "ExtractionUnionMember1ExtractionUnionMember1ItemEvidence",
    "Parse",
    "ParseBlock",
    "ParseBlockHyperlink",
    "Split",
    "SplitFile",
    "SplitPartition",
    "SplitPartitionFile",
]


class Classification(BaseModel):
    """One classifier verdict for the collection."""

    category: str
    """The category the document was classified as."""

    confidence: float
    """0-100 model confidence in the verdict."""

    evidence: Optional[str] = None
    """Free-form evidence text (the snippets the classifier cited).

    `null` when none captured.
    """


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


class ParseBlockHyperlink(BaseModel):
    """A hyperlink found inside a block's content."""

    text: str
    """The display text of the link."""

    uri: str
    """The link target (URL, mailto:, etc.)."""


class ParseBlock(BaseModel):
    """
    One semantic block of a parsed document — a structured alternative to
    pattern-matching against `<section>` tags inside `markdown`.

    All blocks expose the common fields (`id`, `type`, `page`, `bbox`,
    `confidence`, `content`). Type-specific structured data lives in the
    optional fields (`rows` for tables, `image_base64` for pictures).
    Consumers can switch on `type` to access the per-type fields, or treat
    `content` as the universal fallback.
    """

    id: str
    """Stable block identifier in the form `p<page>_b<index>`."""

    bbox: Dict[str, float]
    """
    Normalised bounding box in [0, 1] page coordinates with keys
    `x0`/`y0`/`x1`/`y1`.
    """

    content: str
    """
    Raw section body — markdown for text/title blocks, HTML for tables,
    `<figure-content>` for pictures.
    """

    layout_confidence: float
    """0-100 YOLO layout detection confidence for this block."""

    page: int
    """1-indexed page number this block belongs to."""

    type: str
    """Semantic type: `text`, `title`, `section-header`, `table`, `picture`, `other`."""

    hyperlinks: Optional[List[ParseBlockHyperlink]] = None
    """Hyperlinks found in the content via `[text](uri)` markdown syntax."""

    image_base64: Optional[str] = None
    """Inline base64-encoded cropped image for `type=picture` blocks.

    Currently `null` for all blocks — image hydration is performed client-side by
    the SDK consumer.
    """

    parse_confidence: Optional[float] = None
    """0-100 parse confidence calibrated from LLM logprobs.

    `null` when logprobs were unavailable (e.g. text-bytes strategy).
    """

    rows: Optional[List[List[Dict[str, str]]]] = None
    """2D array of table cells for `type=table` blocks — each cell is
    `{cell_id, text}`.

    `null` for non-table blocks.
    """


class Parse(BaseModel):
    """Parsed markdown for a file."""

    markdown: Optional[str] = None
    """
    Document content rendered as structured markdown (with `<DOCUMENT>` /
    `<section>` tags). Image hydration for picture/figure blocks happens
    client-side. `null` if parsing failed.
    """

    blocks: Optional[List[ParseBlock]] = None
    """
    Structured per-block representation of the parsed document — derived from
    `markdown` at retrieval time. One entry per `<section>` in document order, with
    type-specific structured data (`rows` for tables, `image_base64` for pictures)
    surfaced as first-class fields so consumers don't have to HTML-parse.
    """

    layout_confidence: Optional[float] = None
    """
    Document-level YOLO layout confidence on a 0-100 scale, char-weighted mean
    across all blocks. `null` if no annotated sections.
    """

    parse_confidence: Optional[float] = None
    """
    Document-level parse confidence on a 0-100 scale, char-weighted mean of
    per-block LLM logprob scores. `null` when no blocks have logprob-based
    confidence.
    """

    text: Optional[str] = None
    """
    Plain markdown text with structural tags stripped — `<DOCUMENT>`, `<section>`,
    `<img>`, and `<figure-content>` wrappers removed, leaving the human-readable
    content only. Useful when feeding the parsed output into an LLM or a search
    index that doesn't need the block-level metadata. `null` if `markdown` is null.
    """


class SplitFile(BaseModel):
    """A file's contribution of pages to a split or partition. 1-indexed."""

    file_id: str
    """The file's UUID."""

    file_name: str
    """The file's display name."""

    pages: List[int]
    """1-indexed page numbers from this file."""


class SplitPartitionFile(BaseModel):
    """A file's contribution of pages to a split or partition. 1-indexed."""

    file_id: str
    """The file's UUID."""

    file_name: str
    """The file's display name."""

    pages: List[int]
    """1-indexed page numbers from this file."""


class SplitPartition(BaseModel):
    """A partition value within a split (e.g. `1234-5678` under `Account Holdings`)."""

    confidence: int
    """0-100 minimum confidence across the partition's ranges."""

    files: List[SplitPartitionFile]

    name: str
    """The partition value (free-form string)."""


class Split(BaseModel):
    """
    A category-level split: which pages of which files fall under it, plus
    any partitions inside it. Extraction data lives under `extractions[]` —
    join by `split_name`.
    """

    confidence: int
    """0-100 aggregate confidence (min across partitions)."""

    files: List[SplitFile]
    """Per-file page lists, union of all partitions."""

    name: str
    """The split's category name."""

    partitions: Optional[List[SplitPartition]] = None


class WorkflowGetFileResultsResponse(BaseModel):
    """Canonical response shape for the file-collection results endpoint.

    Returned with HTTP 200 once processing completes. Returns 412 while processing is
    in progress; poll until 200, or use webhooks.
    """

    collection_id: str
    """The file collection's UUID.

    Same value as the `id` returned by `POST /v2/workflows/{wid}/run/`.
    """

    classifications: Optional[List[Classification]] = None
    """Per-classifier-node verdicts. Empty when the workflow has no classifier."""

    extraction: Optional[Dict[str, Extraction]] = None
    """**Deprecated** — use `extractions` instead.

    Extracted fields keyed by field name, populated only for linear workflows
    (single extract node, no splitter). `null` for split workflows; read
    `extractions[]` instead.
    """

    extractions: Optional[List[Extraction]] = None
    """Flat list of extraction datapoints.

    Linear workflows produce one entry with `split_name=null` and `partition=null`.
    Split workflows produce one entry per (split, partition). Empty when no
    extraction has run yet.
    """

    parse: Optional[Parse] = None
    """Parsed markdown for a file."""

    splits: Optional[List[Split]] = None
    """Splitter output: category-level geometry with optional partitions.

    Empty when the workflow has no splitter.
    """

    verification_url: Optional[str] = None
    """Link to the AnyFormat dashboard for human review of this collection's results.

    `null` if the dashboard URL cannot be constructed (e.g. no files in the
    collection, or the deployment has no frontend URL configured).
    """
