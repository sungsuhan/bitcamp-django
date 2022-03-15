from icecream import ic
from context.domains import Dataset
from context.models import Model
from titanic.models import TitanicModel


class TitanicTemplate(object):
    def __init__(self):
        self.model = Model()
        self.dataset = Dataset()

        self.a = TitanicModel(train_fname='train.csv', test_fname='test.csv')

