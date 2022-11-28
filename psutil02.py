import psutil

network_stats = psutil.net_io_counters(pernic=False)
bytes_sent = getattr(network_stats, 'bytes_sent')
bytes_recv = getattr(network_stats, 'bytes_recv')

print ("Bytes sent = {0} | Bytes Received = {1}".format(bytes_sent, bytes_recv))