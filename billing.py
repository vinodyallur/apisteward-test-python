import demo_pay

p1 = demo_pay.PayClient()


def bill(amount):
    p3 = p1.customers.create(email="a@b.com")
    return p1.charges.create(
        p2=amount,
        currency="usd",
        source="tok_visa",
    )
