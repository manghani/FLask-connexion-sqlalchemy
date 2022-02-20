from flask import Flask, render_template, request, redirect
import connexion
from model import db,Person

# app = connexion.App(__name__, specification_dir='./')
# app.add_api('swagger.yml')
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        Type = request.form['Type']
        age = request.form['age']
        description = request.form['description']
        date = request.form['date']
        person = Person(id=id, name=name, Type=Type, age = age, description=description, date=date)
        db.session.add(person)
        db.session.commit()
        return redirect('/data')
 
 
@app.route('/data')
def RetrieveList():
    persons = Person.query.all()
    return render_template('datalist.html', persons=persons)
 
 
@app.route('/data/<int:id>')
def RetrievePerson(id):
    Person = Person.query.filter_by(id=id).first()
    if Person:
        return render_template('data.html', Person = Person)
    return f"Person with id ={id} Doenst exist"
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    Person = Person.query.filter_by(id=id).first()
    if request.method == 'POST':
        if Person:
            db.session.delete(Person)
            db.session.commit()
            name = request.form['name']
            Type = request.form['Type']
            age = request.form['age']
            description = request.form['description']
            date = request.form['date']
            Person = Person(id=id, name=name, Type=Type, age=age, description=description, date=date)
            db.session.add(Person)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Person with id = {id} Does nit exist"
 
    return render_template('update.html', Person = Person)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    Person = Person.query.filter_by(id=id).first()
    if request.method == 'POST':
        if Person:
            db.session.delete(Person)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
