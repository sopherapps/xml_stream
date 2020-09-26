"""Tests for the read_xml_string function"""
from unittest import TestCase, main
from xml.etree import cElementTree as ElementTree
from xml.etree.ElementTree import Element

from xml_stream import read_xml_string


class TestReadXmlString(TestCase):
    """Test class for the read_xml_string function"""

    def setUp(self) -> None:
        """Initialize some variables"""
        self.xml_string = """
        <company>
        <staff>
            <operations_department>
                <employees>
                    <team>Marketing</team>
                    <location name="head office" address="Kampala, Uganda" />
                    <bio first_name="John" last_name="Doe">John Doe</bio>
                    <bio first_name="Jane" last_name="Doe">Jane Doe</bio>
                    <bio first_name="Peter" last_name="Doe">Peter Doe</bio>
                </employees>
                <employees>
                    <team>Customer Service</team>
                    <location name="Kampala branch" address="Kampala, Uganda" />
                    <bio first_name="Mary" last_name="Doe">Mary Doe</bio>
                    <bio first_name="Harry" last_name="Doe">Harry Doe</bio>
                    <bio first_name="Paul" last_name="Doe">Paul Doe</bio>
                </employees>
            </operations_department>
        </staff>
        </company>
        """
        self.expected_xml_output: Element = ElementTree.XML(self.xml_string)
        self.expected_output = {
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

    def test_read_xml_string_to_dict_for_staff(self):
        """Converts the XML string into a dict of staff's sub elements when to_dict=True, records_tag=staff"""
        staff_output = {}

        for element in read_xml_string(self.xml_string, records_tag='staff', to_dict=True):
            staff_output = element

        self.assertDictEqual(staff_output, self.expected_output)

    def test_read_xml_string_to_dict_for_operations_department(self):
        """
        Converts the XML string into a dict of operations_department's
        sub elements when to_dict=True, records_tag=operations_department
        """
        operations_department_output = {}

        for element in read_xml_string(self.xml_string, records_tag='operations_department', to_dict=True):
            operations_department_output = element

        self.assertDictEqual(operations_department_output, self.expected_output['operations_department'])

    def test_read_xml_string_to_dict_for_employees(self):
        """
        Converts the XML string into a list of employee's sub elements when to_dict=True, records_tag=employees
        """
        employees_output = []

        for element in read_xml_string(self.xml_string, records_tag='employees', to_dict=True):
            employees_output.append(element['bio'])

        self.assertListEqual(employees_output, self.expected_output['operations_department']['employees'])

    def test_read_xml_string_for_staff(self):
        """Converts the XML string into a Element of staff's sub elements when records_tag=staff"""
        for element, expected_element in zip(
                read_xml_string(self.xml_string, records_tag='staff'), self.expected_xml_output.findall('staff')):
            self.assertIsInstance(element, Element)
            self.assertEqual(ElementTree.tostring(element), ElementTree.tostring(expected_element))

    def test_read_xml_string_for_operations_department(self):
        """
        Converts the XML string into a Element of operations department's
        sub elements when records_tag=operations_department
        """
        for element, expected_element in zip(
                read_xml_string(self.xml_string, records_tag='operations_department'),
                self.expected_xml_output.findall('operations_department')):
            self.assertIsInstance(element, Element)
            self.assertEqual(ElementTree.tostring(element), ElementTree.tostring(expected_element))

    def test_read_xml_string_for_employees(self):
        """
        Converts the XML string into a Element of employees'
        sub elements when records_tag=employees
        """
        for element, expected_element in zip(
                read_xml_string(self.xml_string, records_tag='employees'),
                self.expected_xml_output.findall('employees')):
            self.assertIsInstance(element, Element)
            self.assertEqual(ElementTree.tostring(element), ElementTree.tostring(expected_element))


if __name__ == '__main__':
    main()
