from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import threading
import paho.mqtt.client as mqtt
from data_handling import handling_violation, handling_random

client = mqtt.Client()
client.connect("localhost", 1883, 60)


class MyHandler(FileSystemEventHandler):
    def __init__(self, pattern=None):
        self.pattern = pattern or (".txt")
        self.dummyThread = None
        self.data_return = {}

    def on_any_event(self, event):
        if not event.is_directory and event.src_path.endswith(self.pattern):
            if "violation" in event.src_path:
                self.data_return["violation"] = handling_violation()
            if "statistic" in event.src_path:
                self.data_return["statistic"] = handling_random()
            client.publish("topic/test", str(self.data_return))

    def start(self):
        self.dummyThread = threading.Thread(target=self._process)
        self.dummyThread.daemon = True
        self.dummyThread.start()

    def _process(self):
        while True:
            time.sleep(1)


handler = MyHandler()
handler.start()


def run_watcher():
    observer = Observer()
    observer.schedule(handler, 'data_crawl', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    watcher_thread = threading.Thread(target=run_watcher)
    watcher_thread.start()
    watcher_thread.join()
