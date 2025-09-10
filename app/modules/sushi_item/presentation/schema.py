from marshmallow import Schema, fields, validate

class SushiItemCreateSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Int(required=True, validate=validate.Range(min=0))
    category = fields.Str(load_default=None)
    description = fields.Str(load_default=None)

class SushiItemUpdateSchema(Schema):
    name = fields.Str(load_default=None)
    price = fields.Int(validate=validate.Range(min=0), load_default=None)
    category = fields.Str(load_default=None)
    description = fields.Str(load_default=None)

class SushiItemResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    price = fields.Int()
    category = fields.Str(allow_none=True)
    description = fields.Str(allow_none=True)
