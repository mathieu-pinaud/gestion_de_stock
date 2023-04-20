import mysql.connector
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    def __init__(self):
        self.connecteur = mysql.connector.connect(host="localhost", user="root", password=os.getenv("aaaa"), database="boutique")
        self.cursor = self.connecteur.cursor()
        self.categorie = self.read_table('categorie')

    def read_table(self, table):
        query = 'SELECT * FROM ' + table + ';'
        self.cursor.execute(query)
        return(self.cursor.fetchall())
    
    def read_product(self, modif_id):
        query = 'SELECT * FROM produit WHERE id=' + str(modif_id) + ';'
        self.cursor.execute(query)
        return(self.cursor.fetchone()) 

    def delete_id(self, id):
        self.cursor.execute("DELETE FROM produit WHERE id=%s", (id,))
        self.connecteur.commit()
    
    def update(self, name, description, price, quantity, id_category, modif_id):
        self.cursor.execute("UPDATE produit SET nom=%s, description=%s, prix=%s, quantite=%s, id_categorie=%s WHERE id=" + str(modif_id) + ";", (name, description, price, quantity, id_category))
        self.connecteur.commit()

    def generate(self, name, description, price, quantity, id_category):
        self.cursor.execute("INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)" , (name, description, price, quantity, id_category))
        self.connecteur.commit()
    
    def close_everything(self):
        self.connecteur.close()
        self.cursor.close()
