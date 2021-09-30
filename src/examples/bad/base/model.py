from time import sleep


class Model:
    def __init__(self, path: str):
        self.path = path
        # loading model
        sleep(10)
    
    def predict(self, data: int=0):
        return True if data > 0 else False
