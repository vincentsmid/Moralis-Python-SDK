# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""

from openapi_evm_api.paths.erc20_address_allowance.get import GetTokenAllowance
from openapi_evm_api.paths.erc20_metadata.get import GetTokenMetadata
from openapi_evm_api.paths.erc20_metadata_symbols.get import GetTokenMetadataBySymbol
from openapi_evm_api.paths.erc20_address_price.get import GetTokenPrice
from openapi_evm_api.paths.erc20_address_transfers.get import GetTokenTransfers
from openapi_evm_api.paths.address_erc20.get import GetWalletTokenBalances
from openapi_evm_api.paths.address_erc20_transfers.get import GetWalletTokenTransfers


class TokenApi(
    GetTokenAllowance,
    GetTokenMetadata,
    GetTokenMetadataBySymbol,
    GetTokenPrice,
    GetTokenTransfers,
    GetWalletTokenBalances,
    GetWalletTokenTransfers,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
