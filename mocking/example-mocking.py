# from unittest.mock import Mock
# json=Mock()
# json.loads('{"key":"value"}')
# json.loads.assert_called()
# json.loads.assert_called_once()
# json.loads.assert_called_with('{"key":"value"}')
# json.loads.assert_called_once_with('{"key":"value"}')

import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    r_post=requests.post('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # Test a connection timeout
        requests.get.side_effect = Timeout
        # with self.assertRaises(Timeout):
        get_holidays()

if __name__ == '__main__':
    unittest.main()