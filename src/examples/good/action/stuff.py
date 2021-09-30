from examples.good.base.base_model import BaseModel


class Stuff:

    def __init__(self, model: BaseModel):
        self.model = model

    def do_stuff(self, data: int=0):
        data *= 2
        return self.model.predict(data=data)
