#!/usr/bin/python3

import pymysql
import datetime
import time



def parse(command, cursor):
    cursor.execute(command)
    data = cursor.fetchall()

    if len(data) == 0:
        result = "none"
    else:
        result = str(data[0])
        result = result[19:]

        test = result.split(", ")
        year = test[0]
        month = test[1]
        day = test[2]

        hour = test[3]
        min = test[4]
        sec = test[5][0:2]

        result = year+ "-" + month + "-" +day + " " + hour + ":" + min + ":" + sec

    return result


def getLiveData():
    #open database
    db = pymysql.connect("localhost","tartan","tartan1234","TartanHome")
    cursor = db.cursor()


    # now = datetime.date.today().strftime('%Y-%m-%d')

    now = "2019-02-05"

    t_m1 = now + ' 00:00:01'
    t_m2 = now + ' 11:59:59'

    t_n1 = now + ' 12:00:00'
    t_n2 = now + ' 23:59:59'

    t_m = "select create_time from Home WHERE create_time between '" + t_m1 + "' and '" + t_m2 + "'" + " and light_state = 'off'"

    tm_mse = t_m + " and home_name = 'mse'"
    tm_cmu = t_m + " and home_name = 'cmu'"

    m_mse = parse(tm_mse, cursor)
    m_cmu = parse(tm_cmu, cursor)



    t_n = "select create_time from Home WHERE create_time between '" + t_n1 + "' and '" + t_n2 + "'" + " and light_state = 'on'"
    tn_mse = t_n + " and home_name = 'mse'"
    tn_cmu = t_n + " and home_name = 'cmu'"

    n_mse = parse(tn_mse, cursor)
    n_cmu = parse(tn_cmu, cursor)


    cursor.close()
    db.close()

    result_mse = m_mse + "," + n_mse
    result_cmu = m_cmu + "," + n_cmu
    result = result_mse + "," + result_cmu
    return result
