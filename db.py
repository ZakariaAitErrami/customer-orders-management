import cx_Oracle
#connection = cx_Oracle.connect("system","zakaria","localhost/orcl")
try:
	conn = cx_Oracle.connect("C##ZAKARIA","zakaria","localhost/orcl")
except Exception as err:
	print('Error while creating the connection ',err)
cur = conn.cursor()
print('les tables: client, marchandise, commande, ligne_commande')
table=input('Donner le nom de la table: ')
ope=input('Donner le type d\'operation (select, insert, delete, update, join,search):')
if ope.upper()=='INSERT':	
    if table.lower()=='client':
	    c=list()
	    client_id=input('Donner l\'id du client (10 caracteres): ')
	    c.append(client_id)
	    nom_client=input('Donner le nom et le prenom du client: ')
	    c.append(nom_client)
	    sql = """ INSERT INTO client VALUES(:1,:2)"""
	    cur.execute(sql,c)
	    print('Insert completed!!')
    elif table.lower()=='marchandise':
	    m=list()
	    marchandise_id=input('Enter the merchandise ID: ')
	    m.append(marchandise_id)
	    descr=input('Enter the merchandise description: ')
	    m.append(descr)
	    prix=input('Enter the price of the merchandise: ')
	    m.append(prix)
	    sql = """INSERT INTO marchandise VALUES(:1,:2,:3) """
	    cur.execute(sql,m)
	    print('Insert Completed!!')
    elif table.lower()=='commande':
	    com=list()
	    client_id=input('Donner l\'id de client: ')
	    com.append(client_id)
	    command_id=input('Donner l\'id de la commande (10 caracteres): ')
	    com.append(command_id)
	    sql="""INSERT INTO commande VALUES(:1,:2)"""
	    cur.execute(sql,com)
	    print('Insert Completed!!')
    elif table.lower()=='ligne_commande':
	    lc=list()
	    command_id=input('Donner l\'id de la commande: ')
	    lc.append(command_id)
	    marchandise_id=input('Donner l\' id du marchandise: ')
	    lc.append(marchandise_id)
	    quantity=input('Donner la quantite commande: ')
	    lc.append(quantity)
    else:
        print('La table ' + table + ' n\'exsiste pas dans la base de donnees !!')
elif ope.upper()=='SELECT':
    if table.lower()=='client':
        sql=""" SELECT * FROM client """
        cur.execute(sql)
        row=cur.fetchall()
        print('Customers information : ')
        for index, record in enumerate(row):
            print(index,': ', record)
    elif table.lower()=='marchandise':
        sql=""" SELECT * FROM marchandise """
        cur.execute(sql)
        row=cur.fetchall()
        for index, record in enumerate(row):
            print(index, ': ',record)
        #for x in cur.description:
            #print(x)
    elif table.lower()=='commande':
        sql="""SELECT * FROM commande """
        cur.execute(sql)
        row=cur.fetchall()
        for r in row:
            print(r)
    elif table.lower()=='ligne_commande':
        sql="""SELECT * FROM ligne_commande"""
        cur.execute(sql)
        row=cur.fetchall()
        for index, record in enumerate(row):
            print(index, ': ',record)
    else:
        print('La table ' + table + ' n\'exsiste pas dans la base de donnees !!')
elif ope.upper()=='DELETE':
    if table.lower()=='client':
        try:
            sql="""DELETE FROM client WHERE id_client=:id"""
            id=input('Donner l\'id de client a supprimé: ')
            cur.execute(sql,{'id':id})
            print('row deleted')
        except Exception as err:
            print('Error while deleting data from the table!!', err)
    elif table.lower()=='commande':
        try:
            sql="""DELETE FROM commande WHERE id_commande=:com"""
            idcom=input('Donner l\'id de la commaned à supprimé:' )
            cur.execute(sql,{'com':idcom})
            print('row deleted')
        except Exception as err:
            print('Error while deleting data from the table!!', err)
    elif table.lower()=='marchandise':
        try:
            sql="""DELETE FROM marchandise WHERE id_marchandise=:mar"""
            idm=input('Donner l\'id de la marchandise à supprimé: ')
            cur.execute(sql,{'mar':idm})
            print('row deleted')
        except Exception as err:
            print('Error while deleting data from the table!!', err)
    elif table.lower()=='ligne_commande':
        try:
            sql="""DELETE FROM ligne_commande WHERE id_commande:=com AND id_marchandise:=mar"""
            comm=input('Donner l\'id de la commande: ')
            marr=input('Donner l\'id de la marchandise: ')
            cur.execute(sql,{'com':comm,'mar':marr})
            print('row deleted')
        except Exception as err:
            print('Error while deleting data from the table!!', err)
    else:
        print('La table ' + table + ' n\'exsiste pas dans la base de donnees !!')
