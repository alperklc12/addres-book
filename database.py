import sqlite3


def get_all_fn():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    data = cursor.execute('SELECT * FROM persons').fetchall()
    connect.close()
    return data


def get_one_fn(per_id):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    data = cursor.execute('SELECT * FROM persons WHERE person_id=?', (per_id,)).fetchone()
    connect.close()
    return data


def save_fn(name, age, adres):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO persons (name, age, adress) VALUES (?, ?, ?)', (name, age, adres))
    connect.commit()
    connect.close()


def delete_fn(per_id):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM persons WHERE person_id=?', (per_id,))
    connect.commit()
    connect.close()


def udate_fn(per_id, name, age, adres):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('UPDATE persons SET name=?, age=?, adress=? WHERE  person_id=?', (name, age, adres, per_id))
    connect.commit()
    connect.close()
