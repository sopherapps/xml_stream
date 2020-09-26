"""Module containing protected utility functions for the package"""
from typing import Dict, List
from xml.etree.ElementTree import Element


def get_unique_and_repeated_sub_elements(element: Element):
    """Returns a tuple of (unique_elements_map: Dict, repeated_elements: List,) """
    unique_elements_map: Dict[str, Element] = {}
    repeated_elements: List[Element] = []
    all_tags = []

    for sub_element in element:
        tag = sub_element.tag

        if tag not in all_tags:
            all_tags.append(tag)
            unique_elements_map[tag] = sub_element
        else:
            previously_saved_sub_element = unique_elements_map.pop(tag, None)
            if previously_saved_sub_element is not None:
                repeated_elements.append(previously_saved_sub_element)

            repeated_elements.append(sub_element)

    return unique_elements_map, repeated_elements


def get_xml_element_attributes_as_dict(xml_element: Element):
    """Add the XML element's attributes as a dictionary"""
    element_attributes = xml_element.items()
    return dict(element_attributes) if element_attributes else {}
