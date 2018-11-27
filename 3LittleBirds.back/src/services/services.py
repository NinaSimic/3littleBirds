'''
Created on Nov 27, 2018

@author: Petar
'''
'''
    register user
'''

from flask.globals import request
from flask.helpers import send_file, make_response
from flask_jsonpify import jsonify
from flask_restful import Resource
import qrcode

from main.myapp import app


@app.route( '/register', methods = [ 'POST' ] )
@app.validate( 'user', 'register' )
def registerUser():
    data = request.get_json(True)
        
    print data["username"]
        
    
'''
   get user details
'''
@app.route( '/user', methods = [ 'GET' ] )
def getUser():
    return jsonify({"name":"Petar Bjeljac", "email":"petar.bjeljac@gmail.com"})
    
'''
    askForHelp
'''
@app.route( '/help', methods = [ 'POST' ] )
@app.validate( 'user', 'details' )
def askHelp():
    pass

'''
    help details
'''
@app.route( '/helpDetails/<id>', methods = [ 'GET' ] )
def helpDetails(id):
    return jsonify({"name":"Melinda","location":"Haiti","target":20000,"collected":1500})

'''
    get affected regions
'''
@app.route( '/regions', methods = [ 'GET' ] )
def affectedRegions():
    return jsonify(["Haiti","Surinam","Port\'O\'Prence"])

@app.route( '/qrCode/<id>', methods = [ 'GET' ] )
def generateQR(id):
    img = qrcode.make('Some data here')
    
