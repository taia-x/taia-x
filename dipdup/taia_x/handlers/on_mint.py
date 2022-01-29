
from dipdup.context import HandlerContext
from dipdup.models import Transaction
from taia_x.metadata_utils import fix_other_metadata, fix_token_metadata
from taia_x.types.taia_x_fa2.storage import TaiaX_Fa2Storage
from taia_x.types.taia_x_fa2.parameter.mint import MintParameter
from taia_x.utils import fromhex
from random import randrange

import taia_x.models as models

async def on_mint(
    ctx: HandlerContext,
    mint: Transaction[MintParameter, TaiaX_Fa2Storage],
) -> None:
    # save or get account that minted a new token
    creator, _ = await models.Account.get_or_create(address=mint.parameter.owner)

    metadata = ''
    if mint.parameter.token_metadata_uri:
        metadata = fromhex(mint.parameter.token_metadata_uri)

    # save token in db
    token = models.Token(
        name='',
        description='',
        artifact_uri='',
        metadata=metadata,
        creator=creator,
        timestamp=mint.data.timestamp,
        hash=mint.parameter.hash,
        price=mint.parameter.price,
        cert_state=models.CertState.pending,
        formats=[],
        files=[],
        tags=[]
    )
    await token.save()

    # save or create recipient of the event in db
    recipient, _ = await models.Account.get_or_create(address=mint.data.target_address)
    await recipient.save()

    # save mint event in db
    event = models.Event(
        token=token,
        caller=creator,
        recipient=recipient,
        event_type=models.EventType.mint,
        ophash=mint.data.hash,
        level=mint.data.level,
        timestamp=mint.data.timestamp,
    )
    await event.save()

    # get metadata from ipfs and save information related to this token
    await fix_token_metadata(token)
    await fix_other_metadata()