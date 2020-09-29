import unittest
import port_scanner

print("***Tests***")
class UnitTests(unittest.TestCase):
    def test_port_scanner_ip(self):
        ports = port_scanner.get_open_ports("209.216.230.240", [440, 445], False)
        actual = ports
        expected = [443]
        self.assertEqual(actual, expected, 'Expected scanning ports of IP address to return [443].')

    def test_port_scanner_url(self):
        ports = port_scanner.get_open_ports("www.stackoverflow.com", [79, 82], False)
        actual = ports
        expected = [80]
        self.assertEqual(actual, expected, 'Expected scanning ports of URL address to return [80].')
  
    def test_port_scanner_url_multiple_ports(self):
        ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], False)
        actual = ports
        expected = [22, 80]
        self.assertEqual(actual, expected, 'Expected scanning ports of URL address to return [22, 80].')

    def test_port_scanner_verbose_ip_no_hostname_returned_single_port(self):
        str = port_scanner.get_open_ports("104.26.10.78", [440, 450], True)
        actual = str
        expected = "Open ports for 104.26.10.78\nPORT     SERVICE\n443      https"
        self.assertEqual(actual, expected, "Expected 'Open ports for 104.26.10.78\nPORT     SERVICE\n443      https'")

    def test_port_scanner_verbose_ip_hostname_returned_multiple_ports(self):
        str = port_scanner.get_open_ports("137.74.187.104", [440, 450], True)
        actual = str
        expected = "Open ports for hackthissite.org (137.74.187.104)\nPORT     SERVICE\n443      https"
        self.assertEqual(actual, expected, "Expected 'Open ports for hackthissite.org (137.74.187.104)\nPORT     SERVICE\n443      https'")

    def test_port_scanner_verbose_hostname_multiple_ports(self):
        str = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
        actual = str
        expected = "Open ports for scanme.nmap.org (45.33.32.156)\nPORT     SERVICE\n22       ssh\n80       http"
        self.assertEqual(actual, expected, "Expected 'Open ports for scanme.nmap.org (45.33.32.156)\nPORT     SERVICE\n22       ssh\n80       http'")

    def test_port_scanner_invalid_hostname(self):
        err = port_scanner.get_open_ports("scanme.nmap", [22, 42], False)
        actual = err
        expected = "Error: Invalid hostname"
        self.assertEqual(actual, expected, "Expected 'Error: Invalid hostname'")
  
    def test_port_scanner_invalid_ip_address(self):
        err = port_scanner.get_open_ports("266.255.9.10", [22, 42], False)
        actual = err
        expected = "Error: Invalid IP address"
        self.assertEqual(actual, expected, "Expected 'Error: Invalid IP address'")

if __name__ == "__main__":
    unittest.main()