""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. """

from text import cmudict, pinyin

_pad = "_"
_punctuation = "¡!'(),.:;?¿ "
_special = "-"
_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáéíóúÁÉÍÓÚÑñЙÜü"
_silences = ["@sp", "@spn", "@sil"]
_spanish=['kʰ', 'k', 'v', 'j', 'ɲ', 'ɡ', 'tɕʰ', 'ɾ', 's', 'θ', 'ɤŋ', 'β', 'y', 't̪', 'tʰ', 'aŋ', 'ʈʂʰ', 'ʃ', 'ɔ', 'd̪', 'ɢ', 'ŋ', 'ʝ', 'ʐ', 'm', 'x', 'sil', 'ç', 'ʂ', 'oŋ', 'e', 'tʃ', 'z', 'ɟ', 'spn', 'l', 'iŋ', 'ʁ', 'b', 'ɤ', 'p', 'æ', 'w', 'i', 'u', 'ʌ', 'c', 't͡s', 'a', 'ɯ', 'tɕ', 'ɟʝ', 'pʰ', 'ʎ', 't', 'f', 'ɣ', 'r', 'n', 'o', 'ð']



# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ["@" + s for s in cmudict.valid_symbols]
_pinyin = ["@" + s for s in pinyin.valid_symbols]
_spanish = ["@" + phoneme for phoneme in _spanish ]

# Export all symbols:
symbols = (
    [_pad]
    + list(_spanish)
    + list(_special)
    + list(_punctuation)
    + list(_letters)
    + _arpabet
    + _pinyin
    + _silences
)