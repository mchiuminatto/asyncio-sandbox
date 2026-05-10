"""
Threading model example with bots managing tables in a restaurant. Each bot can prepare and clear tables by taking and returning cutlery from the kitchen. The bots run in separate threads and communicate through a shared queue of tasks. The kitchen starts with a certain number of knives and forks, and the bots manage their own cutlery inventory as they perform their tasks.
"""

import threading
from queue import Queue
from attr import attrs, attrib
import time


class ThreadBot(threading.Thread): # 1
    def __init__(self, name, queue):
        super().__init__(target=self.manage_table) # 2
        self.cutlery = Cutlery(knives=0, foprks=0) # 3
        self.tasks = Queue()  # 4


    def manage_table(self):
        while True: # 5
            task = self.tasks.get()
            if task == "prepare table":
                kitchen.give(to=self.cutlery, knives=4, forks=4) # 6

            elif task == "clear table":
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == "shutdown":
                return
            

    
    @attrs
    class Cutlery:
        knives = attrib(default=0)
        forks = attrib(default=0)

        def give(self, to: "Cutlery", knives=0, forks=0):
            self.change(-knives, -forks)
            to.change(knives, forks)

        def change(self, knives, forks):
            self.knives += knives
            self.forks += forks


    kitchen = Cutlery(knives=100, forks=100)
    bots = [ThreadBot() for i in range (10)]

    



    