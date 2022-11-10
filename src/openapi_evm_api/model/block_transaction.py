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


class BlockTransaction(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "gas_price",
            "receipt_status",
            "receipt_cumulative_gas_used",
            "block_hash",
            "block_number",
            "to_address",
            "transaction_index",
            "nonce",
            "input",
            "receipt_gas_used",
            "block_timestamp",
            "from_address",
            "value",
            "hash",
        }
        
        class properties:
            hash = schemas.StrSchema
            nonce = schemas.StrSchema
            transaction_index = schemas.StrSchema
            from_address = schemas.StrSchema
            
            
            class to_address(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NoneSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'to_address':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            value = schemas.StrSchema
            gas_price = schemas.StrSchema
            input = schemas.StrSchema
            receipt_cumulative_gas_used = schemas.StrSchema
            receipt_gas_used = schemas.StrSchema
            receipt_status = schemas.StrSchema
            block_timestamp = schemas.StrSchema
            block_number = schemas.StrSchema
            block_hash = schemas.StrSchema
            gas = schemas.StrSchema
            
            
            class receipt_contract_address(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NoneSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'receipt_contract_address':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class receipt_root(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NoneSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'receipt_root':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class logs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Log']:
                        return Log
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Log'], typing.List['Log']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'logs':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Log':
                    return super().__getitem__(i)
            __annotations__ = {
                "hash": hash,
                "nonce": nonce,
                "transaction_index": transaction_index,
                "from_address": from_address,
                "to_address": to_address,
                "value": value,
                "gas_price": gas_price,
                "input": input,
                "receipt_cumulative_gas_used": receipt_cumulative_gas_used,
                "receipt_gas_used": receipt_gas_used,
                "receipt_status": receipt_status,
                "block_timestamp": block_timestamp,
                "block_number": block_number,
                "block_hash": block_hash,
                "gas": gas,
                "receipt_contract_address": receipt_contract_address,
                "receipt_root": receipt_root,
                "logs": logs,
            }

    
    gas_price: MetaOapg.properties.gas_price
    receipt_status: MetaOapg.properties.receipt_status
    receipt_cumulative_gas_used: MetaOapg.properties.receipt_cumulative_gas_used
    block_hash: MetaOapg.properties.block_hash
    block_number: MetaOapg.properties.block_number
    to_address: MetaOapg.properties.to_address
    transaction_index: MetaOapg.properties.transaction_index
    nonce: MetaOapg.properties.nonce
    input: MetaOapg.properties.input
    receipt_gas_used: MetaOapg.properties.receipt_gas_used
    block_timestamp: MetaOapg.properties.block_timestamp
    from_address: MetaOapg.properties.from_address
    value: MetaOapg.properties.value
    hash: MetaOapg.properties.hash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas_price"]) -> MetaOapg.properties.gas_price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input"]) -> MetaOapg.properties.input: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_cumulative_gas_used"]) -> MetaOapg.properties.receipt_cumulative_gas_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_gas_used"]) -> MetaOapg.properties.receipt_gas_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_status"]) -> MetaOapg.properties.receipt_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas"]) -> MetaOapg.properties.gas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_contract_address"]) -> MetaOapg.properties.receipt_contract_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_root"]) -> MetaOapg.properties.receipt_root: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logs"]) -> MetaOapg.properties.logs: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hash", "nonce", "transaction_index", "from_address", "to_address", "value", "gas_price", "input", "receipt_cumulative_gas_used", "receipt_gas_used", "receipt_status", "block_timestamp", "block_number", "block_hash", "gas", "receipt_contract_address", "receipt_root", "logs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas_price"]) -> MetaOapg.properties.gas_price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input"]) -> MetaOapg.properties.input: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_cumulative_gas_used"]) -> MetaOapg.properties.receipt_cumulative_gas_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_gas_used"]) -> MetaOapg.properties.receipt_gas_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_status"]) -> MetaOapg.properties.receipt_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas"]) -> typing.Union[MetaOapg.properties.gas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_contract_address"]) -> typing.Union[MetaOapg.properties.receipt_contract_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_root"]) -> typing.Union[MetaOapg.properties.receipt_root, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logs"]) -> typing.Union[MetaOapg.properties.logs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hash", "nonce", "transaction_index", "from_address", "to_address", "value", "gas_price", "input", "receipt_cumulative_gas_used", "receipt_gas_used", "receipt_status", "block_timestamp", "block_number", "block_hash", "gas", "receipt_contract_address", "receipt_root", "logs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        gas_price: typing.Union[MetaOapg.properties.gas_price, str, ],
        receipt_status: typing.Union[MetaOapg.properties.receipt_status, str, ],
        receipt_cumulative_gas_used: typing.Union[MetaOapg.properties.receipt_cumulative_gas_used, str, ],
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        to_address: typing.Union[MetaOapg.properties.to_address, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        transaction_index: typing.Union[MetaOapg.properties.transaction_index, str, ],
        nonce: typing.Union[MetaOapg.properties.nonce, str, ],
        input: typing.Union[MetaOapg.properties.input, str, ],
        receipt_gas_used: typing.Union[MetaOapg.properties.receipt_gas_used, str, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, ],
        from_address: typing.Union[MetaOapg.properties.from_address, str, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        hash: typing.Union[MetaOapg.properties.hash, str, ],
        gas: typing.Union[MetaOapg.properties.gas, str, schemas.Unset] = schemas.unset,
        receipt_contract_address: typing.Union[MetaOapg.properties.receipt_contract_address, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        receipt_root: typing.Union[MetaOapg.properties.receipt_root, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        logs: typing.Union[MetaOapg.properties.logs, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BlockTransaction':
        return super().__new__(
            cls,
            *args,
            gas_price=gas_price,
            receipt_status=receipt_status,
            receipt_cumulative_gas_used=receipt_cumulative_gas_used,
            block_hash=block_hash,
            block_number=block_number,
            to_address=to_address,
            transaction_index=transaction_index,
            nonce=nonce,
            input=input,
            receipt_gas_used=receipt_gas_used,
            block_timestamp=block_timestamp,
            from_address=from_address,
            value=value,
            hash=hash,
            gas=gas,
            receipt_contract_address=receipt_contract_address,
            receipt_root=receipt_root,
            logs=logs,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.log import Log
