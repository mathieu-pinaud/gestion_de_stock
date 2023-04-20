from tkinter import *
from database import *
from csv import *

class Window(Database):
    def __init__(self):
        Database.__init__(self)
        self.wdw = Tk()
        self.wdw.title('stock')
        self.create_column()
        self.create_table()
        self.create_buttons()

    def create_buttons(self):
        self.button_add = Button(self.wdw, text='Ajouter produit', command=self.add_menu)
        self.button_add.grid(row = self.row + 1, columnspan=7, pady=3, sticky = S+W+E)
        self.button_modif = Button(self.wdw, text='Modifier produit', command=self.modif_menu)
        self.button_modif.grid(row = self.row + 2, columnspan=7, pady=3, sticky = S+W+E)
        self.button_delete = Button(self.wdw, text='Supprimer produit', command=self.delete_menu)
        self.button_delete.grid(row = self.row + 3, columnspan=7, pady=3, sticky = S+W+E)
        self.button_csv = Button(self.wdw, text='Exporter en CSV', command=self.csv_export)
        self.button_csv.grid(row = self.row + 4, columnspan=7, pady=3, sticky = S+W+E)
    
    def csv_export(self):
        fd = open('products.csv', 'w')
        pen = writer(fd)
        pen.writerow(['id', 'nom', 'descritpion', 'prix', 'quantité', 'id de la categorie', 'category'])
        for item in self.data_list:
            l = [item[0], item[1], item[2], item[3], item[4], item[5], self.categorie[0][item[5] - 1]]
            pen.writerow(l)
        fd.close()

    def erase_buttons(self):
        self.button_add.destroy()
        self.button_modif.destroy()
        self.button_delete.destroy()
        self.button_csv.destroy()

    def erase_add(self):
        self.new_name.destroy()
        self.name_entry.destroy()
        self.new_description.destroy()
        self.description_entry.destroy()
        self.new_price.destroy()
        self.price_entry.destroy()
        self.new_quantity.destroy()
        self.quantity_entry.destroy()
        self.new_category.destroy()
        self.category_entry.destroy()
        self.button_cancel_add.destroy()
        self.button_validate_add.destroy()
        self.create_table()
        self.create_buttons()

    def erase_modif(self):
        self.modif_id.destroy()
        self.id_entry.destroy()
        self.modif_name.destroy()
        self.name_entry.destroy()
        self.modif_description.destroy()
        self.description_entry.destroy()
        self.modif_price.destroy()
        self.price_entry.destroy()
        self.modif_quantity.destroy()
        self.quantity_entry.destroy()
        self.modif_category.destroy()
        self.category_entry.destroy()
        self.button_cancel_modif.destroy()
        self.button_validate_modif.destroy()
        self.create_table()
        self.create_buttons()

    def erase_delete(self):
        self.id_delete.destroy()
        self.id_entry.destroy()
        self.button_cancel_delete.destroy()
        self.button_validate_delete.destroy()
        self.create_table()
        self.create_buttons()

    def delete_menu(self):
        self.erase_buttons()
        self.id_delete = Label(self.wdw, text='id du produit a supprimer :')
        self.id_delete.grid(row=self.row + 1, pady=3)
        self.id_entry = Entry(self.wdw)
        self.id_entry.grid(row = self.row + 1, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.button_cancel_delete = Button(self.wdw, text = 'annuler', command=self.erase_delete)
        self.button_validate_delete = Button(self.wdw, text='valider', command=self.validate_delete)
        self.button_cancel_delete.grid(row = self.row + 2, columnspan=7, pady=3, sticky='SWEN')
        self.button_validate_delete.grid(row = self.row + 3, columnspan=7, pady=3, sticky='SWEN')

    def validate_delete(self):
        id = self.id_entry.get()
        self.delete_id(id)
        self.erase_delete()


    def add_menu(self):
        self.erase_buttons()
        self.new_name = Label(self.wdw, text='nom :')
        self.new_name.grid(row = self.row + 1, pady=3, sticky='SWEN')
        self.name_entry = Entry(self.wdw)
        self.name_entry.grid(row = self.row + 1, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.new_description = Label(self.wdw, text='description :')
        self.new_description.grid(row = self.row + 2, pady=3, sticky='SWEN')
        self.description_entry = Entry(self.wdw)
        self.description_entry.grid(row = self.row + 2, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.new_price = Label(self.wdw, text='prix :')
        self.new_price.grid(row = self.row + 3, pady=3, sticky='SWEN')
        self.price_entry = Entry(self.wdw)
        self.price_entry.grid(row = self.row + 3, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.new_quantity = Label(self.wdw, text='quantite :')
        self.new_quantity.grid(row = self.row + 4, pady=3, sticky='SWEN')
        self.quantity_entry = Entry(self.wdw)
        self.quantity_entry.grid(row = self.row + 4, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.new_category = Label(self.wdw, text='catégorie (1 shonen/2 seinen) :')
        self.new_category.grid(row = self.row + 5, pady=3, sticky='SWEN')
        self.category_entry = Entry(self.wdw)
        self.category_entry.grid(row = self.row + 5, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.button_cancel_add = Button(self.wdw, text = 'annuler', command=self.erase_add)
        self.button_validate_add = Button(self.wdw, text='valider', command=self.validate_add)
        self.button_cancel_add.grid(row = self.row + 6, columnspan=7, pady=3, sticky='SWEN')
        self.button_validate_add.grid(row = self.row + 7, columnspan=7, pady=3, sticky='SWEN')

    def modif_menu(self):
        self.erase_buttons()
        self.modif_id = Label(self.wdw, text='id du produit à modifier :')
        self.modif_id.grid(row = self.row + 1, pady=3, sticky='SWEN')
        self.id_entry = Entry(self.wdw)
        self.id_entry.grid(row = self.row + 1, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.modif_name = Label(self.wdw, text='nouveau nom :')
        self.modif_name.grid(row = self.row + 2, pady=3, sticky='SWEN')
        self.name_entry = Entry(self.wdw)
        self.name_entry.grid(row = self.row + 2, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.modif_description = Label(self.wdw, text='nouvelle description :')
        self.modif_description.grid(row = self.row + 3, pady=3, sticky='SWEN')
        self.description_entry = Entry(self.wdw)
        self.description_entry.grid(row = self.row + 3, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.modif_price = Label(self.wdw, text='nouveau prix :')
        self.modif_price.grid(row = self.row + 4, pady=3, sticky='SWEN')
        self.price_entry = Entry(self.wdw)
        self.price_entry.grid(row = self.row + 4, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.modif_quantity = Label(self.wdw, text='nouvelle quantite :')
        self.modif_quantity.grid(row = self.row + 5, pady=3, sticky='SWEN')
        self.quantity_entry = Entry(self.wdw)
        self.quantity_entry.grid(row = self.row + 5, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.modif_category = Label(self.wdw, text='nouvelle catégorie (1 shonen/2 seinen) :')
        self.modif_category.grid(row = self.row + 6, pady=3, sticky='SWEN')
        self.category_entry = Entry(self.wdw)
        self.category_entry.grid(row = self.row + 6, column=1, columnspan=6, pady=3, sticky='SWEN')
        self.button_cancel_modif = Button(self.wdw, text = 'annuler', command=self.erase_modif)
        self.button_validate_modif = Button(self.wdw, text='valider', command=self.validate_modif)
        self.button_cancel_modif.grid(row = self.row + 7, columnspan=7, pady=3, sticky='SWEN')
        self.button_validate_modif.grid(row = self.row + 8, columnspan=7, pady=3, sticky='SWEN')

    def validate_add(self):
        name = self.name_entry.get()
        descritpion = self.description_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        id_category = self.category_entry.get()
        self.generate(name, descritpion, price, quantity, id_category)
        self.erase_add()

    def validate_modif(self):
        modif_id = self.id_entry.get()
        base_product_tuple = self.read_product(modif_id)
        name = self.name_entry.get()
        description = self.description_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        id_category = self.category_entry.get()

        if name == '':
            name = base_product_tuple[1]
        if description == '':
            description = base_product_tuple[2]
        if price == '':
            price = base_product_tuple[3]
        if quantity == '':
            quantity = base_product_tuple[4]
        if id_category == '':
            id_category = base_product_tuple[5]

        self.update(name, description, price, quantity, id_category, modif_id)
        self.erase_modif()

    def create_column(self):
        text = Label(self.wdw, text='id')
        text.grid(row= 0, column = 0, sticky='NSWE', ipadx=5, ipady= 3)
        text = Label(self.wdw, text='nom')
        text.grid(row= 0, column = 1, sticky='NSWE', ipadx=5, ipady= 3)
        text = Label(self.wdw, text='description')
        text.grid(row= 0, column = 2, sticky='NSWE', ipadx=5, ipady= 3)
        text = Label(self.wdw, text='prix')
        text.grid(row= 0, column = 3, sticky='NSWE', ipadx=5, ipady= 3)
        text = Label(self.wdw, text='quantite')
        text.grid(row= 0, column = 4, sticky='NSWE', ipadx=5, ipady= 3)
        text = Label(self.wdw, text='categorie')
        text.grid(row= 0, column = 5, columnspan=2, sticky='NSWE', ipadx=5, ipady= 3)
    
    def create_table(self): 
        self.data_list = self.read_table('produit')
        self.row = 0
        self.column = 0
        row = 1
        column = 0

        for data in self.data_list:
            for item in data:
                text = Label(self.wdw, text=item, relief='sunken')
                text.grid(row= row, column = column, sticky='NSWE', ipadx=5, ipady=2)
                column += 1
            text = Label(self.wdw, text=self.categorie[data[5] - 1][1], relief='sunken')
            text.grid(row = row, column=column, sticky='NSEW', ipadx=5, ipady=2)
            self.column = column
            column = 0
            row += 1
        self.row = row - 1


