import os

class Config:
    def __init__(self, mode='hcd'):
        self.mode = mode
        self.model_path = os.path.join('models',mode + '.model')
        self.p_path = os.path.join('pickles', mode + '.p')

