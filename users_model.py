import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="store",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def do_query(query_str):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query_str)
            result = cursor.fetchall()
            return result
    except Exception as x:
        return None
    

def do_query_with_change(query_str):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query_str)
            connection.commit()
            return True
    except Exception as x:
        return False

def add_user(user_name_, name_, birth_date_, max_calories_, max_fat_, max_sugar_, max_protein_, current_state_ = "main"):
    pass

def get_user(user_name):
    pass

def is_exist_user_day(user_name, req_date):
    pass

def add_user_day(user_name, req_date):
    pass

def get_user_day(user_name, req_date):
    pass


