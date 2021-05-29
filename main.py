import pymysql

class Book(object):
    def __init__(self,number,name,author,status,amount):
        self.number = number
        self.name = name
        self.author = author
        self.status = status
        self.amount = amount

class BookManage(object):
    def

if __name__ == '__main__':
    book1 = Book('海底两万里','author','有存书',50)
    print(book1)
