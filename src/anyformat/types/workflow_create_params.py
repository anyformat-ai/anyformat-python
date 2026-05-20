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

    effort: Optional[Literal["low", "mid", "accurate"]]
    """Effort preset for agentic mode (low/mid/accurate).

    Defaults to 'mid' when `mode='agentic'` and not set; must be omitted when
    `mode='standard'`.
    """

    engine: Literal["Fast", "Performant"]

    figure_enhancement_enabled: bool

    mode: Literal["standard", "agentic"]

    prompt_hint: Optional[str]
    """Free-form hint shown to the parse model to bias output."""

    visual_grounding_enabled: bool


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

    partition_key: Required[str]


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
    """Schema for the fields this node extracts."""

    fields: Required[Iterable[NodeExtractNodeExtractionSchemaField]]
    """Field definitions making up this extract's output."""


class NodeExtractNode(TypedDict, total=False):
    id: Required[str]
    """Stable identifier for this node within the graph."""

    extraction_schema: Required[NodeExtractNodeExtractionSchema]
    """Schema for the fields this node extracts."""

    type: Required[Literal["extract"]]

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
