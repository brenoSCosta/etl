import cx_Oracle


def gravadora(cur, curDW):
    checker = None
    cur.execute('select * from GRAVADORAS')
    for result in cur:
        statement = 'insert into DM_GRAVADORA(ID_GRAV,UF_GRAV,NAC_BRAS,NOM_GRAV) ' \
                    'VALUES ( :0, :1, :2, :3)'
        try:
            curDW.execute(statement, (result[0], result[1], result[2], result[3]))
        except cx_Oracle.IntegrityError:
            print("Erro!! Cadastros já existentes na DM_GRAVADORA")
            checker = True
            break
    if checker == None:
        print("Dados ETL realizados com sucesso. DM_GRAVADORA")


def socio(cur, curDW):
    checker = None
    cur.execute('SELECT * FROM SOCIOS')
    di = {}
    i = 0
    for result in cur:
        dsc = ''
        if result[2] == 1:
            dsc = 'Comum'
        elif result[2] == 2:
            dsc = 'Especial'
        elif result[2] == 3:
            dsc = 'Vip'
        di[i] = [result[0], result[4], dsc]
        i += 1
    for ii in di:
        statement = 'insert into DM_SOCIO(ID_SOC,NOM_SOC,TIPO_SOCIO) VALUES (:0,:1,:2)'
        try:
            curDW.execute(statement, (di[ii][0], di[ii][1], di[ii][2]))
        except cx_Oracle.IntegrityError:
            print("Erro!! Cadastros já existente na DM_SOCIO")
            checker = True
            break
    if checker == None:
        print("Dados ETL realizados com sucesso. DM_SOCIO")


def artista(cur, curDW):
    checker = None
    cur.execute("select * from ARTISTAS ")
    for result in cur:
        statement = 'insert into DM_ARTISTA(ID_ART,TPO_ART,NAC_BRAS,NOM_ART)' \
                    'VALUES (:0, :1, :2, :3)'
        try:
            curDW.execute(statement, (result[0], result[1], result[2], result[6]))
        except cx_Oracle.IntegrityError:
            print("Erro!! Cadastros já existentes na DM_ARTISTA")
            checker = True
            break
    if checker == None:
        print("Dados ETL realizados com sucesso. DM_ARTISTA")