elif ope.upper()=='UPDATE':
    if table.lower()=='client':
        l=list()
        try:
            sql="""UPDATE client SET id_client=:1, nom_client=:2 WHERE id_client=:3 """
            oid=input('Donner l\'id du client à mettre à jour: ')
            nid=input('Donner le nouveau id de client: ')
            nn=input('Donner le nouveau nom: ')
            l.append(nid)
            l.append(nn)
            l.append(oid)
            #cur.execute(sql,{'oid':oid,'newid':nid,'newname':nn})
            cur.execute(sql,l)
            print('row updated!')
        except Exception as err:
            print('Error while updating data ',err)
    elif table.lower()=='commande':
        l=list()
        try:
            sql=""""UPDATE commande SET
            id_commande=:1,
            id_client=:2 WHERE id_commande=:3 """
            oidc=input('Donner l\'id de la commande à mettre à jour: ')
            nidcm=input('Donner le numéro de la nouvelle comamnde: ')
            nidcl=input('Donner le nouveau id de client: ')
            l.append(nidcm)
            l.append(nidcl)
            l.append(oidc)
            cur.execute(sql,l)
        except Exception as err:
            print('Error while updating data ',err)
    elif table.lower()=='marchandise':
        l=list()
        try:
            sql="""UPDATE marchandise SET id_marchandise=:1, description=:2, unit_price=:3 WHERE id_marchandise:=4"""
            oid=input('Donner l\'id de la marchandise à mettre à jour: ')
            nid=input('Donner le nouveau id de la marchandise: ')
            desc=input('Donner la description de la marchandise: ')
            prix=int(input('Donner le prix de la marchandise: '))
            l.append(nid)
            l.append(desc)
            l.append(prix)
            l.append(oid)
            cur.execute(sql,l)
        except Exception as err:
            print('Error while updating data ',err)
    elif table.lower()=='ligne_commande':
        l=list()
        try:
            sql="""UPDATE FROM ligne_commande SET quantity=:1 WHERE id_commande=:2 AND id_marchandise:=3"""
            idc=input('Donner l\'id de la commande à mettre à jour: ')
            idm=input('Donner l\'id de la marchandise à mettre à jour: ')
            q=int(input('Donner la nouvelle valeur de la quantité commandé: '))
            l.append(q)
            l.append(idc)
            l.append(idm)
            cur.execute(sql,l)
        except Exception as err:
            print('Error while updating data ',err)
    else:
        print('La table ' + table + ' n\'exsiste pas dans la base de donnees !!')
elif ope.upper()=='JOIN':
    sql="""SELECT client.nom_client, ligne_commande.id_commande,
    marchandise.description, ligne_commande.quantity,
    marchandise.unit_price /100 AS "unit_price_decimal",
    ligne_commande.quantity * marchandise.unit_price / 100 AS "prix_total"
    FROM ligne_commande, commande, client, marchandise
    WHERE
    ligne_commande.id_marchandise = marchandise.id_marchandise AND
    commande.id_client = client.id_client AND
    ligne_commande.id_commande = commande.id_commande
    ORDER BY nom_client, ligne_commande.id_commande,
    marchandise.description"""
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
elif ope.upper()=='SEARCH':
    if table.lower()=='client':
        sql="""SELECT * FROM client WHERE id_client LIKE :id"""
        id=input('Donner l\'id du client que vous cherchez: ')
        data={'id':id}
        cur.execute(sql,data)
        row=cur.fetchall()
        for  record in row:
            print('l\'id est: ',record[0],' nom: ',record[1])
    elif table.lower()=='commande':
        sql="""SELECT cl.id_client, cl.nom_client, com.id_commande, m.id_marchandise, m.description, m.unit_price, 
            lc.quantity, lc.quantity*m.unit_price AS "Prix total"
            FROM client cl, commande com, marchandise m, ligne_commande lc
            WHERE cl.id_client= com.id_client AND com.id_commande=lc.id_commande AND lc.id_marchandise=m.id_marchandise
            AND com.id_commande=:idcom """
        idcom=input('Donner l\'id de la commande que vous cherchez: ')
        data={'idcom':idcom}
        cur.execute(sql,data)
        rows=cur.fetchall()
        print(' \t\t\t\t-------------la commande numéro: ',idcom,'---------------------')
        for record in rows:
            print('l\'id de client: ',record[0], ' son nom: ',record[1], ' l\'id de sa commande: ',record[2],  ' l\'id de la marchandise acheté: ',record[3])
            print('la description de la marchandise: ',record[4])
            print('le prix unitaire est: ',record[5], ' la quantité commandé: ',record[6])
            print('Le prix total : ',record[7])
            print('\t\t\t----------------------------------------------------')
    elif table.lower()=='marchandise':
        sql="""SELECT * FROM marchandise WHERE id_marchandise=:idmar"""
        idmar=input('Donner l\'id de marchandise que vous cherchez: ')
        data={'idmar':idmar}
        cur.execute(sql,data)
        row=cur.fetchone()
        print('l\'id de la marchandise: ',row[0])
        print('Description: ',row[1])
        print('Le prix: ',row[2]) 
    else:
         print('La table ' + table + ' n\'exsiste pas dans la base de donnees !!')      
else:
    print('Operation inconnu!!!')
conn.commit()
