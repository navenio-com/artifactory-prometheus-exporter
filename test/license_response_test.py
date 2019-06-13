import unittest

from artifactory_api_client import ArtifactoryApiClient


class ArtifactoryApiClientTest(unittest.TestCase):

    NR_LICENSE_RESPONSE = {
        "type": "Commercial",
        "validThrough": "N/R",
        "licensedTo": "Artifactory Online",
    }

    DATE_LICENSE_RESPONSE = {
        "type": "Commercial",
        "validThrough": "May 15, 2014",
        "licensedTo": "JFrog inc.",
    }

    def setUp(self):
        self.client = ArtifactoryApiClient(None)

    def test_it_should_handle_NR_licence(self):
        nr_valid_through = self.client.handle_licenses(self.NR_LICENSE_RESPONSE)
        self.assertTrue(nr_valid_through[0] > 0)
        self.assertEqual(nr_valid_through[1], "N/R")

    def test_it_should_handle_date_licence(self):
        date_valid_through = self.client.handle_licenses(self.DATE_LICENSE_RESPONSE)
        self.assertTrue(date_valid_through[0] < 0)
        self.assertEqual(date_valid_through[1], "May 15, 2014")


if __name__ == '__main__':
    unittest.main()
