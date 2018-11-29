from process import Process
import subprocess
import sys

class Project:

    def __init__(self, options):
        self.options = options
        self.process = Process()

    def date(self):
        return self._get_date()

    def _get_date(self):
        # prints stdout of subprocess with command "date"
        # strips tailing endoflines because print adds one
        return self.process.execute("date").rstrip('\n')

    def print_example_arg(self):
        return self.options.known.example

    def verify(self):
        result=subprocess.run(['env', 'mvn', 'verify', '-f', self.options.known.pom], capture_output=True)
        if result != 0:
            print('Pom verify failed with msg ' + str(result.stdout).replace('\\n',"\n"))
            raise AssertionError('Pom verify failed')

    #
    # def get_mvn_bin(self):
    #     words = ['env''cat', 'window', 'defenestrate']
    #     import os.path
# os.path.isfile(fname)


