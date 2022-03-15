# context, fname, train, test, id, lable
from dataclasses import dataclass

@dataclass
class Dataset:
    context : str
    dname : str
    sname : str
    fname : str
    train : str
    test : str
    id : str
    lable : str

    @property
    def context(self) -> str: return self._context
    @context.setter
    def context(self, context): self._context = context

    @property
    def dname(self) -> str: return self._dname
    @dname.setter
    def dname(self, dname): self._dname = dname

    @property
    def sname(self) -> str: return self._sname
    @sname.setter
    def sname(self, sname): self._sname = sname

    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train
    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test
    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id
    @id.setter
    def id(self, id): self._id = id

    @property
    def lable(self) -> str: return self._lable
    @lable.setter
    def lable(self, lable): self._lable = lable
