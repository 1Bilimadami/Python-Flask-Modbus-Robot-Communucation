# Import the library
# pip install --user pymodbus
#pip show pymodbus
#pip install --user pyModbusTCP

#https://pypi.org/project/pyModbusTCP/
#https://pymodbustcp.readthedocs.io/en/latest/
#https://pymodbustcp.readthedocs.io/en/latest/examples/client_read_coils.html

from pyModbusTCP.client import ModbusClient
# Create a TCP client object with auto_open option enabled
client = ModbusClient(host="192.168.3.11", auto_open=True, auto_close=True)
# Connect to the server automatically on first modbus request
#######client.connect()


# Send or receive data using methods like write_multiple_registers, read_holding_registers, etc.
result = client.read_holding_registers(0,2)# Read two holding registers from address 0

if result:
    print(result)
# Print the register values
# Close the connection automatically after each modbus request
###


regs = client.read_holding_registers(0, 99)###### between 0 and 20th registers reading from gantry

if regs:
    print(regs) #here writing [0 0]  i guess coordinates
else:
    print("read error")

###

#if client.write_multiple_registers(10, [44,55]): #10th 11th registra 44 and 55 value writing
#    print("write okzz")
#else:
#    print("write error")
############################################
#####if client.write_multiple_registers(10, [44,55]):
#####    print("write okaaay")
#########################
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