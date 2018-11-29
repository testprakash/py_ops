import sys

from .lib.project import Project
from .lib.options import Options

def run_project(args):
    options = Options()
    options.parse(args[1:])

    project = Project(options)

    project.verify()
    #print('Pom file has valid syntax')

    project.assert_version_snapshot()

    #print('snapshot version')

    project.update_version()

    #print('update completed')

if __name__ == '__main__':
    run_project(sys.argv)
