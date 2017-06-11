#encoding:utf-8
import dbutils

USER_LOGIN_SQL = 'select uid from user where name=%s and password=md5(%s)'
USER_GET_USERS_SQL = 'select uid,name,age from user'
USER_ADD_USER_SAVE_SQL ='insert into user (name,password,age) VALUES (%s,md5(%s),%s)'
USER_DEL_USER_SQL='delete from user where uid=%s'
USER_INFO_MODIFY_SQL='select name,age from user where uid=%s'
USER_MODIFY_USER_SAVE_SQL='update user set name=%s,age=%s where uid=%s'

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

def user_check(name,password,age):
    if name.strip() == '':
        return False, "username can't be null"
    if len(name.strip()) < 0:
        return False, "username is too long "
    if len(password.strip()) < 5 or len(password.strip()) > 25:
        return False, "password is too long or too short"
    if password.strip() == '':
        return False, "password can't be null"
    if not str(age).isdigit() or int(age) > 120 or int(age) < 0:
        return False, "age is not num or too large or less than 0"
    return True, ""



#get topn
def get_topn(src, topn=10):
    stat_dict = {}
    fhandler = open(src, "rb")

    for line in fhandler:
        line_list = line.split()
        key = (line_list[0], line_list[6], line_list[8])
        stat_dict[key] = stat_dict.setdefault(key, 0) + 1

    fhandler.close()

    result = sorted(stat_dict.items(), key=lambda x:x[1])
    return result[:-topn - 1:-1]