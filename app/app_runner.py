import logging
import os
import uvicorn
from main import app

LOG = logging.getLogger(__name__)

HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', '80'))



if __name__ == "__main__":

    env_string = F"HOST={HOST}\nPORT={PORT}\n"

    logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s.%(msecs)03d|%(name)-12s|%(levelname)-8s| %(message)s',
                            datefmt='%m-%d %H:%M:%S')

    LOG.info(F"Environmnet Vars:\n{env_string}")

    uvicorn.run(app, host=HOST, port=PORT)
