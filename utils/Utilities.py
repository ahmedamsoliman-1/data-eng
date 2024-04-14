import logging 
import sys
import psutil
import socket
import requests
from datetime import datetime
import getpass
class LogFormatter(logging.Formatter):
    
    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;11m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'
    green = '\x1b[38;5;40m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            25: self.green + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, msg):
        log = self.FORMATS.get(msg.levelno)
        formatter = logging.Formatter(log)
        return formatter.format(msg)


class StreamLogger():
    
    def __init__(self) -> None:
        format = f"%(asctime)s | %(levelname)8s | %(message)s"
        stream_handler = logging.StreamHandler(sys.stdout)
        
        # Use the updated LogFormatter class
        stream_handler.setFormatter(LogFormatter(format))
        
        logging.basicConfig(format=format, handlers=[stream_handler])
        
        # Add the "green" (INFO) log level and assign it the word "info"
        logging.addLevelName(logging.INFO, "INFO")
        
        # Add the "SYSTEM" log level as you did before
        logging.addLevelName(25, "SYSTEM")
        
        logging.system = self.system
        logging.Logger.system = self.system
        self.stream_logger = logging.getLogger(name="CS2 Stream Logger")
        
        # Set the log level for "info" (green) logs
        self.stream_logger.setLevel(logging.INFO)
        
    def system(self, msg, *args, **kwargs):
        if logging.getLogger(name="CS2 Stream Logger").isEnabledFor(25):
            logging.getLogger(name="CS2 Stream Logger").log(25, msg)

class SystemMonitor():
    def __init__(self):
        pass

    def get_system_info(self):
        memory = psutil.virtual_memory()
        cpu_percent = psutil.cpu_percent(interval=1)
        disk_usage = psutil.disk_usage('/')

        system_name = socket.gethostname()
        private_ip = socket.gethostbyname(system_name)
        public_ip = self.get_public_ip()
        network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        username = getpass.getuser() 

        return {
            'timestamp': timestamp,
            'system_name': system_name,
            'private_ip': private_ip,
            'public_ip': public_ip,
            'memory_percent': memory.percent,
            'cpu_percent': cpu_percent,
            'disk_percent': disk_usage.percent,
            'network_usage': network_usage,
            'username': username 
        }

    def get_public_ip(self):
        response = requests.get("https://api64.ipify.org?format=json")
        return response.json()["ip"]


if __name__ == '__main__':
    stream_logger = StreamLogger()
    monitor = SystemMonitor()
    stream_logger.stream_logger.system(monitor.get_system_info())