from datetime import datetime
from time import strftime
import os
class Logger():

    def __init__(self, filePathDir):

        if not os.path.isdir(filePathDir):
            os.mkdir(filePathDir)
        string = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.fileName = f"log_{string}.log"
        self.file = open(f"{filePathDir}{self.fileName}",'a')


    def write(self, txt):
        self.file.write(f"{datetime.now()}T- {str(txt)}")
        self.file.flush()
