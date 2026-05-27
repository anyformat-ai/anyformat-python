# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "WorkflowCreateParams",
    "Node",
    "NodeParseNode",
    "NodeClassifyNode",
    "NodeClassifyNodeCategory",
    "NodeSplitterNode",
    "NodeSplitterNodeRule",
    "NodeExtractNode",
    "NodeExtractNodeExtractionSchema",
    "NodeExtractNodeExtractionSchemaField",
    "NodeExtractNodeExtractionSchemaFieldStringField",
    "NodeExtractNodeExtractionSchemaFieldIntegerField",
    "NodeExtractNodeExtractionSchemaFieldFloatField",
    "NodeExtractNodeExtractionSchemaFieldBooleanField",
    "NodeExtractNodeExtractionSchemaFieldDateField",
    "NodeExtractNodeExtractionSchemaFieldDatetimeField",
    "NodeExtractNodeExtractionSchemaFieldEnumField",
    "NodeExtractNodeExtractionSchemaFieldEnumFieldEnumOption",
    "NodeExtractNodeExtractionSchemaFieldMultiSelectField",
    "NodeExtractNodeExtractionSchemaFieldMultiSelectFieldEnumOption",
    "NodeExtractNodeExtractionSchemaFieldObjectField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldStringField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldIntegerField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldFloatField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldBooleanField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldDateField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldDatetimeField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldEnumField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldEnumFieldEnumOption",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldMultiSelectField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldMultiSelectFieldEnumOption",
    "NodeExtractNodeLookupFileUpload",
    "NodeExtractNodeLookupSchema",
    "NodeExtractNodeLookupSchemaStringField",
    "NodeExtractNodeLookupSchemaIntegerField",
    "NodeExtractNodeLookupSchemaFloatField",
    "NodeExtractNodeLookupSchemaBooleanField",
    "NodeExtractNodeLookupSchemaDateField",
    "NodeExtractNodeLookupSchemaDatetimeField",
    "NodeExtractNodeLookupSchemaEnumField",
    "NodeExtractNodeLookupSchemaEnumFieldEnumOption",
    "NodeExtractNodeLookupSchemaMultiSelectField",
    "NodeExtractNodeLookupSchemaMultiSelectFieldEnumOption",
    "NodeExtractNodeLookupSchemaObjectField",
    "NodeExtractNodeLookupSchemaObjectFieldNestedField",
    "NodeExtractNodeLookupSchemaObjectFieldNestedFieldStringField",
    "NodeExtractNodeLookupSchemaObjectFieldNestedFieldIntegerField",
    "NodeExtractNodeLookupSchemaObjectFieldNestedFieldFloatField",
    "NodeExtractNodeLookupSchemaObjectFieldNestedFieldBooleanField",
    "NodeExtractNodeLookupSchemaObjectFieldNestedFieldDateField",
    "NodeExtractNodeLookupSchemaObjectFieldNestedFieldDatetimeField",
    "NodeExtractNodeLookupSchemaObjectFieldNestedFieldEnumField",
    "NodeExtractNodeLookupSchemaObjectFieldNestedFieldEnumFieldEnumOption",
    "NodeExtractNodeLookupSchemaObjectFieldNestedFieldMultiSelectField",
    "NodeExtractNodeLookupSchemaObjectFieldNestedFieldMultiSelectFieldEnumOption",
    "NodeValidateNode",
    "NodeValidateNodeRule",
    "Edge",
]


class WorkflowCreateParams(TypedDict, total=False):
    name: Required[str]

    nodes: Required[Iterable[Node]]

    description: Optional[str]

    edges: Iterable[Edge]


class NodeParseNode(TypedDict, total=False):
    id: Required[str]
    """Stable identifier for this node within the graph."""

    type: Required[Literal["parse"]]

    figure_enhancement: bool

    mode: Literal["standard", "agentic"]

    prompt_hint: Optional[str]
    """Free-form hint shown to the parse model to bias output."""


