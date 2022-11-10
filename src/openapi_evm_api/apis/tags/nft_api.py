# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""

from openapi_evm_api.paths.nft_address.get import GetContractNfts
from openapi_evm_api.paths.nft_address_metadata.get import GetNftContractMetadata
from openapi_evm_api.paths.nft_address_transfers.get import GetNftContractTransfers
from openapi_evm_api.paths.nft_address_lowestprice.get import GetNftLowestPrice
from openapi_evm_api.paths.nft_address_token_id.get import GetNftMetadata
from openapi_evm_api.paths.nft_address_owners.get import GetNftOwners
from openapi_evm_api.paths.nft_address_token_id_owners.get import GetNftTokenIdOwners
from openapi_evm_api.paths.nft_address_trades.get import GetNftTrades
from openapi_evm_api.paths.nft_address_token_id_transfers.get import GetNftTransfers
from openapi_evm_api.paths.block_block_number_or_hash_nft_transfers.get import GetNftTransfersByBlock
from openapi_evm_api.paths.nft_transfers.get import GetNftTransfersFromToBlock
from openapi_evm_api.paths.address_nft_collections.get import GetWalletNftCollections
from openapi_evm_api.paths.address_nft_transfers.get import GetWalletNftTransfers
from openapi_evm_api.paths.address_nft.get import GetWalletNfts
from openapi_evm_api.paths.nft_address_token_id_metadata_resync.get import ReSyncMetadata
from openapi_evm_api.paths.nft_search.get import SearchNfts
from openapi_evm_api.paths.nft_address_sync.put import SyncNftContract


class NftApi(
    GetContractNfts,
    GetNftContractMetadata,
    GetNftContractTransfers,
    GetNftLowestPrice,
    GetNftMetadata,
    GetNftOwners,
    GetNftTokenIdOwners,
    GetNftTrades,
    GetNftTransfers,
    GetNftTransfersByBlock,
    GetNftTransfersFromToBlock,
    GetWalletNftCollections,
    GetWalletNftTransfers,
    GetWalletNfts,
    ReSyncMetadata,
    SearchNfts,
    SyncNftContract,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
