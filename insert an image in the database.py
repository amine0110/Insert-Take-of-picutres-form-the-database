import sqlite3 as db



with open('my_image.jpg','rb') as pic:
    photo = pic.read()
print(photo.__sizeof__())
dataBase = db.connect("data.db")

cursor = dataBase.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tab(name text, photo BLOB )")

cursor.execute("INSERT INTO tab VALUES(:name, :photo)",
               {
                   'name':"amine",
                   'photo':photo
               }
               )
cursor.execute("SELECT *, oid FROM tab")
items = cursor.fetchall()

photo = items[0][1]

exten = 'new.ico'
with open(exten, 'wb') as new_pic:
    my_new_pic = new_pic.write(photo)


dataBase.commit()
dataBase.close()