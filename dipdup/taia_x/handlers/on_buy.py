
from dipdup.models import Transaction
from taia_x.types.taia_x_fa2.parameter.buy import BuyParameter
from dipdup.context import HandlerContext
from taia_x.types.taia_x_fa2.storage import TaiaX_Fa2Storage

import aiohttp
from taia_x.utils import http_request
import taia_x.models as models

async def on_buy(
    ctx: HandlerContext,
    buy: Transaction[BuyParameter, TaiaX_Fa2Storage],
) -> None:
    # get token that was purchased from db
    token, _ = await models.Token.get_or_create(id=buy.parameter.__root__)

    # save or get account that purchased the token
    caller, _ = await models.Account.get_or_create(address=buy.data.sender_address)

    # get contract that received entrypoint call
    recipient, _ = await models.Account.get_or_create(address=buy.data.target_address)

    # get operation by ophash from tzkt blockchain indexer to get internal transaction
    async def get_operation():
        addr = f"http://api_tzkt:5000/v1/operations/{buy.data.hash}"
        try:
            session = aiohttp.ClientSession()
            data = await http_request(session, 'get', url=addr, timeout=10)
            await session.close()
            if data:
                return data
        except Exception:
            await session.close()
        return {}
    
    operation = await get_operation()

    token.buyer = caller
    await token.save()
    #await token.buyers.add(caller)
    #await caller.purchases.add(token)
    #await token.save()

    # save buy event in db
    buy_event = models.Event(
        token=token,
        _from=caller,
        _to=recipient,
        price=buy.data.amount,
        event_type=models.EventType.purchase,
        ophash=buy.data.hash,
        level=buy.data.level,
        timestamp=buy.data.timestamp,
    )
    await buy_event.save()

    # save or get receiver of payment from operation
    receiver, _ = await models.Account.get_or_create(address=operation[1]["target"]["address"])
    
    # save transfer event in db
    transfer_event = models.Event(
        token=token,
        _from=recipient,
        _to=receiver,
        price=buy.data.amount,
        event_type=models.EventType.transfer,
        ophash=buy.data.hash,
        level=buy.data.level,
        timestamp=buy.data.timestamp,
    )
    await transfer_event.save()

    # save purchase in db for backend access control
    purchase, _ = await models.Purchase.get_or_create(
     #   token=token
        token_id=buy.parameter.__root__,
        account_id=buy.data.sender_address
    )
    await purchase.save()
    #await purchase.buyer.add(caller)