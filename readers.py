#input data
import pandas as pd
from packet import Packet



class CsvPacketReader:
    @staticmethod
    def read(path):
        df = pd.read_csv(path)
        packets = []
        
        for _, raw in df.iterrows():
            data = raw.to_dict()
            packet = Packet(data)
            packets.append(packet)
        return packets