#!/usr/bin/python3

from flask import request

def getUsername():
    #sample user
    testRemoteUser = "testuser1"
    request.environ['REMOTE_USER'] = testRemoteUser #set value to sample-user

    userName = request.environ.get('REMOTE_USER') #retrieve from request.environ. eg: apache can set this env-value and pass it to flask-app via WSGI
    return userName
