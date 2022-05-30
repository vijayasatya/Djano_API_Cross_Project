import time
import subprocess
import os
cmd = "bash reload_web.sh"
returned_value = os.system(cmd)
def restart_server():
    while 1:
        returned_value = os.system(cmd)
        print("server restarted")
        break
        time.sleep(30)
#runserver()
