# raw CSV → internal schema
FIELD_MAPPING = {
    "packet_id": "packet_id",
    "timestamp": "timestamp",
    "source ip": "src_ip",
    "destination ip": "dst_ip",
    "protocol": "protocol",
    "source port": "src_port",
    "destination port": "dst_port",
    "length": "length"
}

REQUIRED_FIELDS = {
    "packet_id",
    "timestamp",
    "src_ip",
    "dst_ip",
    "protocol",
    "src_port",
    "dst_port",
    "length"
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




def parse_packet_row(raw_row):
    # 1. rename fields
    data = map_fields(raw_row)
    
    # 2. validate required fields
    validate_required_fields(data)
    
    # 3. normalize values
    data["protocol"] = validate_protocol(data["protocol"])
    ***************************************************************
    # 4. convert types
    data["packet_id"] = parse_int(data["packet_id"], "packet_id")
    data["src_port"] = parse_int(data["src_port"], "src_port")
    data["dst_port"] = parse_int(data["dst_port"], "dst_port")
    data["length"] = parse_int(data["length"], "length")
    data["timestamp"] = parse_timestamp(data["timestamp"])
    data["src_ip"] = parse_ip(data["src_ip"],"src_ip")
    data["dst_ip"] = parse_ip(data["dst_ip"],"dst_ip")
    
    # 5. (optional) extra validation
    if data["length"] < 0:
        raise ValueError("Packet length cannot be negative")
    
    return data

def map_field(raw):
    mapped = {}
    for raw_key, internal_key in FIELD_MAPPING.items():
        if raw_key in raw:
            mapped[internal_key]=raw[raw_key]
    return mapped


def validate_required_fields(data):
    missing = []
    for item in REQUIRED_FIELDS:
        if not item in data:
            missing.append(item)
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

  
    
def validate_protocol(protocol):
    
    if isinstance(protocol, str):
        if protocol.strip().upper() in VALID_PROTOCOLS:
            return protocol.strip().upper()
        raise ValueError("Invalid protocol")
    raise TypeError("Protocol must be a string")