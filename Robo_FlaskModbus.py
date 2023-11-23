#This software is initial sample software of flask modbus commn. between master ERP and server robot
#Rpi connected to robot as a maste via flask and modbus we can read datas from ERP
#ERP readdata order----> RaspPi Flask----->Robot Modbus
#it has not tested yes

from pyModbusTCP.client import ModbusClient
from flask import Flask,request,redirect,url_for
from flask import jsonify
import requests, json
import threading
import time

#************************************************************************************
client = ModbusClient(host="192.168.3.11", auto_open=True, auto_close=True)
#***********************************************************************************


app=Flask(__name__) #--This Flask is just a extention liblary for python for making webserver application via raspberry pi
app.config['JSON_SORT_KEYS'] = False
   
@app.route('hello') 
def hello_world():
    return jsonify(result="Hey, It is a flask test")

###########################################################################################################

@app.route('/readdata') #--it is just for test and not necessary for normal pin LEDs working conditions
def readdata():
    global regs, coils_1, coils_2, coils_3, coils_4
    coils_l = client.read_coils(0, 10)
    #this section could be unsuccesfulll
    # if success display registers
    if coils_l:
        print('coil ad #0 to 9: %s' % coils_l)
    else:
        print('unable to read coils')

########################################
    coils_2 = client.read_coils(10, 49)
#this section is new
    # if success display registers
    if coils_2:
        print('coil ad #0 to 49: %s' % coils_2)
    else:
        print('unable to read coils2readcoilsimple')
#########################################
    coils_3 = client.read_discrete_inputs(10, 49)
#this section is new
    # if success display registers
    if coils_3:
        print(coils_3)
    else:
        print('unable to read coils3readdisc.input')
########################################

    coils_4 = client.read_input_registers(10, 49)
#this section is new
    # if success display registers
    if coils_4:
        print(coils_4)
    else:
        print('unable to read coil4readinputdegister')
    client.close()
    return jsonify(result="Hey, It is a data read flask test")



#app.run(debug=False,host='192.168.178.139',port='1080') #Intializing
app.run(debug=False,host='192.168.3.2',port='5000') #test

#maybe UDP could be better    