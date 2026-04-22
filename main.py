from models.capture import PacketCapture
import models.packet as packet
from analysis.visualizer import Visualizer
from utils.readers import CsvPacketReader
from analysis.analyzer import PacketAnalyzer
from models.flow import Flow

packets = CsvPacketReader.read("./data/sample2.csv")
capture = PacketCapture(packets)
top10=PacketAnalyzer.top_talkers(capture)
#print(dict(top10))
#print(Visualizer.format_result(dict(top10)))
##print(Visualizer.format_result(PacketAnalyzer.protocol_count(capture)))
#print(capture.to_dataframe())
vis = Visualizer()
#print(vis.format_result(df.top_talkers(by = "bytes")))
#vis.plot_packet_size_hist(df.get_packet_lengths())
flows = Flow.build_flows(capture)
#print(PacketAnalyzer.longest_flow(flows))
print(PacketAnalyzer.top_flows(flows,sort_item="packets"))
print(f"average packet size in flow = {flows[0].average_packet_size}")