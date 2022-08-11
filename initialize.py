import json
import os
import sys


def initialize():
    if "config.json" in os.listdir():
        pass

    else:
        config = {
            "MPC_CODE": "L01"
        }
        with open("config.json", "w") as f:
            f.write(json.dumps(config, indent=4))

        if sys.platform == "darwin":
            # os.chmod("find_orb/find_orb", 755)
            os.chmod("find_orb/fo", 755)
            print("* Changed ./fo permission to 755")
