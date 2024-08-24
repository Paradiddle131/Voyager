import os
from voyager import Voyager

voyager = Voyager(mc_port=os.environ.get("mc_port")
                  , server_port=os.environ.get("server_port")
                  )

# start lifelong learning
voyager.learn()