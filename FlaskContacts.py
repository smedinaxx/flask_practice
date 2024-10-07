#09 ☎️ Contact Book
# Crea una libreta de contactos que:
# - ✅ Mantenga una lista de contactos
# - ✅ Permita agregar nuevos contactos (nombre, teléfono, email)
# - Permita buscar contactos por nombre
# - Muestre todos los contactos
# - Permita editar la información de los contactos existentes
# - Implemente una función para exportar los contactos a un archivo CSV

from flask import Flask, render_template, redirect, url_for, flash, request
app = Flask (__name__)
app.secret_key = 'kkroto'

#modelo contactos
class Contacts:
    list = []
    
    def __init__(self, name, cellphone, email):
        self.name = name
        self.cellphone = cellphone
        self.email = email
        Contacts.list.append (self)
    
    @classmethod
    def search (cls, name):
        if len(cls.list) > 0:
            for contact in cls.list:
                if contact.name == name:
                    flash('Contacto encontrado !!!!')
                    flash(f'Nombre: {contact.name}')
                    flash(f'Telefono: {contact.cellphone}')
                    flash(f'Email: {contact.email}')
                    
                    return contact
            flash ('El contacto no existe')
            return None
        else:
            flash('Directorio de contactos vacio...')
            return None
    
    @classmethod
    def show_all (cls):
        if len(cls.list) > 0:
            for contact in cls.list:
                flash(f'<br>Nombre: {contact.name} <br>Telefono: {contact.cellphone} <br>Email: {contact.email}')
        else:
            flash('Directorio de contactos vacio...')

    def edit_contact(self, field, new_value):
        if field == 'name':
            self.name = new_value
        elif field == 'cellphone':
            self.cellphone = new_value
        elif field == 'email':
            self.email = new_value
        flash(f'El contacto ha sido actualizado: <br>Nombre: {self.name} <br>Telefono: {self.cellphone} <br>Email: {self.email}')
            
@app.route ('/')
def index ():
    return render_template('index.html')

@app.route('/add_contact', methods=['GET','POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        cellphone = request.form['cellphone']
        email = request.form['email']
        
        Contacts(name, cellphone, email)
        flash (f'Contacto {name} añadido correctamente!!!')
        return redirect(url_for('index'))
    
    return render_template('add_contact.html')

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method=='POST':
        name = request.form['name']
        Contacts.search(name)
        return redirect(url_for('index'))
    return render_template('search_contacts.html')

if __name__ == '__main__':
    app.run(debug=True)