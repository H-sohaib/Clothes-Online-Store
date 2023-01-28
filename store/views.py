from store import app, db, bcrypt
from store.forms import RegistreForm, LoginForm
from flask import render_template, redirect, flash, url_for, request
from store.Models import User, Product
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistreForm()
    if current_user.is_authenticated:
        return redirect('/')
    if (form.validate_on_submit()):
        # store in db
        hashed_pswd = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_pswd)
        db.session.add(user)
        db.session.commit()
        # send a flash message for notificate create a accountw
        flash(f' Account created for {form.username.data} ', 'success')
        return redirect('/')
    return render_template("register.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect('/')
    if (form.validate_on_submit()):
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.rememberme.data)
            flash('You have been logged in!', 'success')
            return redirect('/')
        else:
            flash('Login Unsuccessful', 'danger')

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect('/')


@app.route("/jackets", methods=["POST", "GET"])
@login_required
def jackets():
    if request.method == "POST":
        card_id = request.form["id"]
        card = Product.query.filter_by(id=card_id).first()
        card.quantity = card.quantity - 1
        db.session.commit()
        print("updated card")
        print(card.quantity)

    jacket = Product.query.filter_by(clothes_type='jackets').all()
    return render_template('product.html', jacket=jacket, cloth_type="Jackets")
