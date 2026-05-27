import colorama
from colorama import Fore, Style
from enum import StrEnum

class LOGOS(StrEnum):
    ASKEE_LOGO_TOILET = '''
    mm               mm
   ####              ##
   ####    mm#####m  ## m##"    m####m    m####m
  ##  ##   ##mmmm "  ##m##     ##mmmm##  ##mmmm##
  ######    """"##m  ##"##m    ##""""""  ##""""""
 m##  ##m  #mmmmm##  ##  "#m   "##mmmm#  "##mmmm#
 ""    ""   """"""   ""   """    """""     """""
 Anything,                             to anyone.
'''

    ASKEE_LOGO_FIRE = '''
Anything
          :::      ::::::::  :::    ::: :::::::::: ::::::::::
       :+: :+:   :+:    :+: :+:   :+:  :+:        :+:
     +:+   +:+  +:+        +:+  +:+   +:+        +:+
   +#++:++#++: +#++:++#++ +#++:++    +#++:++#   +#++:++#
  +#+     +#+        +#+ +#+  +#+   +#+        +#+
 #+#     #+# #+#    #+# #+#   #+#  #+#        #+#
###     ###  ########  ###    ### ########## ##########
                                              anywhere
'''

    ASKEE_LOGO_STICKS = '''
         o           o__ __o      o         o/   o__ __o__/_   o__ __o__/_
        <|>         /v     v\    <|>       /v   <|    v       <|    v
        / \        />       <\   / >      />    < >           < >
      o/   \o     _\o____        \o__ __o/       |             |
     <|__ __|>         \_\__o__   |__ __|        o__/_         o__/_
     /       \               \    |      \       |             |
   o/         \o   \         /   <o>      \o    <o>           <o>
  /v           v\   o       o     |        v\    |             |
 />             <\  <\__ __/>    / \        <\  / \  _\o__/_  / \  _\o__/_
     anything                                         anytime
'''

    ASKEE_LOGO_MONEY = '''
                 something
  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$$
 /$$__  $$ /$$__  $$| $$  /$$/| $$_____/| $$_____/
| $$  \ $$| $$  \__/| $$ /$$/ | $$      | $$
| $$$$$$$$|  $$$$$$ | $$$$$/  | $$$$$   | $$$$$
| $$__  $$ \____  $$| $$  $$  | $$__/   | $$__/
| $$  | $$ /$$  \ $$| $$\  $$ | $$      | $$
| $$  | $$|  $$$$$$/| $$ \  $$| $$$$$$$$| $$$$$$$$
|__/  |__/ \______/ |__/  \__/|________/|________/
                 whatever

'''

    ASKEE_LOGO_MINIMAL = '''
            _____ _  ________ ______
     /\    / ____| |/ /  ____|  ____|
    /  \  | (___ | ' /| |__  | |__
   / /\ \  \___ \|  < |  __| |  __|
  / ____ \ ____) | . \| |____| |____
 /_/    \_\_____/|_|\_\______|______|
                askee.
'''

    ASKEE_LOGO_BLUR = '''
            aaa nnn yyy ttt hhh iii nnn ggg
 ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓████████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░
            ttt ooo aaa nnn yyy ooo nnn eee
'''

    def next(self):
            members = list(LOGOS)
            next_index = (members.index(self) + 1) % len(members)
            return members[next_index]

    def previous(self):
        members = list(LOGOS)
        next_index = (members.index(self) - 1) % len(members)
        return members[next_index]

class COLORS(StrEnum):
    RED = Fore.RED
    GREEN = Fore.GREEN
    PURPLE = Fore.MAGENTA
    WHITE = Fore.WHITE
    BLUE = Fore.BLUE
    BLACK = Fore.BLACK
    CYAN = Fore.CYAN
    YELLOW = Fore.YELLOW

    def next(self):
            members = list(COLORS)
            next_index = (members.index(self) + 1) % len(members)
            return members[next_index]

    def previous(self):
        members = list(COLORS)
        next_index = (members.index(self) - 1) % len(members)
        return members[next_index]

class ERRORS(StrEnum):
    DEFAULT = '''

!     ______    ______    ______    ______    ______     !
!    /      \  /      \  /      \  /      \  /      \    !
!   |  $$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\   !
!   | $$    $$| $$   \$$| $$   \$$| $$  | $$| $$   \$$   !
!   | $$$$$$$$| $$      | $$      | $$__/ $$| $$         !
!    \$$     \| $$      | $$       \$$    $$| $$         !
!     \$$$$$$$ \$$       \$$        \$$$$$$  \$$         !
!                                                        !
!
    '''