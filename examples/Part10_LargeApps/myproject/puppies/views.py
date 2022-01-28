from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Pup
from myproject.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint('puppies', __name__,
                              template_folder='templates/puppies')


@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data
        pup = Pup(name)
        db.session.add(pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('add.html', form=form)


@puppies_blueprint.route('/list')
def list():

    pups = Pup.query.all()

    return render_template('list.html', pups=pups)


@puppies_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():

        puppy_id = form.id.data
        pup_remove = Pup.query.get(puppy_id)

        db.session.delete(pup_remove)
        db.session.commit()
        print("It should be done")

        return redirect(url_for('puppies.list'))

    return render_template('delete.html', form=form)
