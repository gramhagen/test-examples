from time import sleep
from examples.better.base.base_model import BaseModel


class Model(BaseModel):
    def __init__(self, path: str):
        self.path = path
        # loading model
        sleep(10)
    
    def predict(self, data: int=0):
        return True if data > 0 else False
