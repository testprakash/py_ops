from argparse import ArgumentParser

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        # overrides usage that is by default something like:
        # usage: PROG [-h] [--foo [FOO]] bar [bar ...]
        usage = './bin/run_project'
        self.parser = ArgumentParser(usage=usage)
        # inits the argparser with an argument 'example' with
        # a default value 'example-value'
        self.parser.add_argument('-p',
                                 '--pom',
                                 default='/tmp/pom.xml', # specifies default value
                                 dest='pom', # determines the name of the attribute that parse_args yields
                                 help='Path to pom file') # specifies help message

        self.parser.add_argument('-o',
                                 '--org',
                                 dest='org', # determines the name of the attribute that parse_args yields
                                 required=True,
                                 help='Github org name') # specifies help message


        self.parser.add_argument('-b',
                                 '--branch',
                                 dest='branch', # determines the name of the attribute that parse_args yields
                                 required=True,
                                 help='Github branch name') # specifies help message

    def parse(self, args=None):
        # parse known args, returns a Namespace object
        # unknown args are ignored
        # Parse known args returns (Namespace_of_known, list_of_unknown)
        self.known, self.unknown = self.parser.parse_known_args(args)[:]
        if len(self.unknown) != 0:
            print('*WARN* Unknown args received: ' % repr(self.unknown))
