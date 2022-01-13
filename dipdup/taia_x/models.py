from tortoise import Model, fields
from datetime import datetime
from enum import Enum, IntEnum

class EventType(str, Enum):
    unspecified = 'unspecified'
    mint = 'mint'
    transfer = 'transfer'
    purchase = 'purchase'

class Holder(Model):
    address = fields.CharField(36, pk=True)
    name = fields.TextField(default='')
    description = fields.TextField(default='')
    metadata_file = fields.TextField(default='')
    metadata = fields.JSONField(default={})
    #hdao_balance = fields.BigIntField(default=0)
    #is_split = fields.BooleanField(default=False)

class Token(Model):
    id = fields.BigIntField(pk=True)
    creator = fields.ForeignKeyField('models.Holder', 'tokens', index=True, null=True)
    name = fields.TextField(default='')
    description = fields.TextField(default='')
    artifact_uri = fields.TextField(default='')
    metadata = fields.TextField(default='')
    timestamp = fields.DatetimeField(default=datetime.utcnow())
    #thumbnail_uri = fields.TextField(default='')
    #display_uri = fields.TextField(default='')
    #extra = fields.JSONField(default={})
    #mime = fields.TextField(default='')
    #royalties = fields.SmallIntField(default=0)
    #supply = fields.SmallIntField(default=0)
    #hdao_balance = fields.BigIntField(default=0)
    #is_signed = fields.BooleanField(default=False)
    #level = fields.BigIntField(default=0)

class TokenOperator(Model):
    token = fields.ForeignKeyField('models.Token', 'operators', null=False, index=True)
    owner = fields.ForeignKeyField('models.Holder', 'owner', index=True)
    operator = fields.CharField(36)

    class Meta:
        table = 'token_operator'

class TokenHolder(Model):
    holder = fields.ForeignKeyField('models.Holder', 'holders_token', null=False, index=True)
    token = fields.ForeignKeyField('models.Token', 'token_holders', null=False, index=True)
    #quantity = fields.BigIntField(default=0)
    #trades_count = fields.BigIntField(default=0)
    #trades_volume = fields.DecimalField(decimal_places=6, max_digits=32, default=0)

    class Meta:
        table = 'token_holder'

class Event(Model):
    id = fields.BigIntField(pk=True)
    token = fields.ForeignKeyField('models.Token', 'mints', null=True, index=True)
    creator = fields.ForeignKeyField('models.Holder', 'sales', null=True, index=True)
    recipient = fields.ForeignKeyField('models.Holder', 'purchases', null=True, index=True)
    amount = fields.BigIntField()
    event_type = fields.CharEnumField(EventType, default=EventType.unspecified)
    price = fields.BigIntField(null=True)
    ophash = fields.CharField(51)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()