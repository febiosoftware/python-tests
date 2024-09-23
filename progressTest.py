# @fbs {
#  "name" : "progress",
#  "info" : "Watch a progress bar"
# }
from fbs import ui, args
import time

for i in range(100):
    ui.setProgress(i)
    time.sleep(0.05)
