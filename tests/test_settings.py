'''
Here we test several aspects of our YamlSettings class
'''
import os
import pytest
from yamlsettings import YamlSettings, errors


class TestYamlSettings(object):
    ''' this class should read / query yaml files and only create 
        one instance per file read '''

    def setup_method(self, method):
        ''' create common resources for our tests '''
        dir_path = self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.yaml_file1_path = os.path.join(dir_path, "test_yaml_file1.yaml")
        self.yaml_file2_path = os.path.join(dir_path, "test_yaml_file2.yaml")
    
    def teardown_method(self, method):
        ''' and delete them at the end of each run '''
        del self.dir_path
        del self.yaml_file1_path
        del self.yaml_file2_path

    def test_is_flyweight(self):
        ''' test that this is implemented as a Flyweight pattern '''
        obj1A = YamlSettings(self.yaml_file1_path)
        obj1B = YamlSettings(self.yaml_file1_path)
        obj2A = YamlSettings(self.yaml_file2_path)
        obj2B = YamlSettings(self.yaml_file2_path)
        assert id(obj1A) == id(obj1B)
        assert id(obj2A) == id(obj2B)
