import csv
import json
from abc import ABC, abstractmethod

class ConverterAdapter(ABC):

    @abstractmethod
    def convert(self, path_origin):
        pass

class CsvConversor(ConverterAdapter):

    def __init__(self):
        pass

    def convert(self, path_origin):
        jsonArray = []
        with open (path_origin, "r") as csv_file:
            fieldnames = ["DNI", "Fecha", "Importe", "Terminal", "Transaccion", "Codigo"]
            csvReader = csv.DictReader(csv_file, fieldnames=fieldnames, delimiter=";")
            for row in csvReader:
                jsonArray.append(row)
        return jsonArray


class TextConversor(ConverterAdapter):
    
    def __init__(self):
        pass

    def convert(self, path_origin):
        jsonArray = []
        fieldnames = ["Fecha", "Terminal", "Transaccion", "Importe"]
        with open(path_origin, "r") as txt_file:
            for line in txt_file:
                line = line.split("   ")
                if not line:
                    continue
                jsonArray.append({fieldnames[0]:line[0], fieldnames[1]:line[1], fieldnames[2]:line[2], fieldnames[3]:line[3]})
        return jsonArray
        

class JsonCreator:

    def __init__(self):
        pass

    def save(self, path, jsonArray):
        with open (path, "w") as json_file:
            jsonString = json.dumps(jsonArray, indent=4)
            json_file.write(jsonString)

class ConverterImpl:
    
    def __init__(self, adaptee:ConverterAdapter):
        self.adaptee = adaptee

    def convert(self, path_origin, path_end):
        jsonArray = self.adaptee.convert(path_origin)
        create_json = JsonCreator()
        create_json.save(path_end, jsonArray)

def main():
    path_csv = "8283531-20221013.csv"
    path_txt = "858-20221013.txt"
    path_json = "json_file.json"
    path_json_2 = "json_file_txt.json"
    
    csv_conversor = ConverterImpl(CsvConversor())
    txt_conversor = ConverterImpl(TextConversor())
    
    csv_conversor.convert(path_csv, path_json)
    txt_conversor.convert(path_txt, path_json_2)

if __name__ == '__main__':
    main()