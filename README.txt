Pypann
===

Pypann is a simple and small audio library for the right-left panning of audio "Sources".

Installation
Dependencies
Pypann relies on only one other library, pygame (http://www.pygame.org).
It uses it for audio.
Though it seems like overkill for such a simple library it was used because of it's simple audio interface.
So install pygame with the instructions for your operating system.
Than just cd to the pypann directory and run $python setup.py install.

Usage

Pypann only has one class the "pypann.Source".
pypann.Source(soundfile) > pypann.Source instance
The soundfile argument is the name of a file format that your pygame install supports (See the pygame.mixer documentation for details).
This function returns a source object wich can be used to control the position of the sound.
pypann.Source.set_position(position) > None
This function sets the position of the sound source.
The positioning system is as follows.
The position can be a value from -11 to 11.
-11 and 11 are both silence, -10 is far left, 0 is centre, and 10 is far right.
Note that the source objects do not have a play or pause method.
Instead the default position is -11 and to play the position is simply changed to a value that will play and to pause the value is simply changed to -11 or 11 again.
pypann.Source.get_position() > position
Returns the current position.
Note, pypann works best when used with pygame.

Written by Ethan Warren under the MIT license.