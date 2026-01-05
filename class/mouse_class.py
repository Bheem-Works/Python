
# class inheritance mouse projects 

class Computer:
    def __init__(self,device):
        self.device = device
        self.mouse = self.Mouse(self)

    class Mouse:
        def __init__(self,computer):
            self.status = 'off' 
            self.computer = computer
        def start(self):
            self.status = 'running'
            print('your mouse is now on')
        def rightClick(self):
            self.status = 'running'
            print('click the element')
        def leftClick(self):
            self.status = 'running'
            print('show the descriptions')
        def scroll(self):
            self.status = 'running'
            print('you can scroll to the up and down')
        def stop(self):
            self.status = 'off'
            print('your mouuse is stop responding')
        def display(self):
            if self.status == 'running' :
                print(f"Mouse {self.computer.device}")
            else:
                print('plug in the mouse')

run = Computer('mouse')
run.mouse.start()
run.mouse.rightClick()



