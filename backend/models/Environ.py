from decouple import config


class Environ:
    """environment variables"""

    # Stripe Key
    STRIPE_KEY = config("STRIPE_KEY")
    # Mongo Connection String
    MONGO_CON = config("MONGO_CON")
