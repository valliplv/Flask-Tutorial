from flask import Flask
from flask import make_response,request ,redirect,url_for ,flash #for cookies #for URL redirect
from flask import render_template #for including the html templates
from .forms import LoginForm  #we have imported LoginForm from form.py
from app import app


#Template rendering , inheritance
@app.route('/') # default URL
def start():
    #return "<h1>Hello Welcome to my flask application</h1>" #here we have embedded the html contents
    name = "VALLI" #passing values to the render template html file
    return render_template('start.html',name = name)

#Template inheritance
@app.route('/contact')
def contact():
    con_details = {
        'address' : 'Trichy',
        'phone' : '12456778'
    }
    return render_template('contact.html',con_details = con_details) # here con_details is context variable


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/content') #URL with customized naming
def content():
    return "<h2> We are going to learn about various flask concepts </h2>"


@app.route('/User/<name>/<int:age>') #Dynamic URL binding
def user_details(name,age):
    return """<h3>Hello welcome to my channel {0} <br>
              Your age is {1}
            <h3> """.format(name,age)

#Flask Cookies
@app.route('/set')
def setCookie():
    response = make_response("I have set the cookie")
    response.set_cookie("myappcookie" ,"Flask web development Cookie")
    return response

@app.route('/get')
def getCookie():
    myapp = request.cookies.get("myappcookie")
    return "This is your cookie {}" .format(str(myapp))

#error handilng
@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html')


@app.route('/login' ,methods = ['GET','POST'])
def Login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     return redirect(url_for('start')) #start refers to the view function name
    if form.validate_on_submit():
        if request.form['username'] != 'valli' or request.form['password'] != 'Valli':
            flash("Invalid username or credentials") #these flash needs to be shown in the appropriate html page
        else:
            return redirect(url_for('start'))
    
    return render_template('login.html',title = 'Login', form = form)#during the first call always the else part only takes place since we dont have any data to be submitted


@app.errorhandler(500)
def pageNotFound(error):
    return render_template('500.html')
