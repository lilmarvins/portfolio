import requests,random,string,os,json
from functools import wraps
from flask import render_template,request,session,redirect,flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_mail import Mail,Message


from pkg import Message
from pkg import app

mail= Mail()
@app.route("/")
def user_home():
    return render_template("user/index.html",title="Marvins Profile")





@app.route('/sendmail/',methods=['POST',"GET"])
def sendmail():
        name = request.form.get('name')
        email = request.form.get('email')
        content = request.form.get('message')
        # we have received email on the website and have written it to file/db and we now want to acknowledge the emailto the person who filled the form
        sender= ('marvns Portolio','admin@devfest.com')
        subject = 'message from marvins portfolio'
        msg =Message(subject=subject,sender=sender, recipients=[email]) 
        mymessage =Message(subject=subject,sender=sender, recipients=['enujekormarvellous@gmail.com']) 
        mymessage.html= f"a message was sent from {name} through the website which is: {content}"
        msg.html=f"thank you {name} your message was recieved as folows:{content} <img src='https://cdn.pixabay.com/photo/2024/04/25/06/50/banana-8719086_1280.jpg'>"
        mail.send(msg) # import mail from dev app
        mail.send(mymessage)
        flash("your message has been sent sccessfully you will receive a mail with your message", category="success")
        return redirect('/')

   