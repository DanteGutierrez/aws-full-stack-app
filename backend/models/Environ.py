from decouple import config


class Environ:
    """environment variables"""

    # Stripe Key
    STRIPE_KEY = config("STRIPE_KEY")
    # Mongo Connection String
    MONGO_CON = config("MONGO_CON")
    MAIL_FROM=config("MAIL_FROM")
    MAIL_PASSWORD=config("MAIL_PASSWORD")
    BROKER_QUEUE=config("BROKER_QUEUE")
    BROKER_ID=config("BROKER_ID")
    BROKER_USERNAME=config("BROKER_USERNAME")
    BROKER_PASSWORD=config("BROKER_PASSWORD")
    BROKER_REGION=config("BROKER_REGION")