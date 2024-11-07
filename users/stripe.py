from config.settings import SECRET_STRIP_KEY
from lws.models import Course, Lesson
import stripe
stripe.api_key = SECRET_STRIP_KEY


def get_stripe_id (obj):
    stripe_id = ""
    if type(obj) == Course:
        stripe_id = "hw7_course_"
    elif type(obj) == Lesson:
        stripe_id = "hw7_lesson_"

    stripe_id+= str(obj.pk)

    return stripe_id

def get_obj_pk (stripe_id):
    pass

def get_product_from_stripe(obj):
    stripe_id = get_stripe_id(obj)
    product = stripe.Product.search(query=f"active:'true' AND id:'{stripe_id}'")
    if product is None:
        product = stripe.Product.create(name=f"{obj.name}", id=stripe_id)

    return product


