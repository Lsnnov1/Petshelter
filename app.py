from flask import Flask, request, session, render_template, redirect
from models import connect_db, db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "adoptapet"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_shelter_db"
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()
connect_db(app)
db.create_all()

@app.route("/petshelter", methods=["GET"])
def show_pets():
    pets = Pet.query.all()
    return render_template("petshelter.html", pets=pets)


@app.route("/petshelter/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        newpet = Pet(name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data)
        db.session.add(newpet)
        db.session.commit()
        return redirect("/petshelter")
    else:
        return render_template("add_pet_form.html", form=form)

@app.route("/petshelter/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data or None
        pet.age = form.age.data or None
        pet.notes = form.notes.data or None
        pet.available = form.available.data
        
        db.session.commit()
        return redirect('/petshelter')
    
    return render_template("edit_pet_form.html", form=form, pet=pet)
