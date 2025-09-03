from marshmallow import Schema, fields, validate

class OrderCreateSchema(Schema):
    customer_id = fields.Int(required=True)
    order_type = fields.Str(
        required=True, 
        validate=validate.OneOf(["dine-in", "take_out", "delivery"])
    )

class OrderUpdateSchema(Schema):
    customer_id = fields.Int(required=False)

class OrderStatusUpdateSchema(Schema):
    new_status = fields.Str(
        required=True, 
        validate=validate.OneOf([
            "pending", "preparing", "ready", "served", 
            "delivering", "completed", "cancelled"
        ])
    )

class OrderResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int()
    order_type = fields.Str()
    status = fields.Str()