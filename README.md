# xml_stream

A simple XML file and string reader that is able to read big XML files and strings by using streams (iterators),
with an option to convert to dictionaries

## Description

`xml_stream` comprises two helper functions:

### read_xml_file

When given a path to a file and the name of the tag that holds the relevant data, it returns an iterator
of the data as `xml.etree.ElementTree.Element` object by default, or as dicts when `to_dict` argument is `True`

### read_xml_string

When given an XML string and the name of the tag that holds the relevant data, it returns an iterator
of the data as `xml.etree.ElementTree.Element` object by default, or as dicts when `to_dict` argument is `True`

## Main Dependencies

- [Python +3.6](https://www.python.org)

## Getting Started

- Install the package

  ```bash
  pip install xml_stream
  ```

- Import the `read_xml_file` and the `read_xml_string` classes and use accordingly

  ```python
  from xml_stream import read_xml_file, read_xml_string
  
  xml_string = """
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
  
  file_path = '...' # path to your XML file
  
  # For XML strings, use read_xml_string which returns an iterator  
  for element in read_xml_string(xml_string, records_tag='staff'):
      # returns the element as xml.etree.ElementTree.Element by default
      # ...do something with the element
      print(element)
  
  # Note that if a tag is namespaced with say _prefix:tag_ and domain is _xmlns:prefix="https://example",
  # the records_tag from that tag will be '{https://example}tag'
  for element_as_dict in read_xml_string(xml_string, records_tag='staff', to_dict=True):
      # returns the element as dictionary
      # ...do something with the element dictionary
      print(element_as_dict)
      # will print
      """
      {
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
      """
  
  # For XML files (even really large ones), use read_xml_file which also returns an iterator  
  for element in read_xml_file(file_path, records_tag='staff'):
      # returns the element as xml.etree.ElementTree.Element by default
      # ...do something with the element
      print(element)
  
  for element_as_dict in read_xml_file(file_path, records_tag='staff', to_dict=True):
      # returns the element as dictionary
      # ...do something with the element dictionary
      print(element_as_dict)
      # see the print output for read_xml_string
  ```

## How to test

- Clone the repo and enter its root folder

  ```bash
  git clone https://github.com/sopherapps/xml_stream.git && cd xml_stream
  ```

- Create a virtual environment and activate it

  ```bash
  virtualenv -p /usr/bin/python3.6 env && source env/bin/activate
  ```

- Install the dependencies

  ```bash
  pip install -r requirements.txt
  ```
  
- Download a huge xml file for test purposes and save it in the `/test` folder as `huge_mock.xml`

  ```sh
  wget http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/data/SwissProt/SwissProt.xml && mv SwissProt.xml test/huge_mock.xml
  ```

- Run the test command

  ```bash
  python -m unittest
  ```

## Acknowledgements

- This [Stack Overflow Answer](https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary#answer-5807028) about converting XML to dict was very helpful.
- This [Real Python tutorial on publishing packages](https://realpython.com/pypi-publish-python-package/) was very helpful

## License

Copyright (c) 2020 [Martin Ahindura](https://github.com/Tinitto) Licensed under the [MIT License](./LICENSE)
