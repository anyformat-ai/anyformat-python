# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "WorkflowCreateParams",
    "Field",
    "FieldStringFieldDef",
    "FieldIntegerFieldDef",
    "FieldFloatFieldDef",
    "FieldBooleanFieldDef",
    "FieldDateFieldDef",
    "FieldDatetimeFieldDef",
    "FieldEnumFieldDef",
    "FieldEnumFieldDefEnumOption",
    "FieldMultiSelectFieldDef",
    "FieldMultiSelectFieldDefEnumOption",
    "FieldObjectFieldDef",
    "FieldObjectFieldDefNestedField",
    "FieldObjectFieldDefNestedFieldStringFieldDef",
    "FieldObjectFieldDefNestedFieldIntegerFieldDef",
    "FieldObjectFieldDefNestedFieldFloatFieldDef",
    "FieldObjectFieldDefNestedFieldBooleanFieldDef",
    "FieldObjectFieldDefNestedFieldDateFieldDef",
    "FieldObjectFieldDefNestedFieldDatetimeFieldDef",
    "FieldObjectFieldDefNestedFieldEnumFieldDef",
    "FieldObjectFieldDefNestedFieldEnumFieldDefEnumOption",
    "FieldObjectFieldDefNestedFieldMultiSelectFieldDef",
    "FieldObjectFieldDefNestedFieldMultiSelectFieldDefEnumOption",
]


class WorkflowCreateParams(TypedDict, total=False):
    fields: Required[Iterable[Field]]
    """Field definitions. Each entry's shape is determined by its `data_type`."""

    name: Required[str]
    """Workflow name"""

    description: Optional[str]
    """Workflow description"""


class FieldStringFieldDef(TypedDict, total=False):
    data_type: Required[Literal["string"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldIntegerFieldDef(TypedDict, total=False):
    data_type: Required[Literal["integer"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldFloatFieldDef(TypedDict, total=False):
    data_type: Required[Literal["float"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldBooleanFieldDef(TypedDict, total=False):
    data_type: Required[Literal["boolean"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldDateFieldDef(TypedDict, total=False):
    data_type: Required[Literal["date"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldDatetimeFieldDef(TypedDict, total=False):
    data_type: Required[Literal["datetime"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldEnumFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class FieldEnumFieldDef(TypedDict, total=False):
    data_type: Required[Literal["enum"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[FieldEnumFieldDefEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldMultiSelectFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class FieldMultiSelectFieldDef(TypedDict, total=False):
    data_type: Required[Literal["multi_select"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[FieldMultiSelectFieldDefEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldObjectFieldDefNestedFieldStringFieldDef(TypedDict, total=False):
    data_type: Required[Literal["string"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldObjectFieldDefNestedFieldIntegerFieldDef(TypedDict, total=False):
    data_type: Required[Literal["integer"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldObjectFieldDefNestedFieldFloatFieldDef(TypedDict, total=False):
    data_type: Required[Literal["float"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldObjectFieldDefNestedFieldBooleanFieldDef(TypedDict, total=False):
    data_type: Required[Literal["boolean"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldObjectFieldDefNestedFieldDateFieldDef(TypedDict, total=False):
    data_type: Required[Literal["date"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldObjectFieldDefNestedFieldDatetimeFieldDef(TypedDict, total=False):
    data_type: Required[Literal["datetime"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldObjectFieldDefNestedFieldEnumFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class FieldObjectFieldDefNestedFieldEnumFieldDef(TypedDict, total=False):
    data_type: Required[Literal["enum"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[FieldObjectFieldDefNestedFieldEnumFieldDefEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


class FieldObjectFieldDefNestedFieldMultiSelectFieldDefEnumOption(TypedDict, total=False):
    description: Required[str]
    """Free-form description shown to the model."""

    name: Required[str]


class FieldObjectFieldDefNestedFieldMultiSelectFieldDef(TypedDict, total=False):
    data_type: Required[Literal["multi_select"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    enum_options: Required[Iterable[FieldObjectFieldDefNestedFieldMultiSelectFieldDefEnumOption]]

    name: Required[str]
    """Field name. Used as the key in the extraction response."""


FieldObjectFieldDefNestedField: TypeAlias = Union[
    FieldObjectFieldDefNestedFieldStringFieldDef,
    FieldObjectFieldDefNestedFieldIntegerFieldDef,
    FieldObjectFieldDefNestedFieldFloatFieldDef,
    FieldObjectFieldDefNestedFieldBooleanFieldDef,
    FieldObjectFieldDefNestedFieldDateFieldDef,
    FieldObjectFieldDefNestedFieldDatetimeFieldDef,
    FieldObjectFieldDefNestedFieldEnumFieldDef,
    FieldObjectFieldDefNestedFieldMultiSelectFieldDef,
    object,
]


class FieldObjectFieldDef(TypedDict, total=False):
    data_type: Required[Literal["object"]]

    description: Required[str]
    """Free-form description shown to the extraction model."""

    name: Required[str]
    """Field name. Used as the key in the extraction response."""

    nested_fields: Required[Iterable[FieldObjectFieldDefNestedField]]


Field: TypeAlias = Union[
    FieldStringFieldDef,
    FieldIntegerFieldDef,
    FieldFloatFieldDef,
    FieldBooleanFieldDef,
    FieldDateFieldDef,
    FieldDatetimeFieldDef,
    FieldEnumFieldDef,
    FieldMultiSelectFieldDef,
    FieldObjectFieldDef,
]
