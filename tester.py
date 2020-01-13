loop  = '''for (int thisNote = 0; thisNote < 142; thisNote++) {

      // to calculate the note duration, take one second
      // divided by the note type.
      //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
      int noteDuration = 1000 / 200;
      tone(5, melody[thisNote], noteDuration);

      // to distinguish the notes, set a minimum time between them.
      // the note's duration + 30% seems to work well:
      int pauseBetweenNotes = noteDuration * 1.30;
      delay(pauseBetweenNotes);
      // stop the tone playing:
      noTone(5);'''


for x in range(0, 113):
    print('''for (int thisNote = 0; thisNote < 142; thisNote++) {
      int noteDuration = 1000 / 200;''')
    print("tone(5, melody" + str(x) + "[thisNote], noteDuration")
    print('''int pauseBetweenNotes = noteDuration * 1.30;
      delay(pauseBetweenNotes);noTone(5);
      };''')