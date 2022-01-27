
from dipdup.models import Transaction
from taia_x.types.taia_x_fa2.parameter.buy import BuyParameter
from dipdup.context import HandlerContext
from taia_x.types.taia_x_fa2.storage import TaiaX_Fa2Storage

async def on_buy(
    ctx: HandlerContext,
    buy: Transaction[BuyParameter, TaiaX_Fa2Storage],
) -> None:
    ...