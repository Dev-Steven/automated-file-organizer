import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os.path
from os import path
import os, sys
import json


folder_watched = "/Users/stevenchung/Desktop/input"
# print("folder_watched exists: " + str(path.exists(folder_watched)))
png_folder = "/Users/stevenchung/Desktop/png_folder"
# print("png_folder exists: " + str(path.exists(png_folder)))
screenshot_folder = "/Users/stevenchung/Desktop/screenshot_folder"


class FileManager(FileSystemEventHandler):
    print("here!")  
    def on_modified(self, event):
        for file in os.listdir(folder_watched):
            # check for png/jpeg files
            png = ".png"
            screenShot = "Screen Shot"
            if(png in file):
                print("png found: " + file)
                src = folder_watched + "/" + file
                print("src: " + src)
                new_destination = png_folder + "/" + file
                os.rename(src, new_destination)
            if(screenShot in file):
                print("screen shot found! " + file)
                src = folder_watched + "/" + file
                print("src: " + src)
                new_destination = screenshot_folder + "/" + file
                os.rename(src, new_destination)


# print("event_handler created")
event_handler = FileManager()

# print("observer created")
my_observer = Observer()

# print("running if statement")
my_observer.schedule(event_handler, folder_watched, recursive=True)

# print("starting observer")
my_observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
my_observer.join()
