"""Entry point for simple_email"""
from typing import Optional, Union, Iterator, Tuple
from xml.etree import cElementTree as ElementTree
from xml.etree.cElementTree import Element

__version__ = "0.0.7"

from .data_types import XmlDictElement, XmlListElement


def _convert_xml_element_to_dict(xml_element: Element) -> XmlDictElement:
    """Converts an xml element into a dictionary"""
    return XmlDictElement(xml_element)


def read_xml_file(file_path: str, records_tag: Optional[list], to_dict: Optional[bool] = False,
                  **kwargs) -> Tuple[Union[Iterator[Element], Iterator[XmlDictElement]], str]:
    """Reads an XML file element by element and returns an iterator of either dicts or XML elements and found tag"""
    with open(file_path, 'rb') as xml_file:
        context = ElementTree.iterparse(xml_file, events=('start', 'end',))
        context = iter(context)
        root = None

        for event, element in context:
            if root is None:
                root = element

            if event == 'end' and element.tag in records_tag:
                found_element = _convert_xml_element_to_dict(element) if to_dict else element
                yield found_element, element.tag
                # clear the root element to leave it empty and use less memory
                if root != element:
                    root.clear()
                    element.clear()


def read_xml_string(xml_string: str, records_tag: Optional[list], to_dict: Optional[bool] = False,
                    **kwargs) -> Tuple[
    Union[Iterator[Element], Iterator[XmlDictElement]], str]:
    """Reads an XML string element by element and returns an iterator of either dicts or XML elements and found tag"""
    parser = ElementTree.XMLPullParser(events=('start', 'end',))
    ElementTree.XML(xml_string, parser=parser)

    for event, element in parser.read_events():
        if event == 'end' and element.tag in records_tag:
            found_element = _convert_xml_element_to_dict(element) if to_dict else element
            yield found_element, element.tag
