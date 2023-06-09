#!/usr/bin/python3

#flask stuff
from flask import Blueprint, request,jsonify, render_template, flash, redirect, url_for

#custom-form class
from forms import ContactForm

from localutils import getUsername

#custom config definitions
from config import Config

from email_sendinblue import sendEmail

#ui-form route
contactusui = Blueprint('contactusui', __name__)

#variables
httpRCok=200
httpRCbad=400
httpRCsvr=500

devopscontact=Config.devopscontact

#Contact Form
@contactusui.route('/', methods=['GET', 'POST'])
def uiform():
    username = getUsername()

    form = ContactForm()
    formOutput = {}
    if form.validate_on_submit():
        #form-input
        name_sub = form.name.data
        senderemail_sub = form.senderemail.data
        message_sub = form.message.data

        #app-config
        emailsubject = "Flask App"
        recipientname = "VN"
        recipientemail = "kans.vignesh@gmail.com"

        sendEmailRC = sendEmail(emailsubject, senderemail_sub, recipientemail, recipientname, message_sub)
        if (sendEmailRC):
          contactusOutput = "Message sending success. Thank you."
        else:
          contactusOutput = "Sorry, message sending failed. Please try again later. Thank you."

        #return redirect(url_for('home'))
        return render_template('contactus.html', title='Get in touch', user=username, form=form, output=contactusOutput)

    return render_template('contactus.html', title='Get in touch', user=username, form=form)
