import pytest # <-- New code
from lib.reading_time import *

def test_read_speed():
    text = "this will work"
    
    textb = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam facilisis, ex in consequat elementum, augue quam pellentesque libero, nec viverra quam dui a justo. Etiam vitae varius tortor. Integer bibendum convallis odio, vel fermentum risus. Quisque ultrices, purus a euismod suscipit, eros metus vehicula dui, eget euismod purus lorem eget justo. Sed quis enim eget risus cursus ultricies eu ac ex. Morbi varius turpis sit amet orci euismod tincidunt. Nulla quis justo a ex hendrerit semper ac nec quam. Nam sed purus in odio congue volutpat a et ligula. Curabitur nec justo vitae est ultrices efficitur. Vestibulum a vehicula ipsum, eget finibus odio. Donec tincidunt diam eget tortor congue tincidunt. Proin non odio in nunc tincidunt euismod. Fusce id tellus vel urna ultricies euismod a id quam. Vivamus dignissim, libero a bibendum laoreet, ipsum massa pharetra elit, vel vestibulum justo orci quis felis. Aliquam erat volutpat. Ut ac feugiat felis. Nullam vel ante justo. Suspendisse potenti. Phasellus blandit bibendum ex, nec fringilla neque. In auctor, enim sit amet rhoncus consequat, libero turpis posuere libero, eu tincidunt velit nunc eget odio. Curabitur sit amet massa a arcu ultrices facilisis eget sed lectus. Integer auctor tortor at laoreet sollicitudin. Duis in augue nec ipsum fermentum facilisis vel in risus. Sed feugiat, purus ut tristique auctor, velit nunc dignissim nisl, non euismod justo justo non urna. Nullam non neque ac dui efficitur feugiat ac sit amet dolor. Vivamus interdum libero vitae elit elementum, id vestibulum orci auctor. Phasellus nec erat eu mi tristique vehicula. Nullam efficitur lectus ut justo laoreet, id congue ex varius."
    
    assert read_speed(text, 3) == 1
    assert read_speed(text, 1.5) == 2


def test_grammar_correct():
    g = grammar("Hello, how are you.")
    assert g == True

def test_grammar_false():
    
    with pytest.raises(Exception) as e:
        g = grammar("hello how are you")
    error_message = str(e.value)
    assert error_message == "sorry WRONG"

        
