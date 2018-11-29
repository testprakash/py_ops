import subprocess
import sys

class Project:

    def __init__(self, options):
        self.options = options

    def verify(self):
        result=subprocess.run(['env', 'mvn', 'verify', '-f', self.options.known.pom], capture_output=True)
        if result.returncode != 0:
            print('Pom verify failed with msg ' + str(result.stdout).replace('\\n',"\n"))
            raise AssertionError('Pom verify failed')




