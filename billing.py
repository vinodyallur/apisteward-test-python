import demo_pay

client = demo_pay.PayClient()


def bill(amount):
    customer = client.customers.createPayment(email="a@b.com")
    return client.charges.createPayment(
        amount=amount,
        currency="usd",
        source="tok_visa",
    )
