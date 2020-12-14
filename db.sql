CREATE TABLE marchandise(
    id_marchandise CHAR(10),
    description VARCHAR2(60),
    unit_price NUMBER,
    CONSTRAINT mar_id_marchandise_pk PRIMARY KEY (id_marchandise)
);
ALTER TABLE marchandise ADD CONSTRAINT marchandise_description_uk UNIQUE(description);
DESC marchandise

CREATE TABLE client(
        id_client CHAR(10),
        nom_client VARCHAR2(50),
        CONSTRAINT client_id_client_pk PRIMARY KEY (id_client)
);
DESC client

CREATE TABLE commande(
        id_commande CHAR(10),
        id_client CHAR(10),
        id_marchandise CHAR(10),
        CONSTRAINT commande_id_commande_pk PRIMARY KEY(id_commande),
        CONSTRAINT commande_id_client_fk FOREIGN KEY(id_client) REFERENCES client(id_client)
);
DESC commande
ALTER TABLE commande DROP COLUMN id_marchandise;

CREATE TABLE ligne_commande(
     id_commande CHAR(10),
     id_marchandise CHAR(10),
     quantity NUMBER,
     CONSTRAINT ligne_com_idcom_idmar_pk PRIMARY KEY(id_commande,id_marchandise),
     CONSTRAINT ligne_com_id_com_fk FOREIGN KEY(id_commande) REFERENCES commande(id_commande),
     CONSTRAINT ligne_com_id_mar_fk FOREIGN KEY(id_marchandise) REFERENCES marchandise(id_marchandise)
);

INSERT INTO client(id_client,nom_client) VALUES('C000000001','Zakaria AIT ERRAMI');
INSERT INTO client(id_client,nom_client) VALUES('C000000002','Soukaine HAFIDI');
INSERT INTO client(id_client,nom_client) VALUES('C000000003','Ahmed ALI');
SELECT * FROM client;
UPDATE client SET nom_client='Soukaina HAFIDI' WHERE id_client='C000000002';
DELETE FROM client WHERE id_client='C000000003';
SELECT * FROM client;


INSERT INTO marchandise(id_marchandise,description,unit_price)
 VALUES('DR943TA39F','Manuel du guerir de la lumiere ecrit par Paulo Coelho', 500);
INSERT INTO marchandise(id_marchandise,description,unit_price)
 VALUES('BA8379CF0K', 'Dell ordinateur portable Core i5 8Go de RAM SSD 256 Go', 40000);
INSERT INTO marchandise(id_marchandise,description,unit_price)
 VALUES('TH30759G6L','Manette sans fil pour Playstation 4',2500); 

INSERT INTO commande(id_client,id_commande) VALUES('C000000001','D000000001');
INSERT INTO commande(id_client,id_commande) VALUES('C000000001','D000000002');
   INSERT INTO commande(id_client,id_commande) VALUES('C000000002','D000000003');

#commande de zakaria
INSERT INTO ligne_commande(id_commande,id_marchandise,quantity) VALUES('D000000001','BA8379CF0K',4);
INSERT INTO ligne_commande(id_commande,id_marchandise,quantity) VALUES('D000000001','DR943TA39F',2);
INSERT INTO ligne_commande(id_commande,id_marchandise,quantity) VALUES('D000000001','TH30759G6L',1);
#deuxieme commande de zakaria (secons screenshot)
INSERT INTO ligne_commande(id_commande,id_marchandise,quantity) VALUES('D000000002','BA8379CF0K',20);
INSERT INTO ligne_commande(id_commande,id_marchandise,quantity) VALUES('D000000002','DR943TA39F',50);
INSERT INTO ligne_commande(id_commande,id_marchandise,quantity) VALUES('D000000002','TH30759G6L',15);
#commade de soukaina (third screenshot)
  INSERT INTO ligne_commande(id_commande,id_marchandise,quantity) VALUES('D000000003','DR943TA39F',1000);
  INSERT INTO ligne_commande(id_commande,id_marchandise,quantity) VALUES('D000000003','TH30759G6L',500);
SELECT * FROM commande;


SELECT
client.nom_client,
ligne_commande.id_commande,
marchandise.description,
ligne_commande.quantity,
marchandise.unit_price /100 AS "unit_price_decimal",
ligne_commande.quantity * marchandise.unit_price / 100 AS "prix_total"
FROM ligne_commande, commande, client, marchandise
WHERE
ligne_commande.id_marchandise = marchandise.id_marchandise AND
commande.id_client = client.id_client AND
ligne_commande.id_commande = commande.id_commande
ORDER BY
nom_client,
ligne_commande.id_commande,
marchandise.description;


SELECT  client.nom_client, commande.id_commande, 
SUM(ligne_commande.quantity*marchandise.unit_price) "Prix total" 
FROM client, marchandise, commande, ligne_commande 
WHERE client.ID_CLIENT=commande.ID_CLIENT 
AND ligne_commande.ID_COMMANDE=commande.ID_COMMANDE 
AND ligne_commande.ID_MARCHANDISE=marchandise.ID_MARCHANDISE
GROUP BY commande.id_commande, client.nom_client
ORDER BY commande.id_commande;

SELECT id_marchandise, description
      CASE unit_price WHEN unit_price<500 THEN 'cheap'
      ELSE 'expensive' END "Classification"
FROM marchandise;

SELECT id_marchandise, description, 
TO_CHAR(unit_price,'9999999.99$') "prix_unitaire" FROM marchandise 
WHERE id_marchandise IN 
         (SELECT id_marchandise FROM ligne_commande WHERE quantity>=1000);

CREATE OR REPLACE VIEW commande_zakaria
   AS 
   SELECT  client.nom_client, commande.id_commande, 
     SUM(ligne_commande.quantity*marchandise.unit_price) "Prix total" 
     FROM client, marchandise, commande, ligne_commande 
     WHERE client.ID_CLIENT=commande.ID_CLIENT 
     AND ligne_commande.ID_COMMANDE=commande.ID_COMMANDE 
     AND ligne_commande.ID_MARCHANDISE=marchandise.ID_MARCHANDISE
     AND client.nom_client LIKE 'Zakaria AIT ERRAMI'
GROUP BY commande.id_commande, client.nom_client;