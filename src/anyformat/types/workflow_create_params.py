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
    "NodeExtractNodeExtractionSchemaFieldStringFieldDef",
    "NodeExtractNodeExtractionSchemaFieldIntegerFieldDef",
    "NodeExtractNodeExtractionSchemaFieldFloatFieldDef",
    "NodeExtractNodeExtractionSchemaFieldBooleanFieldDef",
    "NodeExtractNodeExtractionSchemaFieldDateFieldDef",
    "NodeExtractNodeExtractionSchemaFieldDatetimeFieldDef",
    "NodeExtractNodeExtractionSchemaFieldEnumFieldDef",
    "NodeExtractNodeExtractionSchemaFieldEnumFieldDefEnumOption",
    "NodeExtractNodeExtractionSchemaFieldMultiSelectFieldDef",
    "NodeExtractNodeExtractionSchemaFieldMultiSelectFieldDefEnumOption",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDef",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedField",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldStringFieldDef",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldIntegerFieldDef",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldFloatFieldDef",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldBooleanFieldDef",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldDateFieldDef",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldDatetimeFieldDef",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldEnumFieldDef",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldEnumFieldDefEnumOption",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldMultiSelectFieldDef",
    "NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldMultiSelectFieldDefEnumOption",
    "NodeExtractNodeLookupSchema",
    "NodeExtractNodeLookupSchemaStringFieldDef",
    "NodeExtractNodeLookupSchemaIntegerFieldDef",
    "NodeExtractNodeLookupSchemaFloatFieldDef",
    "NodeExtractNodeLookupSchemaBooleanFieldDef",
    "NodeExtractNodeLookupSchemaDateFieldDef",
    "NodeExtractNodeLookupSchemaDatetimeFieldDef",
    "NodeExtractNodeLookupSchemaEnumFieldDef",
    "NodeExtractNodeLookupSchemaEnumFieldDefEnumOption",
    "NodeExtractNodeLookupSchemaMultiSelectFieldDef",
    "NodeExtractNodeLookupSchemaMultiSelectFieldDefEnumOption",
    "NodeExtractNodeLookupSchemaObjectFieldDef",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedField",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldStringFieldDef",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldIntegerFieldDef",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldFloatFieldDef",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldBooleanFieldDef",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldDateFieldDef",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldDatetimeFieldDef",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldEnumFieldDef",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldEnumFieldDefEnumOption",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldMultiSelectFieldDef",
    "NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldMultiSelectFieldDefEnumOption",
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


