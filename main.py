from capture import PacketCapture


df = PacketCapture("./data/sample.csv")
print(df.ptl_count())
#print(df)