from Colors import colors
from dbk import dbk
colors.green("""
   _____ __        ____             __ __ _ __ 
  / ___// /_____ _/ / /_____  _____/ //_/(_) /_
  \__ \/ __/ __ `/ / //_/ _ \/ ___/ ,<  / / __/
 ___/ / /_/ /_/ / / ,< /  __/ /  / /| |/ / /_  
/____/\__/\__,_/_/_/|_|\___/_/  /_/ |_/_/\__/  
                                               
""")
value = input("\nSelect an Option:\n1)DatabaseKit\n2)NameLookup\n:")
if value == "1":
    dbk()
elif value == "2":
    nlk()
