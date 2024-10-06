#09 ☎️ Contact Book
# Crea una libreta de contactos que:
# - Mantenga una lista de contactos
# - Permita agregar nuevos contactos (nombre, teléfono, email)
# - Permita buscar contactos por nombre
# - Muestre todos los contactos
# - Permita editar la información de los contactos existentes
# - Implemente una función para exportar los contactos a un archivo CSV

from flask import Flask, render_template, redirect, url_for, flash, request
app = Flask (__name__)
app.secret_key = "kkroto"

#modelo contactos
class Contacts:
    def __init__(self, name, cellphone, email):
        self.name = name
        self.cellphone = cellphone
        self.email = email
        Contacts.list.append (self)
    
    def search (self, name):
        if len(Contacts.list) > 0:
            for contact in Contacts.list:
                if contact.name == name:
                    flash(f"\nContacto encontrado !!!! \nNombre: {contact.name} \nTelefono: {contact.cellphone} \nEmail: {contact.email}")
                    return contact
            flash ("El contacto no existe")
            return None
        else:
            flash("Directorio de contactos vacio...")
            return None
    
    @classmethod
    def show_all (cls):
        if len(cls.list) > 0:
            for contact in cls.list:
                flash(f"\nNombre: {contact.name} \nTelefono: {contact.cellphone} \nEmail: {contact.email}")
        else:
            flash("Directorio de contactos vacio...")

    def edit_contact(self, field, new_value):
        if field == 'name':
            self.name = new_value
        elif field == 'cellphone':
            self.cellphone = new_value
        elif field == 'email':
            self.email = new_value
        print(f"El contacto ha sido actualizado: \nNombre: {self.name} \nTelefono: {self.cellphone} \nEmail: {self.email}")
            
contact = Contacts ()

