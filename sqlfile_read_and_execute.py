import psycopg2
import sys
import pandas as pd

# sql ファイルの内容を実行する関数
def execute_sql_from_file(sqlfile):
    conn = psycopg2.connect("dbname=hoge host=fuga user = piyo password = pass port = moga")
    cursor = conn.cursor()

    sql_file = open(sqlfile)
    sql_data = sql_file.read()
    sql_file.close()

    cursor.execute(sql_data)
    result = pd.read_sql(sql=sql_data,con=conn)

    cursor.close()
    conn.close()

    return result

if __name__ == "__main__":
    sqlfile="test.sql"
    result = execute_sql_from_file(sqlfile)
    print(result)
