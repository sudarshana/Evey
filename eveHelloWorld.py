# generated by mBlock5 for codey & rocky
# codes make you happy

import codey, time, rocky, event

@event.start
def on_start():
    codey.display.show('hello', wait = False)
    codey.display.show_image("00003c1e0e0400000000040e1e3c0000", time_s=1)
    codey.display.show_image("00003c7e7e3c000000003c7e7e3c0000", time_s=1)
    codey.display.clear()
    codey.led.show(255, 0, 0, 1)
    codey.speaker.play_melody('hi.wav')
    codey.speaker.play_melody('wow.wav')
    rocky.forward(50, 1)
    rocky.turn_left(50, 1)
    rocky.forward(50, 1, straight = True)

