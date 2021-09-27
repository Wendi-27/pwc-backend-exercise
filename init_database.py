#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This project use sqlite3 as the relational database.
This module init the database of the web service. It create
the table of companies and insert the details of companies from the
csv file.
"""

import csv
import sqlite3

if __name__ == '__main__':
    connect = sqlite3.connect('database.db')
    with open('create_database.sql') as f:
        cmd = f.read()
        connect.executescript(cmd)

    with open('faux_id_fake_companies.csv') as csv_file:
        cur = connect.cursor()
        reader = csv.reader(csv_file)
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
            else:
                data_list = list(map(lambda x: x.strip(), row))
                if data_list[-1].lower() == 'no':  # convert 'YES' or 'No' to boolean values in sqlite database
                    data_list[-1] = '0'
                elif data_list[-1].lower() == 'yes':
                    data_list[-1] = '1'
                else:
                    print('Invalid data: {}, the value Restricted must be yes or no.'.format(" ".join(data_list)))
                    continue
                data_tuple = tuple(data_list)
                cur.execute(
                    "INSERT INTO companies (id, fake_company_name, description, tagline, company_email, business_number, restricted) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    data_tuple)
                line_count += 1
        connect.commit()
        connect.close()
