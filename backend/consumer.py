from models.Environ import Environ
from models.BasicMessageReciever import BasicMessageReceiver

if __name__ == "__main__":
    basic_message_receiver = BasicMessageReceiver(
            Environ.BROKER_ID,
            Environ.BROKER_USERNAME,
            Environ.BROKER_PASSWORD,
            Environ.BROKER_REGION,
    )

    basic_message_receiver.declare_queue(Environ.BROKER_QUEUE)

    basic_message_receiver.consume_messages(Environ.BROKER_QUEUE)
    basic_message_receiver.close()