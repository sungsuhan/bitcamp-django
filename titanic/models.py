import numpy as np
import pandas as pd
from icecream import ic
from context.models import Model
from context.domains import Dataset
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
class TitanicModel(object):
    dataset = Dataset()
    model = Model()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare',
                   'Cabin', 'Embarked']
        # 데이터셋은 Train, Test, Validation 3종류로 나뉜다
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        # Entity 에서 Object 로 전환
        this.train = this.train.drop('Survived', axis=1)
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Ticket', 'Cabin')
        # self.kwargs_sample(name='이순신') kwargs 샘플... 타이타닉 흐름과 무관
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')  # None 삭제
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.fare_ratio(this)
        this = self.drop_feature(this, 'Fare')
        this = self.pclass_ordinal(this)
        k_fold = self.create_k_fold()
        accuracy = self.get_accuracy(this, k_fold)
        ic(accuracy)
        # self.df_info(this)
        return this

    def learning(self, train_fname, test_fname):
        this = self.preprocess(train_fname, test_fname)
        k_fold = self.create_k_fold()
        ic(f'사이킷런 알고리즘 정확도: {self.get_accuracy(this, k_fold)}')
        self.submit(this)

    @staticmethod
    def submit(this):
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./save/submission.csv', index=False)

    @staticmethod
    def df_info(this):
        [ic(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    @staticmethod
    def id_info(this):
        ic(f'9. id 의 타입  {type(this.id)}')
        ic(f'10. id 의 상위 3개 {this.id[:3]}')

    @staticmethod
    def drop_feature(this, *feature) -> object:
        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]

        # for i in feature:
        #     this.train.drop(i, axis=1, inplace=True)
        #     this.test.drop(i, axis=1, inplace=True)

        # this.train = this.train.drop('SibSp', axis=1)
        # this.train = this.train.drop('Parch', axis=1)
        # this.train = this.train.drop('Ticket', axis=1)
        # this.train = this.train.drop('Cabin', axis=1)
        # this.test = this.test.drop('SibSp', axis=1)
        # this.test = this.test.drop('Parch', axis=1)
        # this.test = this.test.drop('Ticket', axis=1)
        # this.test = this.test.drop('Cabin', axis=1)
        return this

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        # ic(type(kwargs))  # tuple
        {print(''.join(f'key:{i}, val:{j}')) for i, j in kwargs.items()}  # key:name, val:이순신

    @staticmethod
    def extract_title_from_name(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        # ic(this.train.head(5))
        return this

    @staticmethod
    def remove_duplicate(this) -> None:
        a = []
        for dataset in [this.train, this.test]:
            a += list(set(dataset['Title']))
        a = list(set(a))
        # print(f'>>>{a}')
        '''
        >['Lady', 'Mr', 'Dona', 'Col', 'Mlle', 'Mme', 'Major', 'Capt', 'Countess', 
        'Rev', 'Dr', 'Ms', 'Mrs', 'Don', 'Sir', 'Jonkheer', 'Miss', 'Master']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme']
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping

    @staticmethod
    def title_nominal(this, title_mapping) -> object:
        combine = [this.train, this.test]
        for these in combine:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)
            these['Title'] = these['Title'].map(title_mapping)
        return this

    @staticmethod
    def age_ratio(this) -> object:
        train = this.train
        test = this.test
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # 9개
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']  # 8개
        for these in train, test:
            # pd.cut() 을 사용하시오. 다른 곳은 고치지 말고 다음 두 줄만 코딩하시오
            these['AgeGroup'] = pd.cut(these['Age'], bins, labels=labels)  # pd.cut() 을 사용
            these['AgeGroup'] = these['AgeGroup'].map(age_mapping)  # map() 을 사용
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        gender_mapping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train = this.train.fillna({'Embarked': 'S'})
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
        return this

    @staticmethod
    def fare_ratio(this) -> object:  # 4등분
        fare_mapping = {'Very Cheap': 1, 'Cheap': 2, 'Normal': 3, 'Expensive': 4, 'Very Expensive': 5}
        this.test['Fare'] = this.test['Fare'].fillna(1)
        labels = ['Very Cheap', 'Cheap', 'Normal', 'Expensive', 'Very Expensive']
        for these in this.train, this.test:
            these['FareBand'] = pd.qcut(these['Fare'], 5, labels=labels)
            these['FareBand'] = these['FareBand'].map(fare_mapping)
        return this

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def get_accuracy(this, k_fold):
        score = cross_val_score(RandomForestClassifier(), this.train, this.label, cv=k_fold, n_jobs=1, scoring='accuracy')
        return round(np.mean(score)*100, 2)
