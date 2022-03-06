from TableReader import TableReader

table_reader = TableReader()
cards = table_reader.get_table_state()
table_reader.stop_video_stream()

def make_cluster(cards):
    CLUSTER_THRESHOLD = 100
    pass
