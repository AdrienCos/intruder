# Database information
db_path = "postgresql://pi:password@hub.local/sentinel"

# Network
node_addr: str = '130.203.33.155'
node_port: int = 50500
node_iface: str = "wlan0"

# MQTT information
broker_addr: str = "hub.local"
broker_port: int = 8883
cafile: str = "/certs/CA.pem"
certfile: str = "/certs/node.crt"
keyfile: str = "/certs/node.key"
topic_prefix: str = "intruder/"

# Attack types
PIVOT_NMAP = 0
EXFILTRATION = 1
BLACK_HOLE = 2
GREY_HOLE = 3
C2_HEARTBEAT = 4

# Attack parameters
pivot_addr = "ether.cosson.io"
exfil_addr = "ether.cosson.io"
exfil_port_min = 10000
exfil_port_max = 60000
black_hole_src = "google.com"
black_hole_dest = 'ether.cosson.io'
black_hole_port = 12345
c2_addr = "ether.cosson.io"
c2_port = 4567
