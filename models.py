#encoding:utf-8
import dbutils

USER_LOGIN_SQL = 'select id from user where name=%s and password=md5(%s)'
USER_GET_USERS_SQL = 'select id,name,age from user'
USER_ADD_USER_SAVE_SQL ='insert into user (name,password,age) VALUES (%s,md5(%s),%s)'
USER_DEL_USER_SQL='delete from user where id=%s'
USER_INFO_MODIFY_SQL='select name,age from user where id=%s'
USER_MODIFY_USER_SAVE_SQL='update user set name=%s,age=%s where id=%s'

#login check
def login_check(args):
    rt_cnt, rt_list = dbutils.execute_sql(USER_LOGIN_SQL, args, True)
    return rt_cnt

#users list
def get_users():
    rt_cnt, rt_list = dbutils.execute_sql(USER_GET_USERS_SQL, (), True)
    return  rt_list

#add user
def add_user_save(args):
    dbutils.execute_sql(USER_ADD_USER_SAVE_SQL,args,False)
    return True

#del user
def del_user(args):
    dbutils.execute_sql(USER_DEL_USER_SQL,args,False)
    return True

#get modify user_info
def modify_user_info(args):
    rt_cnt,rt_list=dbutils.execute_sql(USER_INFO_MODIFY_SQL,args,True)
    return rt_list

#modify user save
def modify_user_save(args):
    dbutils.execute_sql(USER_MODIFY_USER_SAVE_SQL,args,False)
    return True
