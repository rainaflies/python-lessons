from scamp import *

s = Session(tempo=80)
violin = s.new_part("Violin")

violin.play_note(60, 1, 1)
violin.play_note(60, 1, 1)

violin.play_note(67, 1, 1)
violin.play_note(67, 1, 1)

violin.play_note(69, 1, 1)
violin.play_note(69, 1, 1)

violin.play_note(67, 1, 2)

violin.play_note(65, 1, 1)
violin.play_note(65, 1, 1)

violin.play_note(64, 1, 1)
violin.play_note(64, 1, 1)

violin.play_note(62, 1, 1)
violin.play_note(62, 1, 1)

violin.play_note(60, 1, 2)

violin.play_note(60, 1, 0.5)
violin.play_note(60, 1, 0.5)
violin.play_note(60, 1, 0.5)
violin.play_note(60, 1, 0.5)

violin.play_note(67, 1, 0.5)
violin.play_note(67, 1, 0.5)
violin.play_note(67, 1, 0.5)
violin.play_note(67, 1, 0.5)

violin.play_note(69, 1, 0.5)
violin.play_note(69, 1, 0.5)
violin.play_note(69, 1, 0.5)
violin.play_note(69, 1, 0.5)

violin.play_note(67, 1, 2)

violin.play_note(65, 1, 0.5)
violin.play_note(65, 1, 0.5)
violin.play_note(65, 1, 0.5)
violin.play_note(65, 1, 0.5)

violin.play_note(64, 1, 0.5)
violin.play_note(64, 1, 0.5)
violin.play_note(64, 1, 0.5)
violin.play_note(64, 1, 0.5)

violin.play_note(62, 1, 0.5)
violin.play_note(62, 1, 0.5)
violin.play_note(62, 1, 0.5)
violin.play_note(62, 1, 0.5)

#violin.play_note(60, 1, 2)
violin.play_chord([60, 64, 67], 1, 4)
