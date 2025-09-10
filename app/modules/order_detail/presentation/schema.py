from marshmallow import Schema, fields, validate

class OrderDetailCreateSchema(Schema):
    order_id = fields.Int(required=True)
    sushi_item_id = fields.Int(required=True)
    quantity = fields.Int(required=True, validate=validate.Range(min=1))

class OrderDetailUpdateSchema(Schema):
    sushi_item_id = fields.Int(required=False)
    order_id = fields.Int(required=False)
    quantity = fields.Int(validate=validate.Range(min=1))

class OrderDetailResponseSchema(Schema):
    id = fields.Int()
    order_id = fields.Int()
    sushi_item_id = fields.Int()
    quantity = fields.Int()
    unit_price = fields.Int()