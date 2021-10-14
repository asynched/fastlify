import sys
from logging.config import dictConfig as dict_config

DEFAULT_STARTUP_MESSAGE = """
███████╗ █████╗ ███████╗████████╗██╗     ██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔════╝╚══██╔══╝██║     ██║██╔════╝╚██╗ ██╔╝
█████╗  ███████║███████╗   ██║   ██║     ██║█████╗   ╚████╔╝ 
██╔══╝  ██╔══██║╚════██║   ██║   ██║     ██║██╔══╝    ╚██╔╝  
██║     ██║  ██║███████║   ██║   ███████╗██║██║        ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝        ╚═╝   
"""


def show_startup_message(statup_message: str, *args):
    print(statup_message)


def setup_server_startup(startup_message: str = DEFAULT_STARTUP_MESSAGE):
    cli = sys.modules['flask.cli']
    cli.show_server_banner = lambda *args: show_startup_message(startup_message, *args)

    dict_config(
        {
            'version': 1,
            'formatters': {
                'default': {
                    'format': '\u001b[44m\u001b[30m[%(asctime)s]\u001b[0m %(levelname)s: %(message)s',
                }
            },
            'handlers': {
                'wsgi': {
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://flask.logging.wsgi_errors_stream',
                    'formatter': 'default',
                }
            },
            'root': {
                'level': 'INFO',
                'handlers': ['wsgi'],
            },
        }
    )
