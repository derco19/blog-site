import math
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail
from datetime import datetime
import os
from werkzeug.utils import secure_filename

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True

app = Flask(__name__)
app.secret_key = 'secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password'],
)
mail = Mail(app)

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contactsdata(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phno = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(240), nullable=False)


class Blogsdata(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    subtitle = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(240), nullable=False)
    date = db.Column(db.String(40))
    img = db.Column(db.String(20), nullable=True)


@app.route('/')
def home():
    posts = Blogsdata.query.filter_by().all()
    # [0:params['no_of_post']]
    posts = posts[1:len(posts)]
    last = math.ceil(len(posts) / int(params['no_of_post']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1

    page = int(page)
    posts = posts[(page - 1) * (int)(params['no_of_post']):(page) * (int)(params['no_of_post'])]

    if page == 1:
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif page == last:
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)


@app.route("/post/<string:post_slug>", methods=['GET'])
def postslug(post_slug):
    post = Blogsdata.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin-user']):
        post = Blogsdata.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dashboard')


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin-user']):

        if request.method == 'POST':
            box_title = request.form.get('title')
            box_subtitle = request.form.get('subtitle')
            box_slug = request.form.get('subtitle')
            box_content = request.form.get('content')
            box_img = request.form.get('img')
            date = datetime.now()

            if sno == '0':
                post = Blogsdata(title=box_title,
                                 subtitle=box_subtitle,
                                 slug=box_slug,
                                 content=box_content,
                                 date=date,
                                 img=box_img)

                db.session.add(post)
                db.session.commit()
                return redirect('/dashboard')

            else:
                post = Blogsdata.query.filter_by(sno=sno).first()
                post.title = box_title
                post.subtitle = box_subtitle
                post.slug = box_slug
                post.content = box_content
                post.img = box_img
                db.session.commit()
                return redirect('/edit/' + sno)
        post = Blogsdata.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post)


@app.route('/about')
def about():
    return render_template('about.html', params=params)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'user' in session and session['user'] == params['admin-user']:
        session.pop('user')
        return redirect('/dashboard')


@app.route('/dashboard', methods=['GET', 'POST'])
def login():
    posts = Blogsdata.query.all()
    c=0
    for post in posts:
        post.sno = c
        c = c + 1
        db.session.commit()
    posts = posts[1:len(posts)]




    if 'user' in session and session['user'] == params['admin-user']:
        return render_template('dashboard.html', params=params, posts=posts)

    if (request.method == 'POST'):
        uname = request.form.get('uname')
        upass = request.form.get('upass')
        if (uname == params['admin-user'] and upass == params['admin-password']):
            session['user'] = uname
            return render_template('dashboard.html', params=params, posts=posts)
        else:
            return render_template('login.html', params=params)
    else:
        return render_template('login.html', params=params)


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin-user']):
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                secure_filename(f.filename)))
            params['upload'] = "true"
            return redirect('/dashboard')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        db.session.add(Contactsdata(name=name, email=email, phno=phone, message=message))
        db.session.commit()
        mail.send_message('New Message from ' + name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message + '\n\nPhone No:' + phone + '\nEmail: ' + email)

    return render_template('contact.html', params=params)


app.run(debug=True)
