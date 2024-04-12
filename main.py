from utils import StreamLogger

stream_logger = StreamLogger()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    stream_logger.stream_logger.warning(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')