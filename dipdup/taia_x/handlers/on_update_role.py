
from taia_x.types.taia_x_fa2.storage import TaiaX_Fa2Storage
from taia_x.types.taia_x_fa2.parameter.update_user_roles import UpdateUserRolesParameter
from dipdup.models import Transaction
from dipdup.context import HandlerContext

import taia_x.models as models
import json

async def on_update_role(
    ctx: HandlerContext,
    update_user_roles: Transaction[UpdateUserRolesParameter, TaiaX_Fa2Storage],
) -> None:
    # save or get account that changed the role
    user, _ = await models.Account.get_or_create(address=update_user_roles.data.sender_address)

    # save new role for account in db
    user.role = list(json.loads(update_user_roles.parameter.json())[0]["add_role"]["role"].keys())[0]
    await user.save()