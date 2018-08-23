from unittest import TestCase
from mockito import when, mock, unstub
from hallopy.controller import Controller

"""Mockito usage:

when(os.path).exists('/foo').thenReturn(True)

# or:
import requests  # the famous library
# you actually want to return a Response-like obj, we'll fake it
response = mock({'status_code': 200, 'text': 'Ok'})
when(requests).get(...).thenReturn(response)

# use it
requests.get('http://google.com/')

# clean up
unstub()

Another example:

# setup
response = mock({
    'status_code': 200,
    'text': 'Ok'
}, spec=requests.Response)
when(requests).get('https://example.com/api').thenReturn(response)

# run
assert get_text('https://example.com/api') == 'Ok'

# done!
"""


class TestController(TestCase):
    def test_controller_initiation(self):
        """Test if controller params initiated with 0. """
        # setup
        controller = Controller()

        # run
        assert controller.get_up_param() == 0
        assert controller.get_down_param() == 0
        assert controller.get_left_param() == 0
        assert controller.get_right_param() == 0
        assert controller.get_forward_param() == 0
        assert controller.get_backward_param() == 0
        assert controller.get_rotate_left_param() == 0
        assert controller.get_rotate_right_param() == 0

        # clean up

    # def test_get_down_param(self):
    #     """Test if down param initiate with 0 value. """
    #     # setup
    #     controller = Controller()
    #
    #     # run
    #     assert controller.get_down_param() == 0
    #
    #     # clean up
    #
    # def test_get_left_param(self):
    #     """Test if left param initiate with 0 value. """
    #     # setup
    #     controller = Controller()
    #
    #     # run
    #     assert controller.get_left_param() == 0
    #
    # def test_get_right_param(self):
    #     self.fail()
    #
    # def test_get_rotate_left_param(self):
    #     """Test if rotate_left param initiate with 0 value. """
    #     self.fail()
    #
    # def test_get_rotate_right_param(self):
    #     """Test if rotate_right param initiate with 0 value. """
    #     self.fail()
    #
    # def test_get_forward_param(self):
    #     """Test if forward param initiate with 0 value. """
    #     self.fail()
    #
    # def test_get_backward_param(self):
    #     """Test if backward param initiate with 0 value. """
    #     self.fail()