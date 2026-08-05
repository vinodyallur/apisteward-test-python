import demo_pay

client = demo_pay.PayClient()


def bill(amount):
    customer = client.customers.create(email="a@b.com")
    return client.charges.create(
        amount=amount,
        currency="usd",
        source="tok_visa",
    )
