import subprocess
import xml.etree.ElementTree as ET


ET.register_namespace("","http://maven.apache.org/POM/4.0.0")

class Project:

    def __init__(self, options):
        self.options = options

    def verify(self):
        result=subprocess.run(['env', 'mvn', 'verify', '-f', self.options.known.pom], capture_output=True)
        if result.returncode != 0:
            print('Pom verify failed with msg ' + str(result.stdout).replace('\\n',"\n"))
            raise AssertionError('Pom verify failed')

    def assert_version_snapshot(self):
        version_elem = self.get_version(self.options.known.pom)
        if not version_elem.text.endswith('-SNAPSHOT'):
            raise AssertionError('pom version is not SNAPSHOT, version=', version_elem.text)

    def update_version(self):
        tree = ET.parse(self.options.known.pom)
        root = tree.getroot()
        new_version = self.get_new_snapshot_version(self.options.known.org, self.options.known.branch)
        version = self.get_version_from_root(root)
        version.text = new_version

        tree.write(self.options.known.pom, default_namespace="")

    def get_version(self, pom):
        tree = ET.parse(pom)
        root = tree.getroot()
        return self.get_version_from_root(root)

    def get_version_from_root(self, root):
        version_elem = None
        for elem in root:
            if self.tag_without_ns(elem.tag) == 'version':
                version_elem = elem
        return version_elem

    def get_new_snapshot_version(self, organization_name, branch_name):
        return 'ci_' + organization_name + '_' + branch_name + '-SNAPSHOT'

    def tag_without_ns(self, tag):
        return tag.split('}')[1]

