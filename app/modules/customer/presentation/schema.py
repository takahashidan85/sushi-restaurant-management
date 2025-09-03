from marshmallow import Schema, fields

class CustomerCreateSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)

class CustomerUpdateSchema(Schema):
    name = fields.Str(required=False)
    email = fields.Email(required=False)

class CustomerResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Email()
