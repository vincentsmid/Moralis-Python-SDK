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


class Trade(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "token_ids",
            "buyer_address",
            "price",
            "block_timestamp",
            "block_hash",
            "block_number",
            "marketplace_address",
            "token_address",
            "transaction_index",
            "seller_address",
            "transaction_hash",
        }
        
        class properties:
            transaction_hash = schemas.StrSchema
            transaction_index = schemas.StrSchema
            
            
            class token_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'token_ids':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            seller_address = schemas.StrSchema
            buyer_address = schemas.StrSchema
            marketplace_address = schemas.StrSchema
            price = schemas.StrSchema
            block_timestamp = schemas.StrSchema
            block_number = schemas.StrSchema
            block_hash = schemas.StrSchema
            __annotations__ = {
                "transaction_hash": transaction_hash,
                "transaction_index": transaction_index,
                "token_ids": token_ids,
                "seller_address": seller_address,
                "buyer_address": buyer_address,
                "marketplace_address": marketplace_address,
                "price": price,
                "block_timestamp": block_timestamp,
                "block_number": block_number,
                "block_hash": block_hash,
            }

    
    token_ids: MetaOapg.properties.token_ids
    buyer_address: MetaOapg.properties.buyer_address
    price: MetaOapg.properties.price
    block_timestamp: MetaOapg.properties.block_timestamp
    block_hash: MetaOapg.properties.block_hash
    block_number: MetaOapg.properties.block_number
    marketplace_address: MetaOapg.properties.marketplace_address
    token_address: schemas.AnyTypeSchema
    transaction_index: MetaOapg.properties.transaction_index
    seller_address: MetaOapg.properties.seller_address
    transaction_hash: MetaOapg.properties.transaction_hash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_ids"]) -> MetaOapg.properties.token_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seller_address"]) -> MetaOapg.properties.seller_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buyer_address"]) -> MetaOapg.properties.buyer_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["marketplace_address"]) -> MetaOapg.properties.marketplace_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "transaction_index", "token_ids", "seller_address", "buyer_address", "marketplace_address", "price", "block_timestamp", "block_number", "block_hash", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_ids"]) -> MetaOapg.properties.token_ids: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seller_address"]) -> MetaOapg.properties.seller_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buyer_address"]) -> MetaOapg.properties.buyer_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["marketplace_address"]) -> MetaOapg.properties.marketplace_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "transaction_index", "token_ids", "seller_address", "buyer_address", "marketplace_address", "price", "block_timestamp", "block_number", "block_hash", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        token_ids: typing.Union[MetaOapg.properties.token_ids, list, tuple, ],
        buyer_address: typing.Union[MetaOapg.properties.buyer_address, str, ],
        price: typing.Union[MetaOapg.properties.price, str, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, ],
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        marketplace_address: typing.Union[MetaOapg.properties.marketplace_address, str, ],
        token_address: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        transaction_index: typing.Union[MetaOapg.properties.transaction_index, str, ],
        seller_address: typing.Union[MetaOapg.properties.seller_address, str, ],
        transaction_hash: typing.Union[MetaOapg.properties.transaction_hash, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Trade':
        return super().__new__(
            cls,
            *args,
            token_ids=token_ids,
            buyer_address=buyer_address,
            price=price,
            block_timestamp=block_timestamp,
            block_hash=block_hash,
            block_number=block_number,
            marketplace_address=marketplace_address,
            token_address=token_address,
            transaction_index=transaction_index,
            seller_address=seller_address,
            transaction_hash=transaction_hash,
            _configuration=_configuration,
            **kwargs,
        )
