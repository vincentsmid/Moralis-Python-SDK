# coding: utf-8

"""
    Auth API

    API that provides authentication services for dapps.  # noqa: E501

    The version of the OpenAPI document: 1.0
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

from openapi_auth import schemas  # noqa: F401


class BindVerifyRequestDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "verifications",
        }
        
        class properties:
            
            
            class verifications(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['VerificationDto']:
                        return VerificationDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['VerificationDto'], typing.List['VerificationDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'verifications':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'VerificationDto':
                    return super().__getitem__(i)
            __annotations__ = {
                "verifications": verifications,
            }
    
    verifications: MetaOapg.properties.verifications
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verifications"]) -> MetaOapg.properties.verifications: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["verifications", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verifications"]) -> MetaOapg.properties.verifications: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["verifications", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        verifications: typing.Union[MetaOapg.properties.verifications, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BindVerifyRequestDto':
        return super().__new__(
            cls,
            *args,
            verifications=verifications,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_auth.model.verification_dto import VerificationDto
