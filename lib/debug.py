#!/usr/bin/env python3

from dog import Dog
import ipdb

#ipdb.set_trace()
class TestDogproperties:
    '''class Dog in dog.py'''

    def test_name_breed_valid(self):
        '''validates name and breed properties are initialised with valid values'''
        try:
            dog = Dog("Fido", "Corgi")
        except Exception as exc:
            assert False, f'Dog("Fido", "corgi" raised an exception {exc})'

    def test_name_is_string_valid_length(self): 
             '''validates name property is assigned a string between 1 and 25 characters'''
        dog = Dog("Fido", "Corgi")
        with pytest.raises(ValueError):
            dog.name = 7  # not a string
        with pytest.raises(ValueError):
            dog.name = ''  # too short
        with pytest.raises(ValueError):
            dog.name = 'Fido the adorable Corgi who likes to steal socks'
    def test_breed_is_approved_breed(self):
        '''validates breed property is in list of approved choices'''
        dog = Dog("Snoopy", "Beagle")
        with pytest.raises(ValueError):
            dog.breed = "Poodle"  # not an approved breed       