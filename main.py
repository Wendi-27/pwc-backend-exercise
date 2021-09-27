#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module is contains the backend service. The service is implemented by Flask
framework. There are 4 apis which implement the functions of the main page, getting
all companies from the database, getting all restricted companies from the database
and checking if the company is restricted.
"""

from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'COMPANY SERVICE 2021'


def get_db_connect():
    connect = sqlite3.connect('database.db')
    connect.row_factory = sqlite3.Row
    return connect


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getCompanies')
def get_compannies():
    connect = get_db_connect()
    cursor = connect.cursor()
    companies = cursor.execute('SELECT * FROM companies ORDER BY id ASC ').fetchall()
    connect.close()
    company_list = []
    if companies:
        for company_row in companies:
            company_dict = dict(company_row)  # SQLite does not have a separate Boolean storage class
            if company_dict['restricted'] == 0:  # Instead, Boolean values are stored as integers 0 (false) and 1 (true)
                company_dict['restricted'] = 'No'
            elif company_dict['restricted'] == 1:
                company_dict['restricted'] = 'Yes'
            company_list.append(company_dict)
    return jsonify({"companies": company_list})


@app.route('/getRestricted')
def get_restricted():
    connect = get_db_connect()
    cursor = connect.cursor()
    restricted_companies = cursor.execute('SELECT * FROM companies WHERE restricted = 1 ORDER BY id ASC ').fetchall()
    connect.close()
    company_list = []
    if restricted_companies:
        for company_row in restricted_companies:
            company_dict = dict(company_row)
            company_dict['restricted'] = 'Yes'
            company_list.append(company_dict)
    return jsonify({"restrictedCompanies": company_list})


@app.route('/checkRestricted/<string:business_number>')
def check_restricted(business_number):
    if business_number:
        connect = get_db_connect()
        cursor = connect.cursor()
        restricted_tag = cursor.execute('SELECT restricted FROM companies WHERE business_number = ?',
                                        (business_number,)).fetchone()
        connect.close()
        if not restricted_tag:  # convert the integer to boolean value
            return jsonify({'restricted': None})
        if restricted_tag['restricted'] == 0:
            return jsonify({'restricted': False})
        elif restricted_tag['restricted'] == 1:
            return jsonify({'restricted': True})
    return jsonify({'restricted': None})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