class NodeExtractNodeExtractionSchemaFieldStringFieldDef(TypedDict, total=False):
    data_type: Required[Literal["string"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldIntegerFieldDef(TypedDict, total=False):
    data_type: Required[Literal["integer"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldFloatFieldDef(TypedDict, total=False):
    data_type: Required[Literal["float"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldBooleanFieldDef(TypedDict, total=False):
    data_type: Required[Literal["boolean"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldDateFieldDef(TypedDict, total=False):
    data_type: Required[Literal["date"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldDatetimeFieldDef(TypedDict, total=False):
    data_type: Required[Literal["datetime"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldEnumFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeExtractionSchemaFieldEnumFieldDef(TypedDict, total=False):
    data_type: Required[Literal["enum"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeExtractionSchemaFieldEnumFieldDefEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldMultiSelectFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeExtractionSchemaFieldMultiSelectFieldDef(TypedDict, total=False):
    data_type: Required[Literal["multi_select"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeExtractionSchemaFieldMultiSelectFieldDefEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldStringFieldDef(TypedDict, total=False):
    data_type: Required[Literal["string"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldIntegerFieldDef(TypedDict, total=False):
    data_type: Required[Literal["integer"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldFloatFieldDef(TypedDict, total=False):
    data_type: Required[Literal["float"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldBooleanFieldDef(TypedDict, total=False):
    data_type: Required[Literal["boolean"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldDateFieldDef(TypedDict, total=False):
    data_type: Required[Literal["date"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldDatetimeFieldDef(TypedDict, total=False):
    data_type: Required[Literal["datetime"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldEnumFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldEnumFieldDef(TypedDict, total=False):
    data_type: Required[Literal["enum"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[
        Iterable[NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldEnumFieldDefEnumOption]
    ]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldMultiSelectFieldDefEnumOption(
    TypedDict, total=False
):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldMultiSelectFieldDef(TypedDict, total=False):
    data_type: Required[Literal["multi_select"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[
        Iterable[NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldMultiSelectFieldDefEnumOption]
    ]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedField: TypeAlias = Union[
    NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldStringFieldDef,
    NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldIntegerFieldDef,
    NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldFloatFieldDef,
    NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldBooleanFieldDef,
    NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldDateFieldDef,
    NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldDatetimeFieldDef,
    NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldEnumFieldDef,
    NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedFieldMultiSelectFieldDef,
    object,
]


class NodeExtractNodeExtractionSchemaFieldObjectFieldDef(TypedDict, total=False):
    data_type: Required[Literal["object"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    nested_fields: Required[Iterable[NodeExtractNodeExtractionSchemaFieldObjectFieldDefNestedField]]


NodeExtractNodeExtractionSchemaField: TypeAlias = Union[
    NodeExtractNodeExtractionSchemaFieldStringFieldDef,
    NodeExtractNodeExtractionSchemaFieldIntegerFieldDef,
    NodeExtractNodeExtractionSchemaFieldFloatFieldDef,
    NodeExtractNodeExtractionSchemaFieldBooleanFieldDef,
    NodeExtractNodeExtractionSchemaFieldDateFieldDef,
    NodeExtractNodeExtractionSchemaFieldDatetimeFieldDef,
    NodeExtractNodeExtractionSchemaFieldEnumFieldDef,
    NodeExtractNodeExtractionSchemaFieldMultiSelectFieldDef,
    NodeExtractNodeExtractionSchemaFieldObjectFieldDef,
]


class NodeExtractNodeExtractionSchema(TypedDict, total=False):
    """Schema for the fields this node extracts.

    Required. The backend executor populates this from the ORM field tree before constructing the typed node; nothing else should be able to build an ExtractNode without it.
    """

    fields: Required[Iterable[NodeExtractNodeExtractionSchemaField]]
    """Field definitions making up this extract's output."""


class NodeExtractNodeLookupSchemaStringFieldDef(TypedDict, total=False):
    data_type: Required[Literal["string"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaIntegerFieldDef(TypedDict, total=False):
    data_type: Required[Literal["integer"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaFloatFieldDef(TypedDict, total=False):
    data_type: Required[Literal["float"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaBooleanFieldDef(TypedDict, total=False):
    data_type: Required[Literal["boolean"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaDateFieldDef(TypedDict, total=False):
    data_type: Required[Literal["date"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaDatetimeFieldDef(TypedDict, total=False):
    data_type: Required[Literal["datetime"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaEnumFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeLookupSchemaEnumFieldDef(TypedDict, total=False):
    data_type: Required[Literal["enum"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeLookupSchemaEnumFieldDefEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaMultiSelectFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeLookupSchemaMultiSelectFieldDef(TypedDict, total=False):
    data_type: Required[Literal["multi_select"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeLookupSchemaMultiSelectFieldDefEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldStringFieldDef(TypedDict, total=False):
    data_type: Required[Literal["string"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldIntegerFieldDef(TypedDict, total=False):
    data_type: Required[Literal["integer"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldFloatFieldDef(TypedDict, total=False):
    data_type: Required[Literal["float"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldBooleanFieldDef(TypedDict, total=False):
    data_type: Required[Literal["boolean"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldDateFieldDef(TypedDict, total=False):
    data_type: Required[Literal["date"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldDatetimeFieldDef(TypedDict, total=False):
    data_type: Required[Literal["datetime"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldEnumFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldEnumFieldDef(TypedDict, total=False):
    data_type: Required[Literal["enum"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldEnumFieldDefEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldMultiSelectFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldMultiSelectFieldDef(TypedDict, total=False):
    data_type: Required[Literal["multi_select"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldMultiSelectFieldDefEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


NodeExtractNodeLookupSchemaObjectFieldDefNestedField: TypeAlias = Union[
    NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldStringFieldDef,
    NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldIntegerFieldDef,
    NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldFloatFieldDef,
    NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldBooleanFieldDef,
    NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldDateFieldDef,
    NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldDatetimeFieldDef,
    NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldEnumFieldDef,
    NodeExtractNodeLookupSchemaObjectFieldDefNestedFieldMultiSelectFieldDef,
    object,
]


class NodeExtractNodeLookupSchemaObjectFieldDef(TypedDict, total=False):
    data_type: Required[Literal["object"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    nested_fields: Required[Iterable[NodeExtractNodeLookupSchemaObjectFieldDefNestedField]]


NodeExtractNodeLookupSchema: TypeAlias = Union[
    NodeExtractNodeLookupSchemaStringFieldDef,
    NodeExtractNodeLookupSchemaIntegerFieldDef,
    NodeExtractNodeLookupSchemaFloatFieldDef,
    NodeExtractNodeLookupSchemaBooleanFieldDef,
    NodeExtractNodeLookupSchemaDateFieldDef,
    NodeExtractNodeLookupSchemaDatetimeFieldDef,
    NodeExtractNodeLookupSchemaEnumFieldDef,
    NodeExtractNodeLookupSchemaMultiSelectFieldDef,
    NodeExtractNodeLookupSchemaObjectFieldDef,
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
