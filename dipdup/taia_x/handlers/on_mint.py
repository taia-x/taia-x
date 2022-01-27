
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
    holder, _ = await models.Account.get_or_create(address=mint.parameter.owner)
    creator = holder

    #if await models.Token.exists(id=mint.parameter.token_id):
    #    return

    metadata = ''
    if mint.parameter.token_metadata_uri:
        metadata = fromhex(mint.parameter.token_metadata_uri)

    token = models.Token(
        name='',
        description='',
        artifact_uri='',
        metadata=metadata,
        creator=creator,
        timestamp=mint.data.timestamp,
        price=mint.parameter.price_arg,
        formats=[],
        files=[],
        tags=[]
        #royalties=mint_objkt.parameter.royalties,
        #display_uri='',
        #thumbnail_uri='',
        #mime='',
        #supply=mint.parameter.amount,
        #level=mint.data.level,
    )
    await token.save()

    recipient, _ = await models.Account.get_or_create(address=mint.data.target_address)
    await recipient.save()
    #minter, _ = await models.TokenHolder.get_or_create(holder=holder, token=token)
    #await minter.save()

    #operator, _ = await models.TokenOperator.get_or_create(token=token, owner=holder, operator=mint.parameter.operator)
    #await operator.save()

    event = models.Event(
        token=token,
        creator=holder,
        recipient=recipient,
        event_type=models.EventType.mint,
        ophash=mint.data.hash,
        level=mint.data.level,
        timestamp=mint.data.timestamp,
    )
    await event.save()

    await fix_token_metadata(token)
    await fix_other_metadata()