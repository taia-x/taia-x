import json
import logging
from pathlib import Path

import os

import aiohttp
from tortoise.query_utils import Q

import taia_x.models as models
from taia_x.utils import clean_null_bytes, http_request

_logger = logging.getLogger(__name__)



async def fix_token_metadata(token):
    metadata = await get_metadata(token)
    token.name = get_name(metadata)
    token.description = get_description(metadata)
    token.artifact_uri = get_artifact_uri(metadata)
    #token.display_uri = get_display_uri(metadata)
    #token.thumbnail_uri = get_thumbnail_uri(metadata)
    #token.mime = get_mime(metadata)
    #token.extra = metadata.get('extra', {})
    #await add_tags(token, metadata)
    await token.save()
    return metadata != {}



async def fix_other_metadata():
    tokens = await models.Token.filter(Q(artifact_uri='')).all().order_by('id').limit(30)
    for token in tokens:
        fixed = await fix_token_metadata(token)
        if fixed:
            _logger.info(f'fixed metadata for {token.id}')
        else:
            _logger.info(f'failed to fix metadata for {token.id}')



async def add_tags(token, metadata):
    tags = [await get_or_create_tag(tag) for tag in get_tags(metadata)]
    for tag in tags:
        token_tag = await models.TokenTag(token=token, tag=tag)
        await token_tag.save()



async def get_or_create_tag(tag):
    tag, _ = await models.Tag.get_or_create(tag=tag)
    return tag



async def get_metadata(token):
    data = await fetch_metadata_cf_ipfs(token)
    if data != {}:
        _logger.info(f'metadata for {token.id} from IPFS')
    else:
        data = await fetch_metadata_bcd(token)
        if data != {}:
            _logger.info(f'metadata for {token.id} from BCD')

    return data



# def normalize_metadata(token, metadata):
#     n = {
#         '__version': 1,
#         'token_id': token.id,
#         'symbol': metadata.get('symbol', 'OBJKT'),
#         'name': get_name(metadata),
#         'description': get_description(metadata),
#         'artifact_uri': get_artifact_uri(metadata),
#         #'display_uri': get_display_uri(metadata),
#         #'thumbnail_uri': get_thumbnail_uri(metadata),
#         #'formats': get_formats(metadata),
#         'creators': get_creators(metadata),
#         # not cleaned / not lowercased, store as-is
#         'tags': metadata.get('tags', []),
#         'extra': {},
#     }

#     return n



async def fetch_metadata_bcd(token):
    session = aiohttp.ClientSession()
    data = await http_request(
        session,
        'get',
        url=f'https://api.better-call.dev/v1/tokens/granadanet/metadata?contract:KT1AgStGnTVLsB8rbNxv8U5wPAA6nSV116mJ&token_id={token.id}',
    )
    await session.close()

    data = [
        obj for obj in data if (obj['contract'] == 'KT1AgStGnTVLsB8rbNxv8U5wPAA6nSV116mJ')
    ]
    try:
        if data and not isinstance(data[0], list):
            return data[0]
    except FileNotFoundError:
        pass
    return {}



async def fetch_metadata_cf_ipfs(token, failed_attempt=0):
    addr = token.metadata.replace('ipfs://', '')
    try:
        session = aiohttp.ClientSession()
        print("FROM IPFS")
        data = await http_request(session, 'get', url=f'http://ipfs:8080/ipfs/{addr}', timeout=10)
        print("FROM IPFS")
        print(data)
        await session.close()
        if data and not isinstance(data, list):
            return data
    except Exception:
        await session.close()
    return {}



def get_mime(metadata):
    if ('formats' in metadata) and metadata['formats'] and ('mimeType' in metadata['formats'][0]):
        return metadata['formats'][0]['mimeType']
    return ''



def get_tags(metadata):
    tags = metadata.get('tags', [])
    cleaned = [clean_null_bytes(tag) for tag in tags]
    lowercased = [tag.lower() for tag in cleaned]
    uniqued = list(set(lowercased))
    return [tag for tag in uniqued if len(tag) < 255]



def get_name(metadata):
    return clean_null_bytes(metadata.get('name', ''))



def get_description(metadata):
    return clean_null_bytes(metadata.get('description', ''))



def get_artifact_uri(metadata):
    if ('token_info' in metadata):
        return clean_null_bytes(metadata.get('assetUri', '') or metadata['token_info'].get('assetUri', ''))
    else:
        return clean_null_bytes(metadata.get('artifactUri', '') or metadata.get('artifact_uri', ''))



def get_display_uri(metadata):
    return clean_null_bytes(metadata.get('display_uri', '') or metadata.get('displayUri', ''))



def get_thumbnail_uri(metadata):
    return clean_null_bytes(metadata.get('thumbnail_uri', '') or metadata.get('thumbnailUri', ''))



def get_formats(metadata):
    return metadata.get('formats', [])



def get_creators(metadata):
    return [clean_null_bytes(x) for x in metadata.get('creators', [])]



def get_creator(metadata):
    return [clean_null_bytes(x) for x in metadata.get('creator', [])]