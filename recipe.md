
## 1. Describe the Problem

# One
# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text
# ,assuming that I can read 200 words a minute.

#  Design the Function Signature

def read_speed(text,wpm):
    """check how many long to read text based reading speed (wpm)

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")
        wpm: words per minute (integer e.g. 200)

    Returns: (time taken to read)
        an integer (e.g. 120)


# Create Examples as Tests

"""
given 200 words 
return 1 minute as time taken to read wpm(200)
"""
read_speed("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam facilisis, ex in consequat elementum, augue quam pellentesque libero, nec viverra quam dui a justo. Etiam vitae varius tortor. Integer bibendum convallis odio, vel fermentum risus. Quisque ultrices, purus a euismod suscipit, eros metus vehicula dui, eget euismod purus lorem eget justo. Sed quis enim eget risus cursus ultricies eu ac ex. Morbi varius turpis sit amet orci euismod tincidunt. Nulla quis justo a ex hendrerit semper ac nec quam. Nam sed purus in odio congue volutpat a et ligula. Curabitur nec justo vitae est ultrices efficitur. Vestibulum a vehicula ipsum, eget finibus odio. Donec tincidunt diam eget tortor congue tincidunt. Proin non odio in nunc tincidunt euismod. Fusce id tellus vel urna ultricies euismod a id quam.

Vivamus dignissim, libero a bibendum laoreet, ipsum massa pharetra elit, vel vestibulum justo orci quis felis. Aliquam erat volutpat. Ut ac feugiat felis. Nullam vel ante justo. Suspendisse potenti. Phasellus blandit bibendum ex, nec fringilla neque. In auctor, enim sit amet rhoncus consequat, libero turpis posuere libero, eu tincidunt velit nunc eget odio. Curabitur sit amet massa a arcu ultrices facilisis eget sed lectus. Integer auctor tortor at laoreet sollicitudin. Duis in augue nec ipsum fermentum facilisis vel in risus. Sed feugiat, purus ut tristique auctor, velit nunc dignissim nisl, non euismod justo justo non urna. Nullam non neque ac dui efficitur feugiat ac sit amet dolor. Vivamus interdum libero vitae elit elementum, id vestibulum orci auctor. Phasellus nec erat eu mi tristique vehicula. Nullam efficitur lectus ut justo laoreet, id congue ex varius.





", 200) => 1


"""
given 200 words 
return 4 minute as time taken to read (wpm = 50)
"""
read_speed("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam facilisis, ex in consequat elementum, augue quam pellentesque libero, nec viverra quam dui a justo. Etiam vitae varius tortor. Integer bibendum convallis odio, vel fermentum risus. Quisque ultrices, purus a euismod suscipit, eros metus vehicula dui, eget euismod purus lorem eget justo. Sed quis enim eget risus cursus ultricies eu ac ex. Morbi varius turpis sit amet orci euismod tincidunt. Nulla quis justo a ex hendrerit semper ac nec quam. Nam sed purus in odio congue volutpat a et ligula. Curabitur nec justo vitae est ultrices efficitur. Vestibulum a vehicula ipsum, eget finibus odio. Donec tincidunt diam eget tortor congue tincidunt. Proin non odio in nunc tincidunt euismod. Fusce id tellus vel urna ultricies euismod a id quam.

Vivamus dignissim, libero a bibendum laoreet, ipsum massa pharetra elit, vel vestibulum justo orci quis felis. Aliquam erat volutpat. Ut ac feugiat felis. Nullam vel ante justo. Suspendisse potenti. Phasellus blandit bibendum ex, nec fringilla neque. In auctor, enim sit amet rhoncus consequat, libero turpis posuere libero, eu tincidunt velit nunc eget odio. Curabitur sit amet massa a arcu ultrices facilisis eget sed lectus. Integer auctor tortor at laoreet sollicitudin. Duis in augue nec ipsum fermentum facilisis vel in risus. Sed feugiat, purus ut tristique auctor, velit nunc dignissim nisl, non euismod justo justo non urna. Nullam non neque ac dui efficitur feugiat ac sit amet dolor. Vivamus interdum libero vitae elit elementum, id vestibulum orci auctor. Phasellus nec erat eu mi tristique vehicula. Nullam efficitur lectus ut justo laoreet, id congue ex varius.





", 50) => 4
