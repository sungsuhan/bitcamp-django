# https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.templates import TitanicTemplate
from titanic.models import TitanicModel
from titanic.views import TitanicView

if __name__ == '__main__':
    view = TitanicView()

    while 1:
        menu = input('1.템플릿 2.전처리')
        if menu == '1':
            print(' ### 1.템플릿 ### ')
            template = TitanicTemplate(train_fname='train.csv')
        elif menu == '2':
            print(' ### 2.전처리 ###')
            model = TitanicModel(train_fname='train.csv', test_fname='test.csv')
        else:
            break
