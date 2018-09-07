from setuptools import setup, find_packages

setup(name="pyyamlsettings",
      version="0.0.1",
      install_requires=[
          "PyYAML>=3.13"
        ],
      description="A Flyweight pattern for loading yaml files",
      long_description=open("README.md").read(),

      author="Simon Garisch",
      author_email="gatman946@gmail.com",
      url="https://github.com/simongarisch/pyyamlsettings",
      packages=find_packages()
     )
