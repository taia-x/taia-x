
from dipdup.context import HookContext
import taia_x.models as models

async def on_reindex(
    ctx: HookContext,
) -> None:
    await ctx.execute_sql('on_reindex')
    caller, _ = await models.Account.get_or_create(address="tz1ggvpTMyxX5QVYqbpLVmNGCsgDpDyUMawq", role="certifier")