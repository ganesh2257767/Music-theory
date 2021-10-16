MAJOR = [0, 2, 4, 5, 7, 9, 11, 0]
MINOR = [0, 2, 3, 5, 7, 8, 10, 0]

CHORDS_MAJOR = ['Major', 'Minor', 'Minor', 'Major', 'Major', 'Minor', 'Diminished', 'Major']
CHORDS_MINOR = ['Minor', 'Diminished', 'Major', 'Major', 'Minor', 'Minor', 'Major', 'Major']

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
DEGREES = ['Tonic', 'Super Tonic', 'Mediant', 'Sub Dominant', 'Dominant', 'Sub Mediant', 'Leading Tone']

def create_scale(note: str, major: bool = True) -> tuple[str, str, str]:
    n = NOTES.index(note)
    notes = NOTES[n:] + NOTES[:n]
    scale = [notes[i] for i in (MINOR, MAJOR)[major]]
    chords = ''
            
    relative, chord_type = (f'{scale[-3]} Minor', CHORDS_MAJOR) if major else (f'{scale[2]} Major', CHORDS_MINOR)
        
    for i, n in enumerate(scale[:-1]):
        chords += f'{DEGREES[i]} :: {n} {chord_type[i]}: {scale[i%7]} - {scale[(i+2)%7]} - {scale[(i+4)%7]}\n\n'


    return ' - '.join(scale), relative, chords
