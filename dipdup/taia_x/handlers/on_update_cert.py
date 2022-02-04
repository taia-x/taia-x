
from taia_x.types.taia_x_fa2.storage import TaiaX_Fa2Storage
from taia_x.types.taia_x_fa2.parameter.update_certs import UpdateCertsParameter
from dipdup.context import HandlerContext
from dipdup.models import Transaction

import taia_x.models as models
import json

async def on_update_cert(
    ctx: HandlerContext,
    update_certs: Transaction[UpdateCertsParameter, TaiaX_Fa2Storage],
) -> None:
    nft_id = json.loads(update_certs.parameter.json())[0]["certify"]["dataset_id"] if list(json.loads(update_certs.parameter.json())[0].keys())[0] == "certify" else json.loads(update_certs.parameter.json())[0]["reject"]["dataset_id"]

    # update cert_state for token
    token, _ = await models.Token.get_or_create(id=nft_id)
    token.cert_state = models.CertState.certified if list(json.loads(update_certs.parameter.json())[0].keys())[0] == "certify" else models.CertState.rejected
    await token.save()
