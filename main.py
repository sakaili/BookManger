import pymysql


def GetCursor():
    """
    建立与MySQL数据库连接
    connect内的参数依自己情况填写
    :return: db cursor
    """
    db = pymysql.connect(host='localhost', port=3306, user='root', password='515310szc', db="library",
                         charset="utf8")
    cursor = db.cursor()
    return db, cursor


class Book(object):
    """
    定义图书类
    """
    def __init__(self, number, name, author, status, amount):
        self.number = number
        self.name = name
        self.author = author
        self.status = status
        self.amount = amount


class IdChoice(object):
    """
    选择身份类
    """
    def __init__(self):
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
            return 0

    def ManagerIdentity(self):
        """
        管理员身份验证，与数据库通讯验证是否输入正确。
        :return:
        """
        db, cursor = GetCursor()
        account = input('请输入您的帐号')
        password = input('请输入您的密码')
        sql = "SELECT * FROM account WHERE ID='%s'" % account
        cursor.execute(sql)
        results = cursor.fetchone()
        if bool(results) != 1:
            print('您输入的账户不存在')
            return 0
        if account == results[0] and password == results[1]:
            db.close()
            Menu.AdminMenu()

    def StudentIdentity(self):
        """
        验证学生身份
        :return:
        """
        db, cursor = GetCursor()
        account = input('请输入您的帐号')
        password = input('请输入您的密码')
        sql = "SELECT * FROM account WHERE ID='%s'" % account
        cursor.execute(sql)
        results = cursor.fetchone()
        if bool(results) != 1:
            print('您输入的账户不存在')
        if account == results[0] and password == results[1]:
            Menu.StudentMenu()
            db.close()
        """
        学生身份验证
        :return:
        """


class Menu(object):
    """
    菜单类，选择功能
    """
    @staticmethod
    def AdminMenu():
        print('\n欢迎登录图书馆管理员系统!')
        print('[1]学生信息录入')
        print('[2]学生信息修改')
        print('[3]学生信息删除')
        print('[4]图书信息录入')
        print('[5]图书信息修改')
        print('[6]图书信息删除')
        print('[7]借阅情况查询')
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
                Manage.BookIn()
            if AdminChoice == '5':
                Manage.BookChange()
            if AdminChoice == '6':
                Manage.BookDelete()
            if AdminChoice == '7':
                Manage.SearchInfo()
            if AdminChoice == '0':
                print('退出成功！')
                break

    @staticmethod
    def StudentMenu():
        """
        学生菜单
        :return:
        """
        print('\n欢迎登录图书馆系统!')
        print('[1]借书')
        print('[2]还书')
        print('[0]退出')
        while 1:
            StudentChoice = input('请选择您要进行的操作')
            if StudentChoice == '1':
                Manage.BorrowBook()
            if StudentChoice == '2':
                Manage.ReturnBook()
            if StudentChoice == '0':
                print('退出成功')
                break


class Manage(object):
    """
    功能类，实现管理员和学生相应的功能
    """
    @staticmethod
    def BorrowBook():
        db, cursor = GetCursor()
        BorrowName = input('请输入您要借的书名')
        if isinstance(BorrowName, str):
            sql0 = "SELECT * FROM Book WHERE BookName='%s'" % BorrowName
            cursor.execute(sql0)
            result = cursor.fetchone()
            if result[4] > 0:
                print(result)
                ans = input("你确定要借阅'%s'么？(输入你的学号以确认)" % result[1])
                sql1 = "UPDATE Book SET BookAmount='{0}' WHERE BookName='{1}'".format(result[4] - 1, result[1])
                sql2 = "INSERT INTO Log VALUES(0,'{0}','{1}','借出')".format(ans, result[1])
                try:
                    cursor.execute(sql1)
                    db.commit()
                    print('借阅成功')
                    cursor.execute(sql2)
                    db.commit()
                    print('登记成功')
                except:
                    db.rollback()
                    db.close()
                    print('借阅失败')
                finally:
                    return
            elif result[4] == 0:
                print('已无存书')
                return
            else:
                print('未查询到相关书目')
                return
        else:
            print('输入非法！')
            return

    @staticmethod
    def ReturnBook():
        db, cursor = GetCursor()
        ReturnBook = input('请输入您要归还的图书名')
        sql0 = "SELECT * FROM Book WHERE BookName='%s'" % ReturnBook
        cursor.execute(sql0)
        result = cursor.fetchone()
        if isinstance(ReturnBook, str):
            ans = input("你确定要归还'%s'么？(输入你的学号以确认)" % result[1])
            sql1 = "UPDATE Book SET BookAmount='{0}' WHERE BookName='{1}'".format(result[4] + 1, result[1])
            sql2 = "INSERT INTO Log VALUES(0,'{0}','{1}','归还')".format(ans, result[1])
            try:
                cursor.execute(sql1)
                db.commit()
                print('归还成功')
                cursor.execute(sql2)
                db.commit()
                print('登记成功')
            except:
                db.rollback()
                db.close()
                print('归还失败')
            finally:
                return
            pass

    @staticmethod
    def StudentIn():
        db, cursor = GetCursor()
        StudentId = input('请输入要新增的学生学号')
        StudentPassword = input('请输入要新增的学生密码')
        sql = "INSERT INTO account VALUES('{0}','{1}')".format(StudentId, StudentPassword)
        try:
            cursor.execute(sql)
            db.commit()
            print('插入成功')
        except:
            db.rollback()
            db.close()
            print('插入失败')
        finally:
            return

    @staticmethod
    def StudentChange():
        db, cursor = GetCursor()
        StudentId = input('请输入要修改的学生学号')
        StudentPassword = input('请输入要修改的学生密码')
        sql = "UPDATE account SET PASSWORD='{0}' WHERE ID='{1}'".format(StudentPassword, StudentId)
        try:
            cursor.execute(sql)
            db.commit()
            print('修改成功')
        except:
            db.rollback()
            db.close()
            print('修改失败')
        finally:
            return

    @staticmethod
    def StudentDelete():
        db, cursor = GetCursor()
        StudentId = input('请输入要删除的学生学号')
        AdminPassword = input('请输入管理员密码')
        sql0 = "DELETE FROM account WHERE ID='{0}'".format(StudentId)
        sql1 = "SELECT * FROM account WHERE ID='%s'" % AdminPassword
        cursor.execute(sql1)
        result = cursor.fetchone()
        print(result)
        if result[1] == AdminPassword:
            try:
                cursor.execute(sql0)
                db.commit()
                print('删除成功')
            except:
                db.rollback()
                db.close()
                print('删除失败')
            finally:
                return
        else:
            print('密码错误')

    @staticmethod
    def BookIn():
        db, cursor = GetCursor()
        BookNumber = input('请输入新入馆图书的编号')
        BookName = input('请输入新入馆图书的书名')
        BookAuthor = input('请输入新入馆图书的作者')
        BookStatus = input('请输入是否可借阅（是/否）')
        BookAmount = input('请输入新入馆图书的数量')
        sql = "INSERT INTO book(BookNumber,BookName,BookAuthor,BookStatus,BookAmount) VALUES('{0}','{1}','{2}','{3}'," \
              "'{4}')".format(
            BookNumber, BookName, BookAuthor, BookStatus, BookAmount)
        try:
            cursor.execute(sql)
            db.commit()
            print('插入成功')
        except:
            db.rollback()
            db.close()
            print('插入失败')
        finally:
            return

    @staticmethod
    def BookChange():
        print("请选择您要进行的操作：")
        print('[1]修改图书编号')
        print('[2]修改图书数量')
        print('[0]返回上一级')
        AdminChoice = input()
        while 1:
            if AdminChoice == '1':
                print('因为后台数据库是自增的，请谨慎更改！')
                return
            if AdminChoice == '2':
                db, cursor = GetCursor()
                BookName = input('请输入要修改的图书名')
                BookAmount = input('请输入图书数量')
                sql = "UPDATE Book SET BookAmount='{0}' WHERE ID='{1}'".format(BookAmount, BookName)
                try:
                    cursor.execute(sql)
                    db.commit()
                    print('修改成功')
                except:
                    db.rollback()
                    db.close()
                    print('修改失败')
                finally:
                    return
            if AdminChoice == '0':
                break

    @staticmethod
    def BookDelete():
        db, cursor = GetCursor()
        DeleteBookNumber = input('请输入要删除的图书编号')
        AdminPassword = input('请输入管理员密码')
        sql0 = "DELETE FROM book WHERE BookNumber = '%s'" % DeleteBookNumber
        sql1 = "SELECT * FROM account WHERE ID='%s'" % 'admin'
        cursor.execute(sql1)
        result = cursor.fetchone()
        if result[1] == AdminPassword:
            try:
                cursor.execute(sql0)
                db.commit()
                print('删除成功')
            except:
                db.rollback()
                db.close()
                print('删除失败')
        else:
            print('密码错误')

    @staticmethod
    def SearchInfo():
        db, cursor = GetCursor()
        print("请选择您要进行的操作：")
        print('[1]查询图书情况')
        print('[2]查询已借阅图书情况')
        AdminChoice = input()
        while 1:
            if AdminChoice == '1':
                SearchVal = input('请输入要查询的书（书名或编号），按q返回上一级')
                if SearchVal == 'q':
                    break
                elif isinstance(SearchVal, str):
                    sql = "SELECT * FROM Book WHERE BookName='%s'" % SearchVal
                    try:
                        cursor.execute(sql)
                        result = cursor.fetchall()
                        if result:
                            print(result)
                        else:
                            print('未查询到相关信息')
                    except:
                        print('查询错误')
                    finally:
                        return
                else:
                    print('您的输入不合法，请重新输入！')
            if AdminChoice == '2':
                SearchVal = input('请输入要查询的书（书名或编号），按q返回上一级')
                if SearchVal == 'q':
                    break
                elif isinstance(SearchVal, str):
                    sql = "SELECT * FROM Log WHERE BookName='%s'" % SearchVal
                    try:
                        cursor.execute(sql)
                        result = cursor.fetchall()
                        if result:
                            print(result)
                        else:
                            print('未查询到相关信息')
                    except:
                        print('查询错误')
                    finally:
                        return
                else:
                    print('您的输入不合法，请重新输入！')


if __name__ == '__main__':
    IdChoice()
