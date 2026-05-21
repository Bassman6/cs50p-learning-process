import random
import sys
from pyfiglet import Figlet


figlet = Figlet()


#random.choice()

if len(sys.argv) == 1:
    userinput = input('stronly:')
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(userinput))

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f","--font"]:
        sys.exit("illegal input")

    else:
      try:
        user_input = input("input:")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(user_input))

      except ValueError:
        pass

     
else:
    sys.exit("Invalid usage")


