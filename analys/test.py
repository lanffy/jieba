#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import jieba

db = MySQLdb.connect('127.0.0.1', 'root', '', 'ai_market')

uniqueTerms = {}
allTermsCount = 0

f = open('/Users/rlanffy/Desktop/out.csv', 'a+')

cursor = db.cursor()
sql = 'select p.product_name,p.product_summary from market_product p;'
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    terms = jieba.cut(row[0])
    for term in terms:
        if len(term) < 2:
            continue
        allTermsCount += 1
        if term not in uniqueTerms:
            uniqueTerms[term] = 1
        else:
            uniqueTerms[term] += 1
    terms = jieba.cut(row[1])
    for term in terms:
        if len(term) < 2:
            continue
        allTermsCount += 1
        if term not in uniqueTerms:
            uniqueTerms[term] = 1
        else:
            uniqueTerms[term] += 1

db.close()

allTermsCount = float(allTermsCount)

for ut in uniqueTerms:
    td = float(uniqueTerms[ut]) / allTermsCount * 100
    out = "%s,%d,%f\n" % (ut, uniqueTerms[ut], td)
    f.writelines(out.encode('utf-8'))


