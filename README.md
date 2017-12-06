[![PyPI](https://img.shields.io/badge/pypi-v0.1-blue.svg)](https://pypi.python.org/pypi/pvyos/0.1)

# pvyos
"Pvyos" is a combination of "python" and "vyos". Pvyos is a simple library build on pexpect to connect and configure Vyos OS.

Python 3.5.2

#### Requires:
pexpect >= 4.2.1+

#### Support:
- Routing (Static,RIP,OSPF)
- System (User,Hostname)
- Service (SSH,Telnet,DNS)
- Interface (Ethernet, Loopback)

# Instalation
```
pip3 install pvyos
```

# Example

##### Create Session
```
import pvyos

device = pvyos.routing("192.168.1.10","vyos","vyos")
device.telnet_connection()
device.static("99.99.99.0","24","192.168.1.2")
device.commit()
device.closecon()
```
