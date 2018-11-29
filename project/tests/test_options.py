import unittest
import sys
from project.lib import Options


class TestCommandLineParameters(unittest.TestCase):

    def setUp(self):
        self.options = Options()

    def test_missing_required_params(self):
        self.assert_throws_error([])
        self.assert_throws_error(['-o', 'a'])
        self.assert_throws_error(['--org', 'a'])
        self.assert_throws_error(['-b', 'b'])
        self.assert_throws_error(['--branch', 'b'])

    def test_defaults_options_are_set(self):
        self.parse([])
        self.assertEquals(self.options.known.pom, '/tmp/pom.xml')

    def test_set_options(self):
        self.parse(['-p', '/opt/pom.xml'])
        self.assertEquals(self.options.known.pom, '/opt/pom.xml')
        self.parse(['--pom', '/abc/pom.xml'])
        self.assertEquals(self.options.known.pom, '/abc/pom.xml')

    def parse(self, params):
        req_params = ['-o', 'ghorg', '-b', 'branch']
        opts = req_params + params
        self.options.parse(opts)

    def assert_throws_error(self, params):
        with self.assertRaises(SystemExit):
            self.options.parse(params)
            self.assertFalse("Verify should fail")

if __name__ == '__main__':
    unittest.main()
