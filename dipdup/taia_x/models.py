from tortoise import Model, fields
from datetime import datetime
from enum import Enum, IntEnum

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

class Account(Model):
    address = fields.CharField(36, pk=True)
    name = fields.TextField(default='')
    description = fields.TextField(default='')
    metadata_file = fields.TextField(default='')
    role = fields.TextField(default='')

class Token(Model):
    id = fields.BigIntField(pk=True)
    creator = fields.ForeignKeyField('models.Account', 'tokens', index=True, null=True)
    name = fields.TextField(default='')
    description = fields.TextField(default='')
    artifact_uri = fields.TextField(default='')
    metadata = fields.TextField(default='')
    timestamp = fields.DatetimeField(default=datetime.utcnow())
    formats = fields.JSONField(default=[])
    files = fields.JSONField(default=[])
    tags = fields.JSONField(default=[])
    price = fields.BigIntField(null=False)
    cert_state = fields.CharEnumField(CertState, default=CertState.unspecified)
    hash = fields.CharField(64, null=False)

class Event(Model):
    id = fields.BigIntField(pk=True)
    token = fields.ForeignKeyField('models.Token', 'events', null=True, index=True)
    caller = fields.ForeignKeyField('models.Account', 'calls', null=True, index=True)
    recipient = fields.ForeignKeyField('models.Account', 'receivings', null=True, index=True)
    event_type = fields.CharEnumField(EventType, default=EventType.unspecified)
    price = fields.BigIntField(null=True)
    ophash = fields.CharField(51)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()

class Purchase(Model):
    nft_id = fields.BigIntField(pk=True)
    buyer = fields.CharField(36)