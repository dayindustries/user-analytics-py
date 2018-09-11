try:
    # For Python 3.0 and later
    from urllib.request import Request, urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import Request, urlopen

import json

class UserAnalytics:
    def __init__(self, token=None, endpoint=None):
        """
        Creates a UserAnalytics service object.
        :param token: An Amazon API Gateway token.
        :param endpoint: An Amazon API Gateway endpoint.
        Example:
        ::
            import useranalytics
            client = useranalytics.UserAnalytics(
                token='...',
                endpoint='https://4i0ifsvq23.execute-api.us-west-2.amazonaws.com/staging')
        """
        self.token = token
        if not self.token:
            raise Error('token must be provided')
        self.endpoint = endpoint
        if not self.endpoint:
            raise Error('endpoint must be provided')
        self.headers = {
            'x-api-key': self.token,
            'Content-Type': 'application/json'
        }

    def list(self):
        """
        Get a list of user analytics stream corresponding to AWS Kinesis
        streams.
        Example:
        ::
            client.list()
        """
        url = self.endpoint + '/streams'
        request = Request(url, None, self.headers)
        return json.loads(urlopen(request).read())

    def describe(self, streamname):
        """
        Describes a user analytics stream corresponding to an AWS Kinesis
        stream.
        :param streamname: The stream to describe.
        Example:
        ::
            client.describe('UserAnalytics')
        """
        url = self.endpoint + '/streams/' + streamname
        request = Request(url, None, self.headers)
        return json.loads(urlopen(request).read())

    def post(self, streamname, data):
        """
        Describes a user analytics stream corresponding to an AWS Kinesis
        stream.
        :param streamname: The stream to which we will submit.
        :param data: The analytics data to submit.
        Example:
        ::
            client.post('UserAnalytics', {'foo':'bar'})
        """
        url = self.endpoint + '/streams/' + streamname
        blob = bytearray(json.dumps(data), 'utf-8')
        request = Request(url, blob, self.headers)
        return json.loads(urlopen(request).read())
