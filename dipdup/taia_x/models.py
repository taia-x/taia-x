from tortoise import Model, fields
from datetime import datetime
from enum import Enum, IntEnum
import asyncio

class EventType(str, Enum):
    unspecified = 'unspecified'
    mint = 'mint'
    certify = 'certify'
    reject = 'reject'
    purchase = 'purchase'
    transfer = 'transfer'

class CertState(str, Enum):
    unspecified = 'unspecified'
    rejected = 'rejected'
    certified = 'certified'
    pending = 'pending'

class Token(Model):
    id = fields.BigIntField(pk=True)
    creator = fields.ForeignKeyField('models.Account', 'creations', index=True, null=True)
    name = fields.TextField(default='')
    description = fields.TextField(default='')
    artifact_uri = fields.TextField(default='')
    metadata = fields.TextField(default='')
    timestamp = fields.DatetimeField(default=datetime.utcnow())
    formats = fields.JSONField(default=[])
    files = fields.JSONField(default=[])
    tags = fields.JSONField(default=[])
    #buyers = fields.ManyToManyField("models.Account", related_name="purchases", through="token_account", null=True)
    buyer = fields.ForeignKeyField('models.Account', 'purchases', index=True, null=True)
    price = fields.BigIntField(null=False)
    cert_state = fields.CharEnumField(CertState, default=CertState.unspecified)
    hash = fields.CharField(64, null=False)

class Account(Model):
    address = fields.CharField(36, pk=True)
    name = fields.TextField(default='')
    description = fields.TextField(default='')
    metadata_file = fields.TextField(default='')
    #purchases: fields.ManyToManyRelation[Token]
    role = fields.TextField(default='')

class Event(Model):
    id = fields.BigIntField(pk=True)
    token = fields.ForeignKeyField('models.Token', 'events', null=True, index=True)
    _from = fields.ForeignKeyField('models.Account', 'events_from', null=True, index=True)
    _to = fields.ForeignKeyField('models.Account', 'events_to', null=True, index=True)
    event_type = fields.CharEnumField(EventType, default=EventType.unspecified)
    price = fields.BigIntField(null=True)
    ophash = fields.CharField(51)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()

#class Purchase(Model):
#    id = fields.BigIntField(pk=True)
    #nft_id = fields.BigIntField()
 #   token = fields.ForeignKeyField('models.Token', 'purchases', null=True, index=True)
  #  buyer = fields.ManyToManyField('models.Account', 'purchases')

class Purchase(Model):
    #id = fields.BigIntField(pk=True)
    token_id = fields.BigIntField(pk=True)
    account_id = fields.CharField(36)

    #class Meta:
     #   table = "token_account"