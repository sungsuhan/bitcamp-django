from icecream import ic
from context.models import Model
from context.domains import Dataset
class TitanicModel(object):
    dataset = Dataset()
    model = Model()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        # 데이터셋은 Train, Test, Validation 3종류로 나뉜다
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Ticket', 'Cabin')

        # Entity 에서 Object 로 전환
        '''
        this = self.create_train(this)
        this = self.create_label(this)
        this = self.name_nominal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        '''
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        ic(f'1.Train 의 타입 : {type(this.train)}\n')
        ic(f'2.Train 의 컬럼 : {this.train.columns}\n')
        ic(f'3.Train 의 상위 1개 : {this.train.head(1)}\n')
        ic(f'4.Train 의 null의 개수 : {this.train.isnull().sum()}\n')
        ic(f'5.Test 의 타입 : {type(this.test)}\n')
        ic(f'6.Test 의 컬럼 : {this.test.columns}\n')
        ic(f'7.Test 의 상위 1개 : {this.test.head(1)}\n')
        ic(f'8.Test 의 null의 개수 : {this.test.isnull().sum()}\n')
        ic(f'9.id의 타입 : {type(this.id)}\n')
        ic(f'9.id의 상위 3개 : {this.id[:3]}\n')
        print('*'*100)

    @staticmethod
    def drop_feature(this, *feature) -> object:
        this.train = this.train.drop([i for i in feature], axis=1)
        this.test = this.test.drop([i for i in feature], axis=1)

        #this.train = this.train.drop('SibSp', axis=1)
        #this.train = this.train.drop('Parch', axis=1)
        #this.train = this.train.drop('Ticket', axis=1)
        #this.train = this.train.drop('Cabin', axis=1)

        #this.test = this.test.drop('SibSp', axis=1)
        #this.test = this.test.drop('Parch', axis=1)
        #this.test = this.test.drop('Ticket', axis=1)
        #this.test = this.test.drop('Cabin', axis=1)

        '''
        self.sibsp_garbage(df)
        self.parch_garbage(df)
        self.ticket_garbage(df)
        self.cabin_garbage(df)
        '''

        return this

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this

