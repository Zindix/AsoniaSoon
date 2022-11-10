import os
import sys
from pystyle import *
from getpass import getpass
from time import sleep, time

logo = r"""

██      ▄▄▄▄▄   ████▄    ▄   ▄█ ██   
█ █    █     ▀▄ █   █     █  ██ █ █  
█▄▄█ ▄  ▀▀▀▀▄   █   █ ██   █ ██ █▄▄█ 
█  █  ▀▄▄▄▄▀    ▀████ █ █  █ ▐█ █  █ 
   █                  █  █ █  ▐    █ 
  █                   █   ██      █  
 ▀                               ▀  
"""[:-1]

banner = """
         _                      _______                      _
      _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
     dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
     V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
              `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
               `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
          __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
        ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
     _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
                 `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
         ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
       ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
      ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
      MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
      YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
       `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
         `'                  `OObNNNNNdOO'                   `'
                               `~OOOOO~'"""[1:]

banner = Add.Add(logo, banner, center=True)

dark = Col.dark_gray
light = Col.light_gray
green = Colors.StaticMIX((Col.green, Col.blue))
bgreen = Colors.StaticMIX((Col.green, Col.blue, Col.blue))


def p(logo):
	# sleep(0.05)
	return print(stage(logo))

def stage(logo: str, symbol: str = '...', col1 = light, col2 = None) -> str:
	if col2 is None:
		col2 = light if symbol == '...' else green
	return f""" {Col.Symbol(symbol, col1, dark)} {col2}{logo}{Col.reset}"""

def main():
	os.system("Title Asonia")
	os.system("cls")
	Cursor.HideCursor()
	print()
	print(Colorate.Diagonal(Colors.DynamicMIX((green, dark)), Center.XCenter(banner)))
	print('\n')
	term = input(stage(f"Accepter vous les condition d'utilisation {dark}[{light}y{dark}/{light}n{dark}] -> {Col.reset}", "?", col2 = green)).replace('"','').replace("'","")
	print('\n')

	if term == 'Y':
		sleep(2)
		getpass(stage(f"Nous arrivons bientôt merci de repassé plus tard !{Col.reset}", "Asonia", col2 = green))

	if term == 'y':
		sleep(2)
		getpass(stage(f"Nous arrivons bientôt merci de repassé plus tard !{Col.reset}", "Asonia", col2 = green))

	if term == 'N':
		sleep(1)
		exit()

	if term == 'n':
		sleep(1)
		exit()

if __name__ == '__main__':
	main()