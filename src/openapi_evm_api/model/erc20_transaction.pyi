# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_evm_api import schemas  # noqa: F401


class Erc20Transaction(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "address",
            "block_timestamp",
            "block_hash",
            "block_number",
            "to_address",
            "from_address",
            "value",
            "transaction_hash",
        }
        
        class properties:
            transaction_hash = schemas.StrSchema
            address = schemas.StrSchema
            block_timestamp = schemas.StrSchema
            block_number = schemas.StrSchema
            block_hash = schemas.StrSchema
            to_address = schemas.StrSchema
            from_address = schemas.StrSchema
            value = schemas.StrSchema
            __annotations__ = {
                "transaction_hash": transaction_hash,
                "address": address,
                "block_timestamp": block_timestamp,
                "block_number": block_number,
                "block_hash": block_hash,
                "to_address": to_address,
                "from_address": from_address,
                "value": value,
            }

    
    address: MetaOapg.properties.address
    block_timestamp: MetaOapg.properties.block_timestamp
    block_hash: MetaOapg.properties.block_hash
    block_number: MetaOapg.properties.block_number
    to_address: MetaOapg.properties.to_address
    from_address: MetaOapg.properties.from_address
    value: MetaOapg.properties.value
    transaction_hash: MetaOapg.properties.transaction_hash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "address", "block_timestamp", "block_number", "block_hash", "to_address", "from_address", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "address", "block_timestamp", "block_number", "block_hash", "to_address", "from_address", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, ],
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        to_address: typing.Union[MetaOapg.properties.to_address, str, ],
        from_address: typing.Union[MetaOapg.properties.from_address, str, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        transaction_hash: typing.Union[MetaOapg.properties.transaction_hash, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Erc20Transaction':
        return super().__new__(
            cls,
            *args,
            address=address,
            block_timestamp=block_timestamp,
            block_hash=block_hash,
            block_number=block_number,
            to_address=to_address,
            from_address=from_address,
            value=value,
            transaction_hash=transaction_hash,
            _configuration=_configuration,
            **kwargs,
        )
