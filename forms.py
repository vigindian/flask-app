#!/usr/bin/python3

#forms
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, RadioField
#from wtforms.fields.html5 import DateTimeLocalField #deprecated
from wtforms.fields import DateTimeLocalField
from wtforms.validators import DataRequired, ValidationError

import datetime
import re

#sample form fields
class SampleForm(FlaskForm):
    type1 = RadioField(u'Type', choices=[('data1', 'Type1'), ('data2', 'Type2')], widget=None)
    environment = RadioField(u'Environment', choices=[('test', 'Test'), ('staging', 'Staging'),('production', 'Production')], widget=None)
    dataid = IntegerField('ID', validators=[DataRequired()])
    From = DateTimeLocalField('From', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    To = DateTimeLocalField('To', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    status = BooleanField('Status')
    submit = SubmitField('Submit')

    #ensure to is greater than from and set max-allowed time-range
    def validate_To(form, field):
        #to-date should be greater than from-date
        if field.data < form.From.data:
            #print("To date must not be earlier than From date.")
            raise ValidationError("To date must not be earlier than From date")

        #do not allow time-range greater than 2-weeks
        datetimefrom_secs = datetime.datetime.timestamp(form.From.data)
        datetimeto_secs = datetime.datetime.timestamp(form.To.data)
        given_range = datetimeto_secs - datetimefrom_secs
        #print(given_range)

        maxallowedrange_secs = 1209600 #2-weeks in secs
        if given_range > maxallowedrange_secs:
            print("Please choose a shorter time-range, less than 2-weeks")
            raise ValidationError("Please choose a shorter time-range, less than 2-weeks. Thanks.")

    #do not allow date older than 13-months, as it is archived
    def validate_From(form, field):
        datetimefrom_secs = datetime.datetime.timestamp(field.data)
        
        now = datetime.datetime.now()
        thisday_secs = datetime.datetime.timestamp(now)
       
        nowtofrom_secs = thisday_secs - datetimefrom_secs

        earliest_time_secs = 34300800 #13-months ~ 397-days in secs
        if nowtofrom_secs > earliest_time_secs:
            print("Please choose a date within 13-months")
            raise ValidationError("Please choose a date within 13-months. Thanks.")

    def validate_status(form, field):
        print("Status: " +str(field.data) + ", type1: "+str(form.type1.data))
        if field.data and form.type1.data == "data2":
            print("Status is not applicable for data type-2")
            raise ValidationError("Status is not applicable for data type-2")

#######################################

#WeatherForm
class WeatherForm(FlaskForm): 
    city = StringField("City: ", validators=[DataRequired()], render_kw={"placeholder": "City Name"})
    submit = SubmitField('Submit')

    #check if input is string
    def validate_city(form, field):
        invalidchars = re.search(r'[@_!#$%^&*()<>?/\|}{~:\d\.]', field.data) #special characters, numbers, and dot
        if (invalidchars):
            print("Please input city name in string format")
            raise ValidationError("Please input city name in string format")

#######################################

#ContactForm
class ContactForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()], render_kw={"placeholder": "Your Name"})
    senderemail = StringField("Email: ", validators=[DataRequired()], render_kw={"placeholder": "jdoe@gmail.com"})
    message = StringField("Message: ", validators=[DataRequired()])
    submit = SubmitField('Submit')

    #check if input is string
    def validate_name(form, field):
        invalidchars = re.search(r'[@_!#$%^&*()<>?/\|}{~:\d\.]', field.data) #special characters, numbers, and dot
        if (invalidchars):
            print("Please input name in string format")
            raise ValidationError("Please input name in string format")

    #check if input is in email-format
    def validate_senderemail(form, field):
        validregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (not re.fullmatch(validregex, field.data)):
            print("Invalid email address")
            raise ValidationError("Invalid email address")
#######################################
