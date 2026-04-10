#data structure fo packets
#attributes for now: src_ip, dst_ip, src_port, dst_port, protocol
from datetime import datetime


TCP_SERVICES = {
                80: "HTTP",
                443: "HTTPS",
                22: "SSH",
                21: "FTP",
                25: "SMTP",
                110: "POP3",
                143: "IMAP"
            }

UDP_SERVICES = {
                53: "DNS"
            }

SENSITIVE_PORTS = {
    22,     # SSH
    23,     # Telnet (very insecure)
    21,     # FTP
    25,     # SMTP
    3389,   # RDP
    445     # SMB (very attacked)
}

VALID_PROTOCOLS = {
    "TCP", "UDP", "ICMP",
    "HTTP", "HTTPS",
    "DNS",
    "FTP",
    "SMTP",
    "POP3",
    "IMAP",
    "SSH",
    "TELNET"
}

LENGTH_THRESHOLD = 1500





class Packet:
    def __init__(self, data):
        self.packet_id = data["packet_id"]
        self.timestamp = data["timestamp"]
        self.src_ip = data["src_ip"]
        self.dst_ip = data["dst_ip"]
        self.protocol = data["protocol"]
        self.src_port = data["src_port"]
        self.dst_port = data["dst_port"]
        self.length = data["length"]
      
      
        
    def __str__(self):
        return f"ID: {self.packet_id} | {self.src_ip}/{self.src_port} → {self.dst_ip}/{self.dst_port} | {self.protocol} | {self.length} bytes"
         
        
    def to_dict(self):
        return {
            "packet_id":self.packet_id,
            "timestamp": self.timestamp,
            "src_ip": self.src_ip,
            "dst_ip": self.dst_ip,
            "protocol": self.protocol,
            "src_port":self.src_port,
            "dst_port": self.dst_port,
            "length": self.length
        }
        
        
        
    def classify(self):
        
        if self.protocol == "ICMP":
            return "ICMP"
        
        if self.protocol == "TCP":
            return TCP_SERVICES.get(self.dst_port, "OTHER")
        
        if self.protocol == "UDP":
            return UDP_SERVICES.get(self.dst_port, "OTHER")
        
        return "OTHER"
    
    
    
    def suspicious_reasons(self):
        reasons = []
        
        if self.length > LENGTH_THRESHOLD:
            reasons.append("Large Packet")
            
        if self.dst_port in SENSITIVE_PORTS:
            reasons.append("Sensitive Port")
        
        if self.protocol not in VALID_PROTOCOLS:
            reasons.append("Unknown Protocol")
        
        '''"missing_src_ip"
            "missing_dst_ip"
            "invalid_port"'''
        
        return reasons
    
    
    def is_suspicious(self):
        return len(self.suspicious_reasons()) > 0

        
                