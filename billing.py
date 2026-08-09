import demo_pay

c1 = demo_pay.PayClient()


def bill(amount):
    c3 = c1.customers.create(email="a@b.com")
    return c1.charges.create(
        c2=amount,
        currency="usd",
        source="tok_visa",
    )
