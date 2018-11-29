import unittest
from mockito import mock, when, verify
# from .project import Project
# from .options import Options

from ..lib.project import Project
from ..lib.options import Options

class TestProject(unittest.TestCase):

    def _default_options(self, optional):
        if optional is None:
            optional = []
        options = Options()
        options.parse(['-o', 'ghorg', '-b', 'branch'] + optional)
        return options

    def setUp(self):
        self.project = Project(self._default_options([]))
        # mocked_process = mock()
        # when(mocked_process).execute('date').thenReturn("The date might be: "\
        #                                                     +self.project.process.execute("date").strip('\n')\
        #                                                     +"\nbut we could also overwrite it to be the"\
        #                                                     +" 1st of April instead.")
        # overwriting project's process.execute('date') with the mock function above
        # just an example of overwriting a dependency when testing
        # self.project.process = mocked_process

    def test_verify_should_fail_if_invalid_file_is_passed(self):
        self.project = Project(self._default_options(['--pom', '/tmp/not_existing.xml']))
        try:
            self.project.verify()
            self.assertFalse("Required parameters missing but test passed")
        except AssertionError:
            pass


    #
    # def test_project_should_fail_if_file_is_invalid(self):
    #     self.assertTrue('1st of April' in self.project.process.execute('date'))
    #     verify(self.project.process).execute('date')
    #
    # def test_project_should_get_date(self):
    #     self.assertTrue('1st of April' in self.project.process.execute('date'))
    #     verify(self.project.process).execute('date')

if __name__ == '__main__':
    unittest.main()
