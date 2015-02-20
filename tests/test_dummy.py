from oslotest import base as test_base


class DummyTest(test_base.BaseTestCase):

    def test_dummy(self):
        """Tests if Python works, to make Jenkins happy with and empty repo."""
        self.assertTrue(True)