'''
    Tool to pass the time on stream.
    Copyright (C) 2022  theMinesAreShakin

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''


import random

from chatter import Chatter

class FunFactFred(Chatter):

    def __init__(self):
        super().__init__("Fred")
        self.futureDialogList = [
            "Antarctica is the only continent without any reptiles or snakes",
            "'Dreamt' is the only English word that ends in the letters 'mt'",
            "Maine is the only state that has a one-syllable name",
            "In many advertisements, the time displayed on a watch is 10:10",
            "A dime has 118 ridges around the edge",
            "Most people fall asleep in seven minutes",
            "The scientific term for brain freeze is 'sphenopalatine ganglioneuralgia'",
            "The Apology Act is a law in the province of Ontario that provides apologies\nmade by a person does not necessarily constitute an admission of guilt",
            "The only letter that doesn’t appear on the periodic table is J",
            "A single strand of Spaghetti is called a 'Spaghetto'",
            "Forrest Fenn, an art dealer, and author hid a treasure chest in the Rocky\nMountains worth over 1 million dollars. It still has not been found."
        ]
        random.shuffle(self.futureDialogList)
        self.dialog_cooldown = 0
        self.reset_dialog_cooldown()


    def update(self):
        self.dialog_cooldown -= 1
        next_dialog = self.get_next_dialog()
        if next_dialog != "":
            self.queue_dialog(next_dialog)

    
    def get_next_dialog(self):
        if self.dialog_cooldown != 0:
            return ""
        try:
            self.reset_dialog_cooldown()
            return self.futureDialogList.pop(0)
        except IndexError:
            # when out of dialog
            self.dialog_cooldown = -1
            return ""


    def reset_dialog_cooldown(self):
        self.dialog_cooldown = random.randrange(50, 121)