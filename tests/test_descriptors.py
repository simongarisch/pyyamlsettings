'''
Test that our descriptors are operating correctly
'''
import pytest
from yamlsettings import descriptors, errors

class TestDescriptors():
    ''' There is only the one descriptor to test: YamlFilePath '''
    yaml_file_path = descriptors.YamlFilePath()

    def test_default_is_none(self):
        ''' the default value should be none '''
        result = self.yaml_file_path.__get__("no_instance")
        assert result is None

    def test_must_be_string(self):
        ''' the path passed must be of the type string '''
        pass

    def test_must_be_yaml(self):
        ''' the file path must end with '.yaml' '''
        pass

    def test_file_must_exist(self):
        ''' the file path must point to an existing file '''
        pass
        