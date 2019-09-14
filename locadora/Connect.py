import cx_Oracle
from locadora import EtlLocadora as tl
ip = '127.0.0.1'
port = 1521
SID = 'xe'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)


con = cx_Oracle.connect('LOCADORA', '123', dsn_tns)
cur = con.cursor()
conDW = cx_Oracle.connect('DW_LOCADORA','123', dsn_tns)
curDW = conDW.cursor()

#Teste pro git AA
#tl.gravadora(cur, curDW)
#tl.socio(cur, curDW)
tl.artista(cur,curDW)

conDW.commit()
curDW.close()
conDW.close()
cur.close()
con.close()