# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2
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


class WalletHistoryTransaction(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "summary",
                    "nft_transfers",
                    "category",
                    "erc20_transfers",
                }
                
                class properties:
                
                    @staticmethod
                    def category() -> typing.Type['ETransactionCategory']:
                        return ETransactionCategory
                    possible_spam = schemas.BoolSchema
                    method_label = schemas.StrSchema
                    summary = schemas.StrSchema
                    
                    
                    class nft_transfers(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['NftTransfer']:
                                return NftTransfer
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['NftTransfer'], typing.List['NftTransfer']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'nft_transfers':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'NftTransfer':
                            return super().__getitem__(i)
                    
                    
                    class erc20_transfer(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Erc20Transaction']:
                                return Erc20Transaction
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['Erc20Transaction'], typing.List['Erc20Transaction']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'erc20_transfer':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Erc20Transaction':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "category": category,
                        "possible_spam": possible_spam,
                        "method_label": method_label,
                        "summary": summary,
                        "nft_transfers": nft_transfers,
                        "erc20_transfer": erc20_transfer,
                    }
        
            
            summary: MetaOapg.properties.summary
            nft_transfers: MetaOapg.properties.nft_transfers
            category: 'ETransactionCategory'
            erc20_transfers: schemas.AnyTypeSchema
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["category"]) -> 'ETransactionCategory': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["method_label"]) -> MetaOapg.properties.method_label: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["nft_transfers"]) -> MetaOapg.properties.nft_transfers: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["erc20_transfer"]) -> MetaOapg.properties.erc20_transfer: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["category", "possible_spam", "method_label", "summary", "nft_transfers", "erc20_transfer", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> 'ETransactionCategory': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["possible_spam"]) -> typing.Union[MetaOapg.properties.possible_spam, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["method_label"]) -> typing.Union[MetaOapg.properties.method_label, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["nft_transfers"]) -> MetaOapg.properties.nft_transfers: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["erc20_transfer"]) -> typing.Union[MetaOapg.properties.erc20_transfer, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["category", "possible_spam", "method_label", "summary", "nft_transfers", "erc20_transfer", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                summary: typing.Union[MetaOapg.properties.summary, str, ],
                nft_transfers: typing.Union[MetaOapg.properties.nft_transfers, list, tuple, ],
                category: 'ETransactionCategory',
                erc20_transfers: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                possible_spam: typing.Union[MetaOapg.properties.possible_spam, bool, schemas.Unset] = schemas.unset,
                method_label: typing.Union[MetaOapg.properties.method_label, str, schemas.Unset] = schemas.unset,
                erc20_transfer: typing.Union[MetaOapg.properties.erc20_transfer, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    summary=summary,
                    nft_transfers=nft_transfers,
                    category=category,
                    erc20_transfers=erc20_transfers,
                    possible_spam=possible_spam,
                    method_label=method_label,
                    erc20_transfer=erc20_transfer,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                BlockTransaction,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletHistoryTransaction':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.block_transaction import BlockTransaction
from openapi_evm_api.model.e_transaction_category import ETransactionCategory
from openapi_evm_api.model.erc20_transaction import Erc20Transaction
from openapi_evm_api.model.nft_transfer import NftTransfer