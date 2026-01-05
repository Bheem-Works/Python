# build the projects in the python
class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def home(self):
        self.name  = 'home'
        self.description = 'home'
    def car(self):
        self.name = 'car'
        self.description = 'car'

showTask = Task('show', 'show task')
showTask.home()
showTask.car()
