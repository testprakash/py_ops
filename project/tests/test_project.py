import unittest
from mockito import mock, when, verify
# from .project import Project
# from .options import Options

from ..lib.project import Project
from ..lib.options import Options
import os
from shutil import copyfile

class TestProject(unittest.TestCase):

    def _default_options(self, optional):
        if optional is None:
            optional = []
        options = Options()
        options.parse(['-o', 'org', '-b', 'branch'] + optional)
        return options

    def setUp(self):
        self.project = Project(self._default_options([]))
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.tmp_dir = self.test_dir + '/tmp'
        if not os.path.exists(self.tmp_dir):
            os.mkdir(self.tmp_dir)
        self.src_pom = self.test_dir +  '/resources/pom.xml'

    def test_verify_should_fail_if_invalid_file_is_passed(self):
        self.project = Project(self._default_options(['--pom', '/tmp/not_existing.xml']))
        try:
            self.project.verify()
            self.assertFalse("Required parameters missing but test passed")
        except AssertionError:
            pass

        self.project = Project(self._default_options(['--pom', self.test_dir + '/resources/no_version_tag_pom.xml']))
        try:
            self.project.verify()
            self.assertFalse("Required parameters missing but test passed")
        except AssertionError:
            pass

    def test_verify_getting_snapshot_version(self):
        version = self.project.get_version(self.src_pom)
        self.assertEquals(version.text, '1.0-SNAPSHOT')

    def test_get_new_snapshot_version(self):
        new_version = self.project.get_new_snapshot_version('org', 'branch')
        self.assertEquals(new_version, 'ci_org_branch-SNAPSHOT')

    def test_change_version(self):
        tmp_pom = self.tmp_dir + '/pom.xml'
        copyfile(self.src_pom, tmp_pom)

        self.project = Project(self._default_options(['--pom', tmp_pom]))

        # assert we started with 1.0-SNAPSHOT version
        version = self.project.get_version(tmp_pom)
        self.assertEquals(version.text, '1.0-SNAPSHOT')

        # when
        self.project.update_version()

        version = self.project.get_version(tmp_pom)
        self.assertEquals(version.text, 'ci_org_branch-SNAPSHOT')



if __name__ == '__main__':
    unittest.main()
