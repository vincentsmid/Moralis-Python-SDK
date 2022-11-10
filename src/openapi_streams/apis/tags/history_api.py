# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from openapi_streams.paths.history.get import GetHistory
from openapi_streams.paths.history_replay_stream_id_id.post import ReplayHistory


class HistoryApi(
    GetHistory,
    ReplayHistory,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
