from music21 import *
from src.MarkovMusic import MusicMatrix
import random

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
durations =[1, 2, 4, 8, 16]

def get_stream(notes):
    s = stream.Stream()
    for n in notes:
        pitch = n[0]
        duration = 1. / n[1] * 4
        if pitch == 'r':
            s.append(note.Rest(quarterLength=duration))
        else:
            s.append(note.Note(n[0],quarterLength=duration))
    return s

#Row Row Row Your Boat
# song = [['c4', 4], ['c4', 4], ['c4', 4], ['d4', 8], ['e4', 4], ['e4', 4], ['d4', 8], ['e4', 4], ['f4', 8], ['g4', 2], ['c4', 8], ['c4', 8], ['c4', 8], ['g4', 8], ['g4', 8], ['g4', 8], ['e4', 8], ['e4', 8], ['e4', 8], ['c4', 8], ['c4', 8], ['c4', 8], ['g4', 4], ['f4', 8], ['e4', 4], ['d4', 8], ['c4', 2]]

#Undertail
# song = [['g#3', 16.0], ['e4', 16.0], ['d#4', 16.0], ['d4', 16.0], ['d#4', 16.0], ['r', 16.0], ['c#4', 16.0], ['b3', 16.0], ['a#3', 16.0], ['r', 16.0], ['g#3', 16.0], ['g3', 16.0], ['g#3', 16.0], ['r', 16.0], ['d#3', 16.0], ['e3', 16.0], ['d#3', 16.0], ['e3', 16.0], ['d#3', 16.0], ['d3', 16.0], ['d#3', 16.0], ['g3', 16.0], ['b3', 16.0], ['a#3', 16.0], ['g#3', 16.0], ['r', 16.0], ['g#3', 16.0], ['a#3', 16.0], ['b3', 16.0], ['r', 16.0], ['a#3', 16.0], ['b3', 16.0], ['c#4', 16.0], ['r', 16.0], ['b3', 16.0], ['a#3', 16.0], ['g3', 16.0], ['r', 16.0], ['g3', 16.0], ['a#3', 16.0], ['b3', 16.0], ['r', 16.0], ['a#3', 16.0], ['g#3', 16.0], ['d#3', 16.0], ['r', 16.0], ['d#3', 16.0], ['e3', 16.0], ['d#3', 16.0], ['e3', 16.0], ['d#3', 16.0], ['d3', 16.0], ['d#3', 16.0], ['g3', 16.0], ['b3', 16.0], ['a#3', 16.0], ['g#3', 16.0], ['r', 16.0], ['g#3', 16.0], ['g3', 16.0], ['g#3', 16.0], ['r', 16.0], ['g#4', 16.0]]

