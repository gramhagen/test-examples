from examples.bad.base.model import Model


class Stuff:

    def __init__(self, path: str):
        self.model = Model(path=path)
    
    def do_stuff(self, data: int=0):
        data *= 2
        return self.model.predict(data=data)
