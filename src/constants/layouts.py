import chalk
from src.constants.package import package as pkg
from src.utils.functions import loop

banner = f"""
          &#BBB#&        
         #Y?PGGGPB       
         B?7JYJ5GG       
         BJ7?77JGG       
        #GPJJJYPBG&      
       G!^~!7J5BBBGGB&&B&
      B?^^~!~?5PYP5Y5P5G 
     &B7^^~!^7Y?JY7JPG#  
      &!~~!777!?~!?YP    
      P^~~777!P 57JP&    
    #?^^^^~!!#   &&      
   &5~^^^^?7^5           
  BPP5J!!YPP?7#          
  #GPPG55PPPPPP#          
  
  { pkg["name"] } { chalk.green("v" + pkg["version"]) }
  author : { pkg["author"] }
"""

barrier = chalk.yellow(loop("=", 15))