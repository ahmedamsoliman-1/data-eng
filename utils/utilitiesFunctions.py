from .Utilities import StreamLogger
import yaml

stream_logger = StreamLogger()

def read_local_credentials(config_file='_credentials.yaml'):
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
            host = config['es_1']['host']
            port = config['es_1']['port']
            stream_logger.stream_logger.info({"host": host, "port": port, })
            return {
                "host": host,
                "port": port,
            }
        
    except Exception as e:
        stream_logger.stream_logger.error(f"Error reading RabbitMQ credentials: {e}")
        return {} 