class NodeClassifyNodeCategory(TypedDict, total=False):
    id: Required[str]
    """Stable category id used as the edge `branch` value when routing."""

    description: Required[str]
    """Free-form description shown to the LLM."""

    name: Required[str]
    """Display name shown to the LLM."""


class NodeClassifyNode(TypedDict, total=False):
    id: Required[str]
    """Stable identifier for this node within the graph."""

    categories: Required[Iterable[NodeClassifyNodeCategory]]

    type: Required[Literal["classify"]]

    user_prompt: Optional[str]
    """Optional prompt prefix for the classifier."""


class NodeSplitterNodeRule(TypedDict, total=False):
    id: Required[str]

    description: Required[str]

    name: Required[str]

    partition_key: str


class NodeSplitterNode(TypedDict, total=False):
    id: Required[str]
    """Stable identifier for this node within the graph."""

    rules: Required[Iterable[NodeSplitterNodeRule]]

    type: Required[Literal["splitter"]]


class NodeExtractNodeExtractionSchemaFieldStringField(TypedDict, total=False):
    data_type: Required[Literal["string"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldIntegerField(TypedDict, total=False):
    data_type: Required[Literal["integer"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldFloatField(TypedDict, total=False):
    data_type: Required[Literal["float"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldBooleanField(TypedDict, total=False):
    data_type: Required[Literal["boolean"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldDateField(TypedDict, total=False):
    data_type: Required[Literal["date"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldDatetimeField(TypedDict, total=False):
    data_type: Required[Literal["datetime"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldEnumFieldEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeExtractionSchemaFieldEnumField(TypedDict, total=False):
    data_type: Required[Literal["enum"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeExtractionSchemaFieldEnumFieldEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldMultiSelectFieldEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeExtractionSchemaFieldMultiSelectField(TypedDict, total=False):
    data_type: Required[Literal["multi_select"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeExtractionSchemaFieldMultiSelectFieldEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldStringField(TypedDict, total=False):
    data_type: Required[Literal["string"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldIntegerField(TypedDict, total=False):
    data_type: Required[Literal["integer"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldFloatField(TypedDict, total=False):
    data_type: Required[Literal["float"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldBooleanField(TypedDict, total=False):
    data_type: Required[Literal["boolean"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldDateField(TypedDict, total=False):
    data_type: Required[Literal["date"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldDatetimeField(TypedDict, total=False):
    data_type: Required[Literal["datetime"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldEnumFieldEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldEnumField(TypedDict, total=False):
    data_type: Required[Literal["enum"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldEnumFieldEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldMultiSelectFieldEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldMultiSelectField(TypedDict, total=False):
    data_type: Required[Literal["multi_select"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[
        Iterable[NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldMultiSelectFieldEnumOption]
    ]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


NodeExtractNodeExtractionSchemaFieldObjectFieldNestedField: TypeAlias = Union[
    NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldStringField,
    NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldIntegerField,
    NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldFloatField,
    NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldBooleanField,
    NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldDateField,
    NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldDatetimeField,
    NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldEnumField,
    NodeExtractNodeExtractionSchemaFieldObjectFieldNestedFieldMultiSelectField,
    object,
]


class NodeExtractNodeExtractionSchemaFieldObjectField(TypedDict, total=False):
    data_type: Required[Literal["object"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    nested_fields: Required[Iterable[NodeExtractNodeExtractionSchemaFieldObjectFieldNestedField]]

    lookup: bool


NodeExtractNodeExtractionSchemaField: TypeAlias = Union[
    NodeExtractNodeExtractionSchemaFieldStringField,
    NodeExtractNodeExtractionSchemaFieldIntegerField,
    NodeExtractNodeExtractionSchemaFieldFloatField,
    NodeExtractNodeExtractionSchemaFieldBooleanField,
    NodeExtractNodeExtractionSchemaFieldDateField,
    NodeExtractNodeExtractionSchemaFieldDatetimeField,
    NodeExtractNodeExtractionSchemaFieldEnumField,
    NodeExtractNodeExtractionSchemaFieldMultiSelectField,
    NodeExtractNodeExtractionSchemaFieldObjectField,
]


class NodeExtractNodeExtractionSchema(TypedDict, total=False):
    """Schema for the fields this node extracts.

    Required. The backend executor populates this from the ORM field tree before constructing the typed node; nothing else should be able to build an ExtractNode without it.
    """

    fields: Required[Iterable[NodeExtractNodeExtractionSchemaField]]
    """Field definitions making up this extract's output."""


class NodeExtractNodeLookupFileUpload(TypedDict, total=False):
    """Inline lookup-file content carried on the typed create call.

    The backend reads ``filename`` + ``content`` (base64-encoded bytes),
    uploads the file to S3 during workflow create, and stores the resulting
    URI in ``ExtractNode.lookup_files``. This field is stripped from the
    persisted ``GraphNode.config`` — it is create-input only.
    """

    content: Required[str]
    """Base64-encoded file bytes."""

    filename: Required[str]


class NodeExtractNodeLookupSchemaStringField(TypedDict, total=False):
    data_type: Required[Literal["string"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaIntegerField(TypedDict, total=False):
    data_type: Required[Literal["integer"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaFloatField(TypedDict, total=False):
    data_type: Required[Literal["float"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaBooleanField(TypedDict, total=False):
    data_type: Required[Literal["boolean"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaDateField(TypedDict, total=False):
    data_type: Required[Literal["date"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaDatetimeField(TypedDict, total=False):
    data_type: Required[Literal["datetime"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaEnumFieldEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeLookupSchemaEnumField(TypedDict, total=False):
    data_type: Required[Literal["enum"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeLookupSchemaEnumFieldEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaMultiSelectFieldEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeLookupSchemaMultiSelectField(TypedDict, total=False):
    data_type: Required[Literal["multi_select"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeLookupSchemaMultiSelectFieldEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaObjectFieldNestedFieldStringField(TypedDict, total=False):
    data_type: Required[Literal["string"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaObjectFieldNestedFieldIntegerField(TypedDict, total=False):
    data_type: Required[Literal["integer"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaObjectFieldNestedFieldFloatField(TypedDict, total=False):
    data_type: Required[Literal["float"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaObjectFieldNestedFieldBooleanField(TypedDict, total=False):
    data_type: Required[Literal["boolean"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaObjectFieldNestedFieldDateField(TypedDict, total=False):
    data_type: Required[Literal["date"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaObjectFieldNestedFieldDatetimeField(TypedDict, total=False):
    data_type: Required[Literal["datetime"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaObjectFieldNestedFieldEnumFieldEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeLookupSchemaObjectFieldNestedFieldEnumField(TypedDict, total=False):
    data_type: Required[Literal["enum"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeLookupSchemaObjectFieldNestedFieldEnumFieldEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


class NodeExtractNodeLookupSchemaObjectFieldNestedFieldMultiSelectFieldEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeLookupSchemaObjectFieldNestedFieldMultiSelectField(TypedDict, total=False):
    data_type: Required[Literal["multi_select"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeLookupSchemaObjectFieldNestedFieldMultiSelectFieldEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    lookup: bool


NodeExtractNodeLookupSchemaObjectFieldNestedField: TypeAlias = Union[
    NodeExtractNodeLookupSchemaObjectFieldNestedFieldStringField,
    NodeExtractNodeLookupSchemaObjectFieldNestedFieldIntegerField,
    NodeExtractNodeLookupSchemaObjectFieldNestedFieldFloatField,
    NodeExtractNodeLookupSchemaObjectFieldNestedFieldBooleanField,
    NodeExtractNodeLookupSchemaObjectFieldNestedFieldDateField,
    NodeExtractNodeLookupSchemaObjectFieldNestedFieldDatetimeField,
    NodeExtractNodeLookupSchemaObjectFieldNestedFieldEnumField,
    NodeExtractNodeLookupSchemaObjectFieldNestedFieldMultiSelectField,
    object,
]


class NodeExtractNodeLookupSchemaObjectField(TypedDict, total=False):
    data_type: Required[Literal["object"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    nested_fields: Required[Iterable[NodeExtractNodeLookupSchemaObjectFieldNestedField]]

    lookup: bool


NodeExtractNodeLookupSchema: TypeAlias = Union[
    NodeExtractNodeLookupSchemaStringField,
    NodeExtractNodeLookupSchemaIntegerField,
    NodeExtractNodeLookupSchemaFloatField,
    NodeExtractNodeLookupSchemaBooleanField,
    NodeExtractNodeLookupSchemaDateField,
    NodeExtractNodeLookupSchemaDatetimeField,
    NodeExtractNodeLookupSchemaEnumField,
    NodeExtractNodeLookupSchemaMultiSelectField,
    NodeExtractNodeLookupSchemaObjectField,
]


class NodeExtractNode(TypedDict, total=False):
    id: Required[str]
    """Stable identifier for this node within the graph."""

    extraction_schema: Required[NodeExtractNodeExtractionSchema]
    """Schema for the fields this node extracts.

    Required. The backend executor populates this from the ORM field tree before
    constructing the typed node; nothing else should be able to build an ExtractNode
    without it.
    """

    type: Required[Literal["extract"]]

    lookup_file_uploads: Iterable[NodeExtractNodeLookupFileUpload]
    """Inline lookup-file content for the typed create call.

    The backend uploads each entry to S3 and stores the resulting URI in
    `lookup_files`; this field is never persisted in GraphNode.config.
    """

    lookup_files: SequenceNotStr[str]
    """Smart-lookup reference document URIs persisted on the extract node."""

    lookup_schema: Iterable[NodeExtractNodeLookupSchema]
    """Typed schema of fields the smart-lookup pass should produce.

    The _backend_ derives this from the field tree (FieldWorkflowVersion rows whose
    source is SMART_LOOKUP) and attaches it to the node before the message hits the
    wire — the worker then reads it directly off the node, with no DB round-trip.
    Default empty: a node without smart-lookup fields carries an empty list.
    """

    lookup_suggestion: Optional[str]
    """Free-form hint shown to the smart-lookup matcher."""

    mode: Literal["standard", "agentic"]

    use_images: bool


class NodeValidateNodeRule(TypedDict, total=False):
    id: Required[str]
    """Stable rule id; round-trips through ValidationResult.rule_id."""

    description: Required[str]
    """Natural-language description shown to the validation model."""

    name: Optional[str]
    """Optional human-readable rule name shown on the rule card in the Studio.

    Stored verbatim on the GraphNode config and surfaced back through the config
    endpoint so renames round-trip.
    """

    severity: Literal["error", "warning"]

    source_fields: SequenceNotStr[str]
    """Persistent ids of fields this rule references."""


class NodeValidateNode(TypedDict, total=False):
    id: Required[str]
    """Stable identifier for this node within the graph."""

    rules: Required[Iterable[NodeValidateNodeRule]]

    type: Required[Literal["validate"]]


Node: TypeAlias = Union[NodeParseNode, NodeClassifyNode, NodeSplitterNode, NodeExtractNode, NodeValidateNode]


class Edge(TypedDict, total=False):
    """A directed edge between two nodes.

    ``branch`` carries the source-port label
    used for routing out of ``classify`` (category id) or ``splitter`` (rule id) nodes.
    """

    source: Required[str]

    target: Required[str]

    branch: Optional[str]
    """Source-port label for branch routing.

    Required when leaving a classify or splitter node by category/rule.
    """
