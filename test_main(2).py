#test_main(2).py 
#pytest file for testing main.py functionality

#imports
from _main_ import *
import sys
from os.path import exists
import pytest
from errors import * 


class TestClass:
    # tests that read_txt() throws FileNotFoundException
    def test_file_not_found(self):
        file_name = 'hdsjjh.butthole'
        with pytest.raises(FileNotFoundError) as exc:
            read_txt(file_name)
        assert exc.type == FileNotFoundError
    
    # tests that read_text() throws no user input exception
    def test_read_txt(self):
        with pytest.raises(NoUserInput) as exc:
            read_txt("")
        assert str(exc.value) == "User did not enter anything."
     
     #def test_neg_input():
     #def test_large_input():
     #def test_empty_input();