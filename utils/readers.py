#input data
import pandas as pd
from models.packet import Packet



class CsvPacketReader:
    @staticmethod
    def read(path):
        try:
            df = pd.read_csv(path)
            packets = []
            
            for _, raw in df.iterrows():
                data = raw.to_dict()
                packet = Packet(data)
                packets.append(packet)
            return packets
        except KeyError as e:
            raise ValueError(
                "Invalid CSV format. Expected headers: "
                "packet_id,timestamp,source ip,destination ip,protocol,source port,destination port,length"
            ) from e
            