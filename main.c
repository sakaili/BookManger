//
// Created by songz on 2021/6/5.
//
#include <windows.h>
#include <mysql.h>
#include <stdio.h>
#include "string.h"
#include<stdlib.h>
MYSQL *conn_ptr;
MYSQL_RES *res;//定义结果集变量
MYSQL_ROW row;//定义行变量
int StudentLogin();
int AdminLogin();
void BorrowBook();
void ReturnBook();

int main()
{

    conn_ptr = mysql_init(NULL);
    while(1)
    {
        printf("欢迎您使用图书馆系统服务请选择身份登录: \n1.管理员\n2.学生\n0.退出\n");
        int choice;
        printf("请输入您的选择:");
        scanf("%d",&choice);
        switch(choice)
        {
            case 2: StudentLogin();break;
            case 1 :AdminLogin();break;
            case 0 :printf("感谢您的使用，即将退出图书馆系统服务\n");exit(1);
            default:printf("输入无效，请重新输入\n");break;
        }
    }
}

int StudentLogin()
{
    int studentnumber;
    int password;
    char *query_result;
    char studentnumberstring[20];
    char passwordstring[7];
    char *passwordstring2;
    char *sql;
    printf("请输入您的学号：\n");
    scanf("%d",&studentnumber);
    itoa(studentnumber,studentnumberstring,10);
    printf(studentnumber);
    printf("请输入你的密码：\n");
    scanf("%d",&password);
    sql = "select PASSWORD from account where ID=";
    char *result = malloc(strlen(sql)+strlen(studentnumberstring)+1);
    strcpy(result, sql);
    strcat(result,studentnumberstring);
    if (!mysql_real_connect(conn_ptr, "localhost", "root", "515310szc", "library", 3306, NULL, 0))
    {
        printf("不能连接数据库!\n");
        exit(-1);
    }
    else
    {
        mysql_real_query(conn_ptr, result, strlen(result));
        res = mysql_store_result(conn_ptr);
        MYSQL_ROW row = mysql_fetch_row(res);
        //printf("%-10s ",row[0]);
        query_result = *&row[0];
        itoa(password,passwordstring,10);
        passwordstring2 = passwordstring;
        if (strcmp(passwordstring2,query_result)==0)
        {
            mysql_free_result(res);
            mysql_close(conn_ptr);
            while(1)
            {
                int choice;
                printf("登陆成功！\n");
                printf("请选择\n1:借书\n2:还书\n0:退出");
                scanf("%d",&choice);
                switch(choice)
                {
                    case 1: BorrowBook();break;
                    case 2 :ReturnBook();break;
                    case 0 :printf("感谢您的使用，即将退出图书馆系统服务\n");exit(1);
                    default:printf("输入无效，请重新输入\n");break;
                }
            }

        }
        else
        {
            printf("密码错误！请重新输入！\n\n\n\n");
            return 0;
        }
    }

}


void BorrowBook()
{
    MYSQL *conn_ptr = mysql_init(NULL);
    char *sql;
    char bookname[20];
    char *query_result;
    int book_amount;
    printf("请输入你要借的书名：");
    scanf("%s",bookname);
    sql = "select BookAmount from book where BookName=\"";
    char *result = malloc(strlen(sql)+strlen(bookname)+1);
    strcpy(result,sql);
    strcat(result,bookname);
    strcat(result,"\"");
    if (!mysql_real_connect(conn_ptr, "localhost", "root", "515310szc", "library", 3306, NULL, 0))
    {
        printf("不能连接数据库!\n");
        exit(-1);
    }
    else
    {
        mysql_real_query(conn_ptr, result, strlen(result));
        res = mysql_store_result(conn_ptr);
        row = mysql_fetch_row(res);
        query_result = row[0];
        char tem = query_result[0];
        int temp = tem - '0';
        if (temp>0)
        {
            int choice;
            printf("\n");
            printf("该书还剩余%d本\n",temp);
            printf("输入1确定借阅，输入0退出\n");
            char *sql_sentence = "insert into log(ID,BookName,Status) values(NULL,t,'借出')";
            for (int i=0;i< strlen(sql_sentence);i++)
            {
                if(sql_sentence[i]=='t')
                {
                    sql_sentence
                }
            }

            scanf("%d",&choice);
            switch (choice)
            {
                case 1:
                    mysql_
                case 0:
                    break;
            }
        }



    }


}

void ReturnBook()
{

}
int AdminLogin()
{

}