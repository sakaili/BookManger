import pymysql


def Getdb():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='515310szc', db="library",
                         charset="utf8")

    return db


class Book(object):
    def __init__(self, number, name, author, status, amount):
        self.number = number
        self.name = name
        self.author = author
        self.status = status
        self.amount = amount


class IdChoice(object):
    def __init__(self):
        self.cursor = Getdb().cursor()
        self.Choice()

    def Choice(self):
        """
        选择身份并跳转到相对应的验证函数
        """
        print('欢迎使用图书管理系统')
        print('请选择你的身份：\n[1]学生\n[2]管理员\n')
        ans = input()
        if ans == '1':
            self.StudentIdentity()
        elif ans == '2':
            self.ManagerIdentity()
        else:
            print('输入错误，请重新输入！')

    def ManagerIdentity(self):
        account = input('请输入您的帐号')
        password = input('请输入您的密码')
        sql = "SELECT * FROM account WHERE ID='%s'" % account
        self.cursor.execute(sql)
        results = self.cursor.fetchone()
        if bool(results) != 1:
            print('您输入的账户不存在')
        if account == results[0] and password == results[1]:
            Menu.AdminMenu()
        """
        管理员身份验证
        :return:
        """

    def StudentIdentity(self):
        account = input('请输入您的帐号')
        password = input('请输入您的密码')
        sql = "SELECT * FROM account WHERE ID='%s'" % account
        self.cursor.execute(sql)
        results = self.cursor.fetchone()
        if bool(results) != 1:
            print('您输入的账户不存在')
        if account == results[0] and password == results[1]:
            Menu.StudentMenu()
        """
        学生身份验证
        :return:
        """


class Menu(object):
    @staticmethod
    def AdminMenu():
        print('\n欢迎登录图书馆管理员系统!')
        print('[1]学生信息录入')
        print('[2]学生信息修改')
        print('[3]学生信息删除')
        print('[4]图书信息录入')
        print('[5]图书信息修改')
        print('[6]图书信息删除')
        print('[0]退出')
        while 1:
            AdminChoice = input('请选择您要进行的操作')
            if AdminChoice == '1':
                Manage.StudentIn()
            if AdminChoice == '2':
                Manage.StudentChange()
            if AdminChoice == '3':
                Manage.StudentDelete()
            if AdminChoice == '4':
                pass
            if AdminChoice == '5':
                pass
            if AdminChoice == '6':
                pass
            if AdminChoice == '0':
                break

    @staticmethod
    def StudentMenu():
        print('\n欢迎登录图书馆系统!')
        print('[1]借书')
        print('[2]还书')
        print('[0]退出')
        while 1:
            StudentChoice = input('请选择您要进行的操作')
            if StudentChoice == '1':
                pass
            if StudentChoice == '2':
                pass
            if StudentChoice == '3':
                pass


class Manage(object):
    @staticmethod
    def StudentIn():
        db = Getdb()
        StudentId = input('请输入要新增的学生学号')
        StudentPassword = input('请输入要新增的学生密码')
        sql = "INSERT INTO account VALUES('{0}','{1}')".format(StudentId, StudentPassword)
        try:
            db.cursor().execute(sql)
            db.commit()
        except:
            db.rollback()
            db.close()
            print('插入失败')
        finally:
            print('插入成功')

    @staticmethod
    def StudentChange():
        db = Getdb()
        StudentId = input('请输入要修改的学生学号')
        StudentPassword = input('请输入要修改的学生密码')
        sql = "UPDATE account SET PASSWORD='{0}' WHERE ID='{1}'".format(StudentPassword, StudentId)
        try:
            db.cursor().execute(sql)
            db.commit()
        except:
            db.rollback()
            db.close()
            print('修改失败')
        finally:
            print('修改成功')

    @staticmethod
    def StudentDelete():
        db = Getdb()
        StudentId = input('请输入要删除的学生学号')
        AdminPassword = input('请输入管理员密码')
        sql0 = "DELETE FROM account WHERE ID='{0}'".format(StudentId)
        sql1 = "SELECT * FROM account WHERE ID='%s'" % 'admin'
        db.cursor().execute(sql1)
        result = db.cursor().fetchone()
        print(result)
        if result[1] == AdminPassword:
            db.cursor.execute(sql0)
            db.commit()
            print('删除成功')
            db.rollback()
            db.close()


if __name__ == '__main__':
    # book1 = Book(1, '海底两万里', 'author', '有存书', 50)

    IdChoice()
