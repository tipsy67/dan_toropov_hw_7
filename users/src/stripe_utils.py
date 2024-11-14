from itertools import product

import stripe

from config.settings import SECRET_STRIPE_KEY
from lws.models import Course, Lesson

stripe.api_key = SECRET_STRIPE_KEY


def get_stripe_id(obj):
    stripe_id = ""
    if type(obj) == Course:
        stripe_id = "hw7_course_"
    elif type(obj) == Lesson:
        stripe_id = "hw7_lesson_"

    stripe_id += str(obj.pk)

    return stripe_id


def get_product_from_stripe(obj: Course | Lesson):
    stripe_id = get_stripe_id(obj)
    product = stripe.Product.search(query=f"name:'{obj.name}'")
    if not len(product.data):
        product = stripe.Product.create(name=f"{obj.name}", id=stripe_id)
    else:
        product = product.get("data")[0]

    return product


def create_price_on_stripe(obj: Course | Lesson):
    product = get_product_from_stripe(obj)
    return stripe.Price.create(
        currency="usd",
        unit_amount=obj.price * 100,
        product=product.get("id"),
    )


def create_link_for_pay(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )

    return session.get("id"), session.get("url")


def get_status_payment(session_id):
    return stripe.checkout.Session.retrieve(
        session_id,
    ).get("payment_status")
