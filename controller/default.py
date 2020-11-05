import csv
from flask import Flask, request, render_template, make_response
import pandas as pd
import sqlite3

# рендер формы для файла
def home():
    # return make_response({ 'status': 'ok' }, 200)
    return render_template('form.html')

# получение и обаботка данных с формы. коннект в базу и вставка ВСЕХ данных
def form_file():
    connection = sqlite3.connect('test_database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS test_table (fiscal_number_cash_register, type_retail_order, date_receipt, sum_with_vat)''')

    csv_file = request.form['csv_file']

    chunksize = 100000
    i = 0

    for df in pd.read_csv(csv_file, chunksize = chunksize, iterator = True, sep='\t'):
        df = df.rename(columns = {'RNM': 'fiscal_number_cash_register', 'OPERATION_TYPE': 'type_retail_order', 'OPERATION_DATETIME': 'date_receipt', 'TOTAL_AMOUNT': 'sum_with_vat'})
        df.index += i
        del df['DEPARTMENT_NAME']
        del df['SERIAL_NUMBER']

        df.to_sql('test_table', connection, if_exists = 'append', index = False)

        i = df.index[-1] + 1

        print('index {}'.format(i))
        print(df)

    connection.commit()
    connection.close()

    return make_response({ 'status': 'ok', 'data': 'ok' }, 200)