#Debussy - Reverie
song = [('g5', 2.0), ('d5', 1.3333333333333333), ('e5', 8.0), ('f5', 8.0), ('g5', 4.0), ('e5', 8.0), ('d5', 8.0), ('e5', 5.333333333333333), ('c5', 5.314878892780648), ('e5', 5.314878892710022), ('d5', 1.0), ('a#4', 4.0), ('d5', 4.0), ('e5', 4.0), ('f5', 4.0), ('c5', 1.0), ('g4', 2.0), ('a4', 0.4999999999999998), ('a5', 2.0), ('e5', 1.3333333333333333), ('c5', 8.0), ('e5', 8.0), ('d5', 4.0), ('a#4', 8.0), ('g4', 8.0), ('a5', 2.0), ('e5', 1.3333333333333333), ('c5', 8.0), ('e5', 8.0), ('d5', 4.0), ('a#4', 8.0), ('g4', 8.0), ('g5', 2.0), ('d5', 1.3333333333333333), ('a#4', 8.0), ('d5', 8.0), ('c5', 4.0), ('a4', 8.0), ('g4', 8.0), ('a4', 4.0), ('e4', 8.0), ('a4', 8.0), ('f4', 4.0), ('d4', 8.0), ('f4', 8.0), ('d4', 2.0), ('c4', 2.000000000000007), ('c6', 2.0), ('g5', 1.3333333333333333), ('a5', 8.0), ('a#5', 8.0), ('c6', 4.0), ('a5', 8.0), ('g5', 8.0), ('a5', 5.333333333333333), ('f5', 5.314878892498194), ('a5', 5.314878892498194), ('g5', 1.0), ('d#5', 4.0), ('g5', 4.0), ('a5', 4.0), ('a#5', 4.0), ('f5', 1.0), ('a5', 4.0), ('a#5', 4.0), ('c6', 4.0), ('d6', 4.0), ('a5', 1.0), ('a#5', 4.0), ('d6', 4.0), ('f6', 2.0), ('c#6', 2.0000000003000054), ('r', 8.084210527894808), ('d5', 8.0), ('e5', 8.0), ('r', 4.0), ('f5', 8.0), ('a5', 8.0), ('f6', 2.0), ('c#6', 2.0), ('r', 4.0), ('d5', 8.0), ('e5', 8.0), ('r', 4.0), ('f5', 8.0), ('a5', 8.0), ('f5', 4.0), ('d4', 8.0), ('e4', 8.0), ('f5', 0.3333333333333333), ('f4', 8.0), ('a4', 8.0), ('f4', 2.0), ('f4', 1.0), ('d4', 4.0), ('c4', 4.0), ('d4', 1.0), ('c5', 4.0), ('a#4', 8.0), ('a4', 8.0), ('g4', 1.3333333333333333), ('a4', 8.0), ('a#4', 8.0), ('c5', 4.0), ('c5', 8.0), ('d#5', 8.0), ('d5', 0.5), ('c5', 4.0), ('a#4', 8.0), ('a4', 8.0), ('g4', 1.3333333333333333), ('a4', 8.0), ('a#4', 8.0), ('c5', 8.0), ('d#5', 8.0), ('e5', 0.6666666666666666), ('d#5', 4.0), ('e5', 4.0), ('g5', 4.0), ('f5', 8.0), ('e5', 8.0), ('d5', 2.0), ('d5', 2.0), ('e5', 4.0), ('c5', 0.08888888888888886), ('f5', 4.0), ('e5', 8.0), ('d5', 8.0), ('c5', 1.0), ('d5', 4.0), ('f5', 0.5), ('e5', 4.0), ('d5', 8.0), ('c5', 8.0), ('a#4', 2.0), ('a#5', 2.0), ('a5', 4.0), ('g5', 4.0), ('e5', 0.4444444444444444), ('f5', 0.6666666666666666), ('f4', 4.0), ('f5', 0.23529411764705882), ('e4', 4.0), ('f4', 16.0), ('a4', 16.0), ('f4', 16.0), ('e4', 4.0), ('d4', 4.0), ('c4', 2.0), ('e4', 4.0), ('c#4', 4.0), ('c#4', 4.0), ('e4', 4.0), ('f#4', 4.0), ('g#4', 4.0), ('e4', 2.0), ('f#5', 4.0), ('g#5', 4.0), ('e5', 4.0), ('c#6', 4.0), ('f#5', 4.0), ('g#5', 16.0), ('f#5', 16.0), ('g#5', 16.0), ('e5', 4.0), ('b4', 4.0), ('g#4', 4.0), ('b4', 4.0), ('g#4', 4.0), ('e4', 4.0), ('f#4', 2.0), ('c#5', 2.0), ('f#5', 4.0), ('g#5', 4.0), ('e5', 4.0), ('c#6', 4.0), ('f#5', 4.0), ('g#5', 16.0), ('f#5', 16.0), ('g#5', 16.0), ('e5', 4.0), ('b5', 4.0), ('c#6', 4.0), ('e6', 4.0), ('d#6', 4.0), ('b5', 4.0), ('c#6', 4.0), ('e6', 4.0), ('f#6', 4.0), ('b5', 4.000000000000114), ('c#6', 4.0), ('e6', 4.0), ('d#6', 4.0), ('b5', 4.0), ('c#6', 4.0), ('e6', 4.0), ('f#6', 4.0), ('b5', 4.0), ('g6', 1.3333333333333333), ('a5', 4.0), ('g5', 2.6666666666666665), ('a4', 8.0), ('g4', 2.6666666666666665), ('a4', 8.0), ('d4', 4.0), ('e4', 4.0), ('c4', 4.0), ('a4', 4.0), ('d4', 4.0), ('e4', 16.0), ('d4', 16.0), ('e4', 16.0), ('c4', 2.0), ('d5', 4.0), ('e5', 16.0), ('d5', 16.0), ('e5', 16.0), ('c5', 2.0), ('g5', 2.0), ('d5', 1.3333333333333333), ('e5', 8.0), ('f5', 8.0), ('g5', 4.0), ('e5', 8.0), ('d5', 8.0), ('e5', 5.333333333333333), ('c5', 5.31487889037946), ('e5', 5.31487889037946), ('d5', 1.0), ('a#4', 4.0), ('d5', 4.0), ('e5', 4.0), ('f5', 4.0), ('c5', 1.0), ('g4', 2.0), ('a4', 0.5), ('a5', 2.0), ('e5', 1.3333333333333333), ('c5', 8.0), ('e5', 8.0), ('d5', 4.0), ('a#4', 8.0), ('g4', 8.0), ('a5', 2.0), ('e5', 1.3333333333333333), ('c5', 8.0), ('e5', 8.0), ('d5', 4.0), ('a#4', 8.0), ('g4', 8.0), ('g5', 2.0), ('d5', 1.3333333333333333), ('a#4', 8.0), ('d5', 8.0), ('c5', 4.0), ('a4', 8.0), ('f4', 8.0), ('g5', 2.0), ('d5', 1.3333333333333333), ('a#4', 8.0), ('d5', 8.0), ('c5', 4.0), ('d5', 4.0), ('a#4', 4.0), ('e4', 0.02580385041830461), ('a4', 4.0), ('a4', 2.0), ('a#4', 4.0), ('a4', 4.0), ('a4', 2.0), ('a#4', 4.0), ('a#4', 0.6666666666666666), ('a4', 4.0), ('a#4', 16.0), ('d5', 16.0), ('a#4', 16.0), ('a4', 4.0), ('g4', 4.0), ('f4', 2.0), ('a#5', 4.0), ('a4', 0.49983729252717796), ('a5', 4.0), ('a5', 2.0), ('a#5', 4.0), ('a#5', 2.0), ('a5', 2.0), ('a#5', 4.0), ('a5', 4.0), ('a#5', 16.0), ('d6', 16.0), ('a#5', 16.0), ('a5', 2.0), ('g5', 2.0), ('a5', 0.36355029584697357), ('a6', 1.0)]

s = get_stream(song)
fp = s.write('midi', fp='original.mid')

matrix = MusicMatrix(song)
start_note = ['c4', 4]

random_song = []
for i in range(0, 100):
    start_note = matrix.next_note(start_note)
    random_song.append(start_note)
s = get_stream(random_song)

fp = s.write('midi', fp='test.mid')