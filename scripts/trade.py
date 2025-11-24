class Trade:
    def __init__(
        self, item_name, trade_type, quantity, price_per_unit, date, time, owner_id
    ):
        self.item_name = item_name
        self.trade_type = trade_type
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.date = date
        self.time = time
        self.owner_id = owner_id

    def to_dict(self):
        return {
            "item_name": self.item_name,
            "trade_type": self.trade_type,
            "quantity": self.quantity,
            "price_per_unit": self.price_per_unit,
            "date": self.date,
            "time": self.time,
            "owner_id": self.owner_id,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["item_name"],
            data["trade_type"],
            data["quantity"],
            data["price_per_unit"],
            data["date"],
            data["time"],
            data["owner_id"],
        )
