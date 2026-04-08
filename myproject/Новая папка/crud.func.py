#table yaratish
import sqlite3

conn = sqlite3.connect('mimi.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS oquvchilar(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ism TEXT NOT NULL,
        familiya TEXT NO NULL,
        sinf  TEXT,
        yosh INTEGER
        )
        ''')

conn.commit()
print("baza va jadval tayyor")





#CREATE - MALAUMOT QOSHISH


cursor = conn.cursor()

#Bitta oquvchi qoshish

cursor.execute(''' INSERT INTO oquvchilar (ism,familiya,sinf,yosh)
    VALUES (?,?,?,?)
    ''', ('Ruhshona','Rahimova','9-a', 15))


#Bir nechta oquvchi qoshish


oquvchilar = [
    ('Dilnoza','Azizova','10-b', 17),
    ('Bobur','Alimova', '11-g', 18),
    ('Anamoy', 'Gulimova', '10-a',17)
]


cursor.executemany('''
      INSERT INTO oquvchilar (ism,familiya,sinf,yosh)
      VALUES (?,?,?,?)
      ''', oquvchilar)

conn.commit()
print(f'{cursor.rowcount} ta oquvchi qoshildi')



#READ - MALUMOT OQISH

cursor=conn.cursor()




#Hamma oquvxchilarni korish
cursor.execute('SELECT * FROM oquvchilar ')
hamma = cursor.fetchall()
print("Hmma oquvchilar")
for oquvchi in hamma:
    print(f'ID:{oquvchi[0]} ISM : {oquvchi[1]},{oquvchi[2]},{oquvchi[3]}, sinf:{oquvchi[3]}, Yosh: {oquvchi[4]}')
    print("-"*30)




#UPDATE -Malumotni yangilash
cursor = conn.cursor()
cursor.execute('''
                UPDATE oquvchilar
                SET sinf = ?
                WHERE id= ?
''',('10-a', 1))


print(f'{cursor.rowcount} ta oquvchi yangilandi')


#DELETE - Malumotni ochiramz
cursor.execute('DELETE FROM oquvchilar WHERE sinf= ?', ('10-a',))


print(f'{cursor.rowcount} ta oquvchi ocirildi')




