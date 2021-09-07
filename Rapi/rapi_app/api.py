import pyodbc
import json, datetime

def get_logdata():
    server = 'signus-sf1.koreacentral.cloudapp.azure.com,14443'
    database = 'H3_DB'
    username = 'hanmi'
    password = 'u3hanmi'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = cnxn.cursor()

    r1 = cursor.execute("SELECT * FROM T_SYS_LOG_SF WHERE SEND_YN = 'N' ORDER BY 1;")

    d_dict = {}
    i = 0


    for row in r1:
        d_dict[i] = {'id':row[0],'ctkey':row[1], 'logdate':row[2],
                    'use':row[3], 'user':row[4], 'con_ip':row[5]}
                    # 'dataUsgqty':row[6], 'SEND_YN':row[7], 'PROC_NM':row[8]}
        i = i+1

    json.dumps(d_dict)
    # print(d_dict[1])
    # print(type(d_dict[1]))

    # url = "http://127.0.0.1:8000/api/get/"
    # headers = {'Content-Type':'application/json; charset=utf-8'}
    # response = requests.post(url, data=d_dict[1], headers=headers, verify=False)



    # while row:
    #     print(row[0])
    #     row = cursor.fetchone()

    return d_dict

    cnxn.close()
