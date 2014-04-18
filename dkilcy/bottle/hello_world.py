#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Apr 17, 2014

@author: dkilcy
'''
import bottle

@bottle.route('/')
def home_page():
    #return "<html><title>Home Page</title><body><h3>Hello World</h3></body></html>"
    mythings = ["apple","orange","banana","peach"]
    return bottle.template("hello_world", {"username":"dkilcy", "things":mythings } )

@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit"); 
    if( fruit == None or fruit == "" ):
        fruit="No fruit selected"
        
    #return bottle.template("fruit_selection", { "fruit": fruit })
    bottle.response.set_cookie("fruit", fruit)
    bottle.redirect('/show_fruit')

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")
    return bottle.template("fruit_selection", { "fruit":fruit })

@bottle.route('testpage')
def test_page():
    return "Test Page"

bottle.debug()
bottle.run(host='localhost', port=8002)

