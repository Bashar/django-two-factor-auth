from nexmo import send_message
import logging

logger = logging.getLogger(__name__)


class Fake(object):
    """
    Prints the tokens to the logger. You will have to set the message level of
    the ``two_factor`` logger to ``INFO`` for them to appear in the console.
    Useful for local development. You should configure your logging like this::

        LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                },
            },
            'loggers': {
                'two_factor': {
                    'handlers': ['console'],
                    'level': 'INFO',
                }
            }
        }
    keeping this for future voice integration with Nexmo
    @staticmethod
    def make_call(device, token):
        logger.info('Fake call to %s: "Your token is: %s"', device.number, token)
    """


    @staticmethod
    def send_sms(device, token):
        send_message(device.number,'Your token is: %s' % token)
