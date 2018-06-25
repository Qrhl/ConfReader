import os


class ConfigKeyException(Exception):
    """
    Exception that is raised if the key is not in the dictionary thus not in the configuration file.
    """
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return "No such Key in the configuration file"


class ConfReader:
    """
    This class is a parser for a configuration file. It reads the keys and values of the file and write them in a dictionary.
    The configuration file must be written as follows: KEY = Value and a line unused or a commentary must start with a #
    """

    def __init__(self, filename, environment='', path='./'):
        """
        Simple constructor for the object
        :param filename: name of the configuration file
        :param path: path of the configuration file, by default, it is the current folder
        """
        self.path = os.path.join(path, filename)
        self.conf = {}
        self.environment = environment
        self.parse_env()
        self.parse_values()

    def parse_env(self):
        """
        This method reads the configuration file and recovers the environment to use if not specified
        :return: /
        """
        if self.environment == '':
            with open(self.path) as conf_file:
                lines = conf_file.readlines()
                for line_conf in lines:
                    line_conf.strip('\n').strip('\r').strip()
                    if not line_conf.startswith("#") and line_conf != '\r' and line_conf != '\n' and line_conf != ' ':
                        try:
                            conf_key = line_conf.split("=")[0].strip('\n').strip("\r").strip()
                            conf_value = line_conf.split("=")[1].strip('\n').strip("\r").strip()
                            if conf_key == 'ENV':
                                self.environment = conf_value
                        except IndexError:
                            pass

    def parse_values(self):
        """
        This method reads the configuration file and stores the data in a dictionary
        :return: /
        """
        with open(self.path) as conf_file:
            lines = conf_file.readlines()
            current_env = ''
            empty = 0
            for line_conf in lines:
                line_conf.strip('\n').strip('\r').strip()
                if not line_conf.startswith("#") and line_conf != '\r' and line_conf != '\n' and line_conf != ' ':
                    if self.environment != '':
                        try:
                            if line_conf.find('[') != -1 or line_conf.find(']') != -1:
                                current_env = line_conf.split('[')[1].split(']')[0]
                            else:
                                if current_env == self.environment:
                                    conf_key = line_conf.split("=")[0].strip('\n').strip("\r").strip()
                                    conf_value = line_conf.split("=")[1].strip('\n').strip("\r").strip()
                                    if conf_key not in self.conf.keys() and conf_key != "ENV":
                                        self.conf[conf_key] = conf_value
                                        if conf_value == '':
                                            empty += 1
                        except IndexError as e:
                            print('\x1b[31;0m' + e.__str__() + '\x1b[0m')
                            print("The configuration file might have some issues. Check it.")
                    else:
                        try:
                            conf_key = line_conf.split("=")[0].strip('\n').strip("\r").strip()
                            conf_value = line_conf.split("=")[1].strip('\n').strip("\r").strip()
                            if conf_key not in self.conf.keys() and conf_key != "ENV":
                                self.conf[conf_key] = conf_value
                                if conf_value == '':
                                    empty += 1
                        except IndexError:
                            print('\x1b[31;0m' + e.__str__() + '\x1b[0m')
                            print("The configuration file might have some issues. Check it.")
            if empty > 0:
                print('\x1b[34;0m' + "There is {} empty value(s) in the config file!".format(empty) + '\x1b[0m')

    def get_value(self, key):
        """
        :param key: Item of the configuration file
        :return: the value associated to 'key' in the config file
        """
        return self.conf[key]


if __name__ == "__main__":
    config = ConfReader("/Users/quentin/PycharmProjects/ConfReader/test.conf")
    print(config.conf)
