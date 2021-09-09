"""Tests for the read_xml_file function"""
import os
from unittest import TestCase, main
from xml.etree.ElementTree import Element
from xml.etree import cElementTree as ElementTree

from xml_stream import read_xml_file


class TestReadXmlString(TestCase):
    """Test class for the read_xml_file function"""

    def setUp(self) -> None:
        """Initialize some variables"""
        test_folder_path = os.path.dirname(__file__)
        self.small_mock_file_path = os.path.join(test_folder_path, 'small_mock.xml')
        self.huge_mock_file_path = os.path.join(test_folder_path, 'huge_mock.xml')

        with open(self.small_mock_file_path, 'rb') as small_mock_file:
            self.expected_small_xml_output = ElementTree.parse(small_mock_file).getroot()

        self.expected_small_mock_output = {
            'operations_department': {
                'employees': [
                    [
                        {
                            'team': 'Marketing',
                            'location': {
                                'name': 'head office',
                                'address': 'Kampala, Uganda'
                            },
                            'first_name': 'John',
                            'last_name': 'Doe',
                            '_value': 'John Doe'

                        },
                        {
                            'team': 'Marketing',
                            'location': {
                                'name': 'head office',
                                'address': 'Kampala, Uganda'
                            },
                            'first_name': 'Jane',
                            'last_name': 'Doe',
                            '_value': 'Jane Doe'

                        },
                        {
                            'team': 'Marketing',
                            'location': {
                                'name': 'head office',
                                'address': 'Kampala, Uganda'
                            },
                            'first_name': 'Peter',
                            'last_name': 'Doe',
                            '_value': 'Peter Doe'

                        }, ],
                    [
                        {
                            'team': 'Customer Service',
                            'location': {
                                'name': 'Kampala branch',
                                'address': 'Kampala, Uganda'
                            },
                            'first_name': 'Mary',
                            'last_name': 'Doe',
                            '_value': 'Mary Doe'

                        },
                        {
                            'team': 'Customer Service',
                            'location': {
                                'name': 'Kampala branch',
                                'address': 'Kampala, Uganda'
                            },
                            'first_name': 'Harry',
                            'last_name': 'Doe',
                            '_value': 'Harry Doe'

                        },
                        {
                            'team': 'Customer Service',
                            'location': {
                                'name': 'Kampala branch',
                                'address': 'Kampala, Uganda'
                            },
                            'first_name': 'Paul',
                            'last_name': 'Doe',
                            '_value': 'Paul Doe'

                        }
                    ],
                ]
            }
        }

    def test_read_huge_xml_file_to_dict(self):
        """Can read a very big xml file easily to return iterator of dicts when to_dict is set to True"""
        if os.path.isfile(self.huge_mock_file_path):
            for element in read_xml_file(self.small_mock_file_path, records_tag='Entry', to_dict=True):
                self.assertIsInstance(element, dict)

    def test_read_huge_xml_file_to_xml_element(self):
        """Can read a very big xml file easily to return iterator of xml.etree.ElementTree.Element by default"""
        if os.path.isfile(self.huge_mock_file_path):
            for element in read_xml_file(self.small_mock_file_path, records_tag='Entry'):
                self.assertIsInstance(element, Element)

    def test_read_xml_file_to_dict_for_staff(self):
        """Converts the XML string into a dict of staff's sub elements when to_dict=True, records_tag=staff"""
        staff_output = {}

        for element in read_xml_file(self.small_mock_file_path, records_tag='staff', to_dict=True):
            staff_output = element

        self.assertDictEqual(staff_output, self.expected_small_mock_output)

    def test_read_xml_file_to_dict_for_operations_department(self):
        """
        Converts the XML string into a dict of operations_department's
        sub elements when to_dict=True, records_tag=operations_department
        """
        operations_department_output = {}

        for element in read_xml_file(self.small_mock_file_path, records_tag='operations_department', to_dict=True):
            operations_department_output = element

        self.assertDictEqual(operations_department_output, self.expected_small_mock_output['operations_department'])

    def test_read_xml_file_to_dict_for_employees(self):
        """
        Converts the XML string into a list of employee's sub elements when to_dict=True, records_tag=employees
        """
        employees_output = []

        for element in read_xml_file(self.small_mock_file_path, records_tag='employees', to_dict=True):
            employees_output.append(element['bio'])

        self.assertListEqual(employees_output, self.expected_small_mock_output['operations_department']['employees'])

    def test_read_xml_file_for_staff(self):
        """Converts the XML file into a Element of staff's sub elements when records_tag=staff"""
        for element, expected_element in zip(
                read_xml_file(self.small_mock_file_path, records_tag='staff'),
                self.expected_small_xml_output.findall('staff')):
            self.assertIsInstance(element, Element)
            self.assertEqual(ElementTree.tostring(element), ElementTree.tostring(expected_element))

    def test_read_xml_file_for_operations_department(self):
        """
        Converts the XML file into a Element of operations department's
        sub elements when records_tag=operations_department
        """
        for element, expected_element in zip(
                read_xml_file(self.small_mock_file_path, records_tag='operations_department'),
                self.expected_small_xml_output.findall('operations_department')):
            self.assertIsInstance(element, Element)
            self.assertEqual(ElementTree.tostring(element), ElementTree.tostring(expected_element))

    def test_read_xml_file_for_employees(self):
        """
        Converts the XML file into a Element of employees'
        sub elements when records_tag=employees
        """
        for element, expected_element in zip(
                read_xml_file(self.small_mock_file_path, records_tag='employees'),
                self.expected_small_xml_output.findall('employees')):
            self.assertIsInstance(element, Element)
            self.assertEqual(ElementTree.tostring(element), ElementTree.tostring(expected_element))


if __name__ == '__main__':
    main()
