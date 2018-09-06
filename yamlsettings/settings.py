'''
Create a YamlSettings class that holds settings in a dictionary for a given yaml file.
'''
import yaml
import copy
from . import descriptors
from . import errors


class YamlSettings(object):
    ''' class that reads yaml settings files and is
        implemented using the Flyweight Pattern '''
    instances = {}
    yaml_file_path = descriptors.YamlFilePath()
    
    def __new__(cls, yaml_file_path):
        ''' new handles object creation and init handles object initialization '''
        instance = cls.instances.get(yaml_file_path, None)
        if not instance:
            instance = super(YamlSettings, cls).__new__(cls, yaml_file_path)
            cls.instances[yaml_file_path] = instance
        return instance

    def __init__(self, yaml_file_path):
        ''' constructor for our class '''
        self.yaml_file_path = yaml_file_path
        self._settings_dict = self._yaml_loader(yaml_file_path)

    def _yaml_loader(self, yaml_file_path):
        ''' internal method to load yaml files and return the contents as a dict '''
        with open(yaml_file_path, "r") as yaml_file:
            data = yaml.load(yaml_file)
        return data

    def get_data(self, *args):
        ''' exposed method that allows the user to get
            specific yaml attribute/s '''
        data_dict = self._settings_dict
        for arg in args:
            if arg not in data_dict:
                raise errors.AttributeDoesntExistError
            data_dict = data_dict[arg]
        return copy.copy(data_dict)
