import pymysql
import tkinter as tk
from tkinter import messagebox


db = pymysql.connect(host="localhost", user="root", password="avt008",database="vetri")
cursor = db.cursor()


'''CREATE TABLE avt008 (stocks_name varchar(50),price int,username varchar(50),client_id int primary key)'''
def insert_data():
    stocks_name = entry1.get()
    price = entry2.get()
    username = entry3.get()
    client_id = entry4.get()
    cursor.execute("INSERT INTO avt008 (stocks_name, price, username, client_id) VALUES (%s, %s, %s, %s)", (stocks_name, price, username, client_id))
    db.commit()
    msg=messagebox.showinfo("INSERT","INSERTED SUCESSFULLY")


def update_data():
    stocks_name = entry1.get()
    price = entry2.get()
    username = entry3.get()
    client_id = entry4.get()
    cursor.execute("UPDATE avt008 SET price=%s, username=%s , stocks_name=%s WHERE client_id=%s",(price, username, stocks_name, client_id))
    db.commit()
    msg = messagebox.showinfo("UPDATE", "UPDATED SUCESSFULLY")


def delete_data():
    stocks_name = entry1.get()
    cursor.execute("DELETE FROM avt008 WHERE stocks_name = %s", (stocks_name))
    db.commit()
    msg = messagebox.showinfo("DELETE", "DELETED SUCESSFULLY")

def select_data():
    sql = """SELECT * FROM avt008"""

    cursor.execute(sql)

    rows = cursor.fetchall()

    table_window = tk.Tk()
    table_window.title("User Table")
    table_window.geometry("500x500")
    table_window.configure(bg="#ffffff")

    stocksname_label = tk.Label(table_window, text="Stocks Name")
    stocksname_label.grid(column=0, row=0)


    price_label = tk.Label(table_window, text="Price")
    price_label.grid(column=1, row=0)

    username_label = tk.Label(table_window, text="Username")
    username_label.grid(column=2, row=0)

    clientid_label = tk.Label(table_window, text="Client Id")
    clientid_label.grid(column=3, row=0)

    for i, row in enumerate(rows):
        stocks_name_entry = tk.Entry(table_window)
        stocks_name_entry.grid(column=0, row=i + 1)
        stocks_name_entry.insert(tk.END, row[0])

        price_entry = tk.Entry(table_window)
        price_entry.grid(column=1, row=i + 1)
        price_entry.insert(tk.END, row[1])

        username_entry = tk.Entry(table_window)
        username_entry.grid(column=2, row=i + 1)
        username_entry.insert(tk.END, row[2])

        client_id_entry = tk.Entry(table_window)
        client_id_entry.grid(column=3, row=i + 1)
        client_id_entry.insert(tk.END, row[3])


window = tk.Tk()
window.title("Stocks Database")
window.geometry("300x200")
window.configure(bg='#00FFFF')


label1 = tk.Label(window, text="STOCKS NAME")
label1.grid(row=0, column=0)
label1.configure(bg="#D8DEEC")
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

label2 = tk.Label(window, text="PRICE")
label2.grid(row=1, column=0)
label2.configure(bg="#D8DEEC")
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

label3 = tk.Label(window, text="USERNAME")
label3.grid(row=2, column=0)
label3.configure(bg="#D8DEEC")
entry3 = tk.Entry(window)
entry3.grid(row=2, column=1)

label4 = tk.Label(window, text="CLIENT ID")
label4.grid(row=3, column=0)
label4.configure(bg="#D8DEEC")
entry4 = tk.Entry(window)
entry4.grid(row=3, column=1)


button1 = tk.Button(window, text="Insert", command=insert_data)
button1.grid(row=4, column=0)
button1.configure(bg="#FFFDD0")

button2 = tk.Button(window, text="Update", command=update_data)
button2.grid(row=4, column=1)
button2.configure(bg="#FFFDD0")

button3 = tk.Button(window, text="Delete", command=delete_data)
button3.grid(row=4, column=2)
button3.configure(bg="#FFFDD0")

button4 = tk.Button(window, text="Select", command=select_data)
button4.grid(row=4, column=3)
button4.configure(bg="#FFFDD0")


window.mainloop()