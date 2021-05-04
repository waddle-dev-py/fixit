import os
from pathlib import Path

import quickfix as fix
from dotenv import load_dotenv

from fixit.application import Application

_ = load_dotenv()


def main(path):

    try:
        settings = fix.SessionSettings(path.name)
        application = Application(
            username=os.environ['FIX_USERNAME'],
            password=os.environ['FIX_PASSWORD'],
            sender_sub_id=os.environ['FIX_SENDER_SUB_ID']
        )
        store_factory = fix.FileStoreFactory(settings)
        log_factory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, store_factory, settings, log_factory)
        initiator.start()
        application.run()
        # time.sleep(5)
        initiator.stop()
    except fix.ConfigError as e:
        print(e)


if __name__ == '__main__':
    main(path=Path('settings.cfg'))
