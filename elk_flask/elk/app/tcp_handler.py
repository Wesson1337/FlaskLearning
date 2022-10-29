from logstash import TCPLogstashHandler


class ModifiedTCPLogstashHandler(TCPLogstashHandler):
    def makePickle(self, record):
        """Method to remove 'can only concatenate str (not 'bytes')' error"""

        return str.encode(self.formatter.format(record)) + b'\n'
