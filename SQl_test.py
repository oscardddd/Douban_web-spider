import sqlite3

conn = sqlite3.connect("test.db") #打开或创建数据库文件
c = conn.cursor()
def cretae_database():
    sql = '''
        create table ooops2
            (id int primary key not null,
            name text not null,
            age int not null,
            address char(50) not null,
            salary real);
'''



    print("create database successfully")

def insert_data():
    sql1 = '''
        insert into ooops2 (id,name,age,address, salary)
        values (1,'张三',32,"jinan",50000)
    '''

    sql2 = '''
        insert into ooops2 (id,name,age,address, salary)
        values (2,'李四',32,"jinan",5000)
    '''




def select_data():
    sql = "select id,name,address,salary from ooops2"
    cursor = c.execute(sql)
    for row in cursor:
        print("id = ",row[0])
        print("name = ",row[1])
      # 执行

    conn.commit()  # 提交数据库操作

    conn.close()  # 关闭链

    print("finished selection")
if __name__ == "__main__":
    select_data()