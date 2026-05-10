import threading
from queue import Queue
import time


class ThreadBot(threading.Thread):
    def __init__(self, name, queue):
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, foprks=0)
        self.tasks = Queue()


    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == "prepare table":
                kitchen.give(to=self.cutlery, knives=4, forks=4)

            elif task == "clear table":
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == "shutdown":
                return
            

    
            



    