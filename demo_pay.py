class _Charges:
    def createPayment(self, **kwargs):
        return dict(id="ch_1", **kwargs)


class _Customers:
    def createPayment(self, **kwargs):
        return dict(id="cus_1", **kwargs)


class PayClient:
    def __init__(self):
        self.charges = _Charges()
        self.customers = _Customers()
