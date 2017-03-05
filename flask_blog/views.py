from flask_blog import app
from flask import render_template,flash,redirect
from forms import LoginForm
@app.route('/hello')
def home():
    return 'hello world!'
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Migule'}
    post_data = [
        {
            'author':{'nickname':'John'},
            'body':'Beautiful day in Portland.'
        },
        {
            'author':{'nickname':'Susan'},
            'body':'The Avengers movie was so cool.'
        }
    ]
    return render_template('index.html', title ='Home', user=user, posts=post_data)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requst for name:'+ form.name.data)
        flash('password:' + str(form.password.data))
        flash('remember_me' + str(form.remember_me.data))
        return redirect('/index')
    return render_template("login.html", title='Sign in',form=form)
