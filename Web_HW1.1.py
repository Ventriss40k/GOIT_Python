# 1) Напишите классы сериализации контейнеров с данными Python в json, bin файлы.
#  Сами классы должны соответствовать общему интерфейсу (абстрактному базовому классу) SerializationInterface.
from abc import ABCMeta, abstractmethod
import pickle
import json


class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self):
        pass

class SerializeBin(SerializationInterface):
    file = ""
    data = ""
    def serialize(self):
        with open (self.file, "wb") as fh:
            pickle.dump(self.data,fh)


class SerializeJson(SerializationInterface):
    file = ""
    data = ""
    def serialize(self):
        with open (self.file, "w") as fh:
            json.dump(self.data,fh)


SerializeBin.file = "Test_bin_write.bin"
SerializeBin.data = "Test data bin"
SerializeBin.serialize(SerializeBin)


SerializeJson.file = "Test_json_write.json"
SerializeJson.data = "Test data json"
SerializeJson.serialize(SerializeJson)

with open ("Test_bin_write.bin", "rb") as fh:
    result = pickle.load(fh)
    print(result)
with open ("Test_json_write.json","r") as fh:
    result = json.load(fh)
    print(result)
