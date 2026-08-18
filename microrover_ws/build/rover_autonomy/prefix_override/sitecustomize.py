import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kwasi/Autonomous_MicroRover_ROS/microrover_ws/install/rover_autonomy'
