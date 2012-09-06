import os
from os import path
from glob import glob
import difflib
import tempfile
import codecs
import re

from readability import readable, DEFAULT_ENCODING


def test_fixtures():
    def test_fixture(url, original_html, expected_html):
        print('url=%s' % url)
        
        actual_html = readable(url, original_html)
        
        # Write the HTML for later diagnosis
        _, actual_html_fn = tempfile.mkstemp('readabilitytest')
        os.close(_)
        _, expected_html_fn = tempfile.mkstemp('readabilitytest')
        os.close(_)
        with codecs.open(actual_html_fn, 'w', DEFAULT_ENCODING) as f:
            f.write(actual_html)
        with codecs.open(expected_html_fn, 'w', DEFAULT_ENCODING) as f:
            f.write(expected_html)
        
        # Verify that there is no 'diff' between the two versions
        diff = list(difflib.context_diff(
            actual_html.splitlines(), expected_html.splitlines()))
        diff_string = '\n'.join(diff)
        assert not diff, (
            'readable version differs; diff:\n{0}\n'
            'expected: {1}\n'
            'actual: {2}').format(
            diff_string,
            expected_html_fn,
            actual_html_fn,
        )
        
    fixtures_dir = path.join(path.dirname(__file__), 'fixtures')
    for urlf in glob(path.join(fixtures_dir, '*.url')):
        url = open(urlf).read().strip()
        orightmlf = urlf[:-4] + '.orig.html'
        htmlf = urlf[:-4] + '.html'
        original_html = open(orightmlf).read().decode(DEFAULT_ENCODING)
        expected_html = open(htmlf).read().decode(DEFAULT_ENCODING)
        
        yield path.basename(urlf), test_fixture, url, original_html, expected_html