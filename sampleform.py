#!/usr/bin/python3

#flask stuff
from flask import Blueprint, request,jsonify, render_template, flash, redirect, url_for, Markup

#return output in json
import json

#custom-form class
from forms import SampleForm

#custom config definitions
from config import Config

from localutils import getUsername

#ui-form route
sampleformui = Blueprint('sampleformui', __name__)

#variables
httpRCok=200
httpRCbad=400
httpRCsvr=500

devopscontact=Config.devopscontact

@sampleformui.route('/', methods=['GET', 'POST'])
def uiform():
    username = getUsername()

    form = SampleForm()
    formOutput = {}
    if form.validate_on_submit():
        pstype_sub = form.type1.data
        environment_sub = form.environment.data
        dataid_sub = form.dataid.data
        datafrom_sub = form.From.data
        datato_sub = form.To.data
        status_sub = form.status.data

        print('Data requested for environment {}, with id={}, from={}, to={}, hd-data={}'.format(
            environment_sub, dataid_sub, datafrom_sub, datato_sub, status_sub))

        formOutput["pstype"] = pstype_sub
        formOutput["environment"] = environment_sub
        formOutput["dataid"] = dataid_sub
        formOutput["datafrom"] = datafrom_sub
        formOutput["datato"] = datato_sub 
        formOutput["status"] = status_sub 

        #return redirect(url_for('home'))
        return render_template('sampleform.html', title='Sample Form', user=username, form=form, output=formOutput)

    return render_template('sampleform.html', title='Sample Form', user=username, form=form)
