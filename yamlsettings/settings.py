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

    def get_attribute(self, attribute):
        ''' exposed method that allows the user to get a specific yaml attribute '''
        if attribute not in self._settings_dict:
            raise errors.AttributeDoesntExistError
        return copy.copy(self._settings_dict[attribute])

    def get_all_attributes(self):
        ''' exposed method that returns a dict with attributes as keys '''
        return copy.copy(self._settings_dict)
