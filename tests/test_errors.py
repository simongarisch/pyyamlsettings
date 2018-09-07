'''
test that all of the errors are getting raised correctly
'''
import pytest
from pyyamlsettings import errors


def test_errors():
    ''' make sure these can all be raised without issue '''
    errors_list = [errors.YamlSettingsError,
                   errors.YamlFilePathTypeError,
                   errors.NotAYamlFileError,
                   errors.YamlFileMustExistError,
                   errors.AttributeDoesntExistError]

    for error in errors_list:
        # make sure there is no problem raising the error
        with pytest.raises(error):
            raise error
