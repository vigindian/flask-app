#!/usr/bin/python3

#flask stuff
from flask import Blueprint, request,jsonify, render_template, flash, redirect, url_for, Markup

#weather-api-calls
import requests

#return output in json
import json

#custom config definitions
from config import Config

#custom-form class
from forms import WeatherForm

from getweather import getWeather

from localutils import getUsername

#ui-form route
weatherui = Blueprint('weatherui', __name__)

#variables
httpRCok=200
httpRCbad=400
httpRCsvr=500

devopscontact=Config.devopscontact

#Weather UI
@weatherui.route('/', methods=['GET', 'POST'])
def uiform():
    username = getUsername()

    form=WeatherForm()
    if form.validate_on_submit():
        city_sub = form.city.data

        #flash('Weather data requested for city {}'.format(city_sub))
        print('Weather data requested for city {}'.format(
            city_sub))


        weatherOutput = getWeather(city_sub)

        #flash(weatherOutput)
        #return redirect(url_for('home'))
        if weatherOutput:
          return render_template('weatherform.html', title='Weather', user=username, form=form, output=weatherOutput)
        else:
          return render_template('weatherform.html', title='Weather', user=username, form=form, output="No data found")

    return render_template('weatherform.html', title='Weather', user=username, form=form)
