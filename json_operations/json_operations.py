import json
import os
import glob
import os.path
from datetime import datetime


class JsonFile:
    def __init__(self):
        self.output_file = self.set_output_file_path()

    def set_output_file_path(self):
        """
        It takes the current directory, goes up one level, then goes into the
        output directory and returns the path to the output.json file
        :return: The file path to the output file.
        """
        root_dir = os.path.join(os.path.dirname(__file__))
        file_path = os.path.join(root_dir, "output", "output_{0}.json".format(
            self.current_date()))

        return file_path

    def create(self, data):
        """
        It opens the file, writes the data to it, and closes the file
        :param data: The data to be written to the file
        """
        target_file = self.output_file
        with open(target_file, "w+") as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def read(source_file):
        """
        It opens the file, reads the file, and then closes the file
        :param source_file: The file path to the JSON file you want to read
        :return: The data is being returned.
        """
        try:
            with open(source_file) as json_file:
                data = json.load(json_file)
        except:
            raise TypeError("File source_file is not valid json")

        return data

    @staticmethod
    def check_date():
        folder_path = r'output'
        file_type = r'/*.json'
        files = glob.glob(folder_path + file_type)
        return max(files, key=os.path.getctime)

    @staticmethod
    def current_date():

        year = datetime.now().year
        day = datetime.now().day
        month = datetime.now().month
        minutes = datetime.now().minute
        hour = datetime.now().hour

        return "{0}_{1}_{2}_{3}_{4}".format(day, month, year, hour, minutes)
