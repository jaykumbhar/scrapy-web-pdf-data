# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect("mydb.db")
curr = conn.cursor()
curr.execute("""drop table if exists poc_work""")
curr.execute("""create table poc_work (contact text, author text,tag text)""")
curr.execute("""insert into poc_work values(?,?,?)""",(
            'contact',
            'author',
            'tag'
        ))
conn.commit()
