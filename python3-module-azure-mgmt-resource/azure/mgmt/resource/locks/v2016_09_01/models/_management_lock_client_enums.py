# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class LockLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete
    means authorized users are able to read and modify the resources, but not delete. ReadOnly
    means authorized users can only read from a resource, but they can't modify or delete it.
    """

    NOT_SPECIFIED = "NotSpecified"
    CAN_NOT_DELETE = "CanNotDelete"
    READ_ONLY = "ReadOnly"