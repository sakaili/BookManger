//
// Created by songz on 2021/6/5.
//
#include <windows.h>
#include <mysql.h>
#include <stdio.h>
#include "string.h"
#include<stdlib.h>
MYSQL *conn_ptr;
MYSQL_RES *res;//������������
MYSQL_ROW row;//�����б���
int StudentLogin();
int AdminLogin();
void BorrowBook();
void ReturnBook();

int main()
{

    conn_ptr = mysql_init(NULL);
    while(1)
    {
        printf("��ӭ��ʹ��ͼ���ϵͳ������ѡ����ݵ�¼: \n1.����Ա\n2.ѧ��\n0.�˳�\n");
        int choice;
        printf("����������ѡ��:");
        scanf("%d",&choice);
        switch(choice)
        {
            case 2: StudentLogin();break;
            case 1 :AdminLogin();break;
            case 0 :printf("��л����ʹ�ã������˳�ͼ���ϵͳ����\n");exit(1);
            default:printf("������Ч������������\n");break;
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
    printf("����������ѧ�ţ�\n");
    scanf("%d",&studentnumber);
    itoa(studentnumber,studentnumberstring,10);
    printf(studentnumber);
    printf("������������룺\n");
    scanf("%d",&password);
    sql = "select PASSWORD from account where ID=";
    char *result = malloc(strlen(sql)+strlen(studentnumberstring)+1);
    strcpy(result, sql);
    strcat(result,studentnumberstring);
    if (!mysql_real_connect(conn_ptr, "localhost", "root", "515310szc", "library", 3306, NULL, 0))
    {
        printf("�����������ݿ�!\n");
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
                printf("��½�ɹ���\n");
                printf("��ѡ��\n1:����\n2:����\n0:�˳�");
                scanf("%d",&choice);
                switch(choice)
                {
                    case 1: BorrowBook();break;
                    case 2 :ReturnBook();break;
                    case 0 :printf("��л����ʹ�ã������˳�ͼ���ϵͳ����\n");exit(1);
                    default:printf("������Ч������������\n");break;
                }
            }

        }
        else
        {
            printf("����������������룡\n\n\n\n");
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
    printf("��������Ҫ���������");
    scanf("%s",bookname);
    sql = "select BookAmount from book where BookName=\"";
    char *result = malloc(strlen(sql)+strlen(bookname)+1);
    strcpy(result,sql);
    strcat(result,bookname);
    strcat(result,"\"");
    if (!mysql_real_connect(conn_ptr, "localhost", "root", "515310szc", "library", 3306, NULL, 0))
    {
        printf("�����������ݿ�!\n");
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
            printf("���黹ʣ��%d��\n",temp);
            printf("����1ȷ�����ģ�����0�˳�\n");
            char *sql_sentence = "insert into log(ID,BookName,Status) values(NULL,t,'���')";
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