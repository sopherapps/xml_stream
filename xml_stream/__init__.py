"""Entry point for simple_email"""
from typing import Optional, Union, Iterator
from xml.etree import cElementTree as ElementTree
from xml.etree.cElementTree import Element

__version__ = "0.0.1"

from .data_types import XmlDictElement, XmlListElement


def _convert_xml_element_to_dict(xml_element: Element) -> XmlDictElement:
    """Converts an xml element into a dictionary"""
    return XmlDictElement(xml_element)


def read_xml_file(file_path: str, records_tag: str, to_dict: Optional[bool] = False,
                  **kwargs) -> Union[Iterator[Element], Iterator[XmlDictElement]]:
    """Reads an XML file element by element and returns an iterator of either dicts or XML elements"""
    with open(file_path, 'rb') as xml_file:
        context = ElementTree.iterparse(xml_file, events=('start', 'end',))
        context = iter(context)
        event, root = context.__next__()

        for event, element in context:

            if event == 'end' and element.tag == records_tag:
                if to_dict:
                    yield _convert_xml_element_to_dict(element)
                else:
                    yield element
                # clear the root element to leave it empty and use less memory
                root.clear()


def read_xml_string(xml_string: str, records_tag: str, to_dict: Optional[bool] = False,
                    **kwargs) -> Union[Iterator[Element], Iterator[XmlDictElement]]:
    """Reads an XML string element by element and returns an iterator of either dicts or XML elements"""
    parser = ElementTree.XMLPullParser(events=('start', 'end',))
    ElementTree.XML(xml_string, parser=parser)

    for event, element in parser.read_events():
        if event == 'end' and element.tag == records_tag:
            if to_dict:
                yield _convert_xml_element_to_dict(element)
            else:
                yield element
