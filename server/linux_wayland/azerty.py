# encoding: utf-8
from abstractKeyboardMapping import AbstractKeyboardMapping
import evdev

class Azerty(AbstractKeyboardMapping):
	def __init__(self):
		super(AbstractKeyboardMapping, self).__init__()

	def solo(self):
		return { "1" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_1],
		         "2" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_2],
		         "3" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_3],
		         "4" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_4],
		         "5" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_5],
		         "6" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_6],
		         "7" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_7],
		         "8" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_8],
		         "9" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_9],
		         "0" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_0],
		         "°" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_MINUS],
		         "+" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_EQUAL],

		         "&" : [evdev.ecodes.KEY_1],
		         "é" : [evdev.ecodes.KEY_2],
		         "\"" : [evdev.ecodes.KEY_3],
		         "'" : [evdev.ecodes.KEY_4],
		         "(" : [evdev.ecodes.KEY_5],
		         "-" : [evdev.ecodes.KEY_6],
		         "è" : [evdev.ecodes.KEY_7],
		         "_" : [evdev.ecodes.KEY_8],
		         "ç" : [evdev.ecodes.KEY_9],
		         "à" : [evdev.ecodes.KEY_0],
		         ")" : [evdev.ecodes.KEY_MINUS],
		         "=" : [evdev.ecodes.KEY_EQUAL],

		         "¹" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_1],
		         "~" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_2],
		         "#" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_3],
		         "{" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_4],
		         "[" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_5],
		         "|" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_6],
		         "`" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_7],
		         "\\" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_8],
		         "^" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_9],
		         "@" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_0],
		         "]" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_MINUS],
		         "}" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_EQUAL],

		         "£" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_RIGHTBRACE],
		         "¤" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_RIGHTBRACE],
		         "$" : [evdev.ecodes.KEY_RIGHTBRACE],
		         "%" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_APOSTROPHE],
		         "ù" : [evdev.ecodes.KEY_APOSTROPHE],
		         "µ" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_BACKSLASH],
		         "*" : [evdev.ecodes.KEY_BACKSLASH],

		         "?" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_M],
		         "," : [evdev.ecodes.KEY_M],
		         "." : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_COMMA],
		         ";" : [evdev.ecodes.KEY_COMMA],
		         "/" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_DOT],
		         ":" : [evdev.ecodes.KEY_DOT],
		         "§" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_SLASH],
		         "!" : [evdev.ecodes.KEY_SLASH],

		         "<" : [evdev.ecodes.KEY_102ND],
		         ">" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_102ND],
		         "²" : [evdev.ecodes.KEY_GRAVE],
		         "€" : [evdev.ecodes.KEY_RIGHTALT, evdev.ecodes.KEY_E],

		         "a" : [evdev.ecodes.KEY_Q],
		         "A" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_Q],
		         "z" : [evdev.ecodes.KEY_W],
		         "Z" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_W],
		         "q" : [evdev.ecodes.KEY_A],
		         "Q" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_A],
		         "w" : [evdev.ecodes.KEY_Z],
		         "W" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_Z],
		         "m" : [evdev.ecodes.KEY_SEMICOLON],
		         "M" : [evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_SEMICOLON],
		}


	def multi(self):
		return { "â" : [[evdev.ecodes.KEY_LEFTBRACE, 1], [evdev.ecodes.KEY_LEFTBRACE, 0], [evdev.ecodes.KEY_Q, 1], [evdev.ecodes.KEY_Q, 0]],
		         "ê" : [[evdev.ecodes.KEY_LEFTBRACE, 1], [evdev.ecodes.KEY_LEFTBRACE, 0], [evdev.ecodes.KEY_E, 1], [evdev.ecodes.KEY_E, 0]],
		         "î" : [[evdev.ecodes.KEY_LEFTBRACE, 1], [evdev.ecodes.KEY_LEFTBRACE, 0], [evdev.ecodes.KEY_I, 1], [evdev.ecodes.KEY_I, 0]],
		         "ô" : [[evdev.ecodes.KEY_LEFTBRACE, 1], [evdev.ecodes.KEY_LEFTBRACE, 0], [evdev.ecodes.KEY_O, 1], [evdev.ecodes.KEY_O, 0]],
		         "û" : [[evdev.ecodes.KEY_LEFTBRACE, 1], [evdev.ecodes.KEY_LEFTBRACE, 0], [evdev.ecodes.KEY_U, 1], [evdev.ecodes.KEY_U, 0]],
		         "ŷ" : [[evdev.ecodes.KEY_LEFTBRACE, 1], [evdev.ecodes.KEY_LEFTBRACE, 0], [evdev.ecodes.KEY_Y, 1], [evdev.ecodes.KEY_Y, 0]],

		         "Â" : [[evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_Q, 1],
		                [evdev.ecodes.KEY_Q, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		         "Ê" : [[evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_E, 1],
		                [evdev.ecodes.KEY_E, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		         "Î" : [[evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_I, 1],
		                [evdev.ecodes.KEY_I, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		         "Ô" : [[evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_O, 1],
		                [evdev.ecodes.KEY_O, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		         "Û" : [[evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_U, 1],
		                [evdev.ecodes.KEY_U, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		         "Ŷ" : [[evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_Y, 1],
		                [evdev.ecodes.KEY_Y, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],

		         "ä" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0],
		                [evdev.ecodes.KEY_Q, 1],
		                [evdev.ecodes.KEY_Q, 0]],
		         "ë" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0],
		                [evdev.ecodes.KEY_E, 1],
		                [evdev.ecodes.KEY_E, 0]],
		         "ï" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0],
		                [evdev.ecodes.KEY_I, 1],
		                [evdev.ecodes.KEY_I, 0]],
		         "ö" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0],
		                [evdev.ecodes.KEY_O, 1],
		                [evdev.ecodes.KEY_O, 0]],
		         "ü" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0],
		                [evdev.ecodes.KEY_U, 1],
		                [evdev.ecodes.KEY_U, 0]],
		         "ÿ" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0],
		                [evdev.ecodes.KEY_Y, 1],
		                [evdev.ecodes.KEY_Y, 0]],

		         "Ä" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_Q, 1],
		                [evdev.ecodes.KEY_Q, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		         "Ë" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_E, 1],
		                [evdev.ecodes.KEY_E, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		         "Ï" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_I, 1],
		                [evdev.ecodes.KEY_I, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		         "Ö" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_O, 1],
		                [evdev.ecodes.KEY_O, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		         "Ü" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_U, 1],
		                [evdev.ecodes.KEY_U, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		         "Ÿ" : [[evdev.ecodes.KEY_LEFTSHIFT, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 1],
		                [evdev.ecodes.KEY_LEFTBRACE, 0],
		                [evdev.ecodes.KEY_Y, 1],
		                [evdev.ecodes.KEY_Y, 0],
		                [evdev.ecodes.KEY_LEFTSHIFT, 0]],
		}

