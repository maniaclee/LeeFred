#!/usr/bin/python

import re
import xml.etree.ElementTree as et

__author__ = 'lipeng'


def error(errmsg):
    feeds = Feedback()
    feeds.add_item(title='result', subtitle=errmsg, valid='NO')
    return feeds


class Runner():
    def __init__(self, results):
        self.results = results

    def run(self, query):
        feeds = Feedback()
        for e in self.complete(self.results, query):
            e.addToFeedBack(feeds)
        return feeds

    def trim(self, ser):
        return re.subn('[^a-zA-Z]', '', ser)[0]

    def complete(self, results, s):
        if not s or not s.strip():
            return results
        return [ser for ser in results if self.trim(ser.title).lower().find(self.trim(s).lower()) >= 0]


class Result:
    def __init__(self, title, subtitle="", arg="", valid=True, autocomplete="", icon="icon.png"):
        self.title = title
        self.subtitle = subtitle
        self.arg = arg
        self.valid = "yes" if valid else "no"
        self.autocomplete = autocomplete
        self.icon = icon

    def addToFeedBack(self, f):
        f.add_item(self.title, self.subtitle, self.arg, self.valid, self.autocomplete, self.icon)

    def toFeedBack(self):
        result = Feedback()
        self.addToFeedBack(result)
        return result


class Feedback():
    """Feeback used by Alfred Script Filter

    Usage:
        fb = Feedback()
        fb.add_item('Hello', 'World')
        fb.add_item('Foo', 'Bar')
        print fb

    """

    def __init__(self):
        self.feedback = et.Element('items')

    def __repr__(self):
        """XML representation used by Alfred

        Returns:
            XML string
        """
        return et.tostring(self.feedback)

    def add_item(self, title, subtitle="", arg="", valid="yes", autocomplete="", icon="icon.png"):
        """
        Add item to alfred Feedback

        Args:
            title(str): the title displayed by Alfred
        Keyword Args:
            subtitle(str):    the subtitle displayed by Alfred
            arg(str):         the value returned by alfred when item is selected
            valid(str):       whether or not the entry can be selected in Alfred to trigger an action
            autcomplete(str): the text to be inserted if an invalid item is selected. This is only used if 'valid' is 'no'
            icon(str):        filename of icon that Alfred will display
        """
        item = et.SubElement(self.feedback, 'item', uid=str(len(self.feedback)),
                             arg=arg, valid=valid, autocomplete=autocomplete)
        _title = et.SubElement(item, 'title')
        _title.text = title
        _sub = et.SubElement(item, 'subtitle')
        _sub.text = subtitle
        _icon = et.SubElement(item, 'icon')
        _icon.text = icon
