import os
from lib2to3 import refactor

import pytest


def get_cases():
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    ans = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.in.py'):
            basename = filename[:-6]
            input_file = os.path.join(data_dir, filename)
            output_file = os.path.join(data_dir, basename + '.out.py')
            ans.append(pytest.param(input_file, output_file, id=filename[:-6]))
    return ans


@pytest.mark.parametrize('input,output', get_cases())
def test_fixers(input, output):
    fixers = refactor.get_fixers_from_package('trollius_fixers')
    refactorer = refactor.RefactoringTool(fixers)
    with open(input) as f:
        input_text = f.read()
    with open(output) as f:
        output_text = f.read()
    converted = str(refactorer.refactor_string(input_text, input))
    assert output_text == converted
