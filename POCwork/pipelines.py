# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
class PocworkPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn = sqlite3.connect("mydb.db")
        self.curr = self.conn.cursor()
        # import 
    def create_table(self):
        # import ipdb;ipdb.set_trace()
        # self.curr.execute("""drop table if exists poc_work""")
        if len(self.curr.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='poc_work';""").fetchall()) == 0:
            self.curr.execute("""create table poc_work (websiteContent text, date text, website text)""")
        else:
            pass
    def store_db(self,item):
        print("I am in store")
        # if
        data = self.curr.execute("""SELECT websitecontent,website FROM poc_work""").fetchall()
        if data:
            for webdata in data:
                if webdata[1]==item['website']:
                    if webdata[0] == item['websiteContent']:
                        print('I Found same data')
                        pass
                    else:
                        print("I found DIffrent data")
                        # import ipdb;ipdb.set_trace()
                        self.curr.execute("""insert into poc_work values(?,?,?)""",(
                            item['websiteContent'],
                            item['date'],
                            item['website'],
                        ))
        else:
            self.curr.execute("""insert into poc_work values(?,?,?)""",(
                item['websiteContent'],
                item['date'],
                item['website'],
            ))

                    
        self.conn.commit()

    def process_item(self, item, spider):
        print("I AM IN process_item >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        self.store_db(item)
        return item
