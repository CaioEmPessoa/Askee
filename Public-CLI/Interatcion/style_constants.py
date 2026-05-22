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
                                              to anyone.
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