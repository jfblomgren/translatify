#!/usr/bin/env python3

import argparse
from googletrans import Translator


CODE_TO_LANG = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'ma': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'
}

LANG_TO_CODE = dict(map(reversed, CODE_TO_LANG.items()))


def get_language_code(lang):
    if lang in CODE_TO_LANG or lang == 'auto':
        return lang
    elif lang in LANG_TO_CODE:
        return LANG_TO_CODE[lang]
    return None

def language(string):
    lang = string.lower()
    lang_code = get_language_code(lang)
    if lang_code is not None:
        return lang_code
    raise argparse.ArgumentTypeError(lang + ' is not a valid language')

def language_list(string):
    lang_list = []
    for lang in string.split(','):
        if lang.lower() == 'all':
            lang_list += list((CODE_TO_LANG.keys()))
        else:
            lang_list.append(get_language_code(lang))
    return lang_list


translator = Translator()
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--from', metavar='LANGUAGE',
                    help='the language of the original text (default: auto)',
                    type=language, default='auto', dest='from_lang')
parser.add_argument('to_langs', metavar='TO',
                    help='an ordered, comma-separated list of languages to '
                         'translate the text to',
                    type=language_list)
parser.add_argument('text', metavar='TEXT', help='the text to translate',
                    type=str)
args = parser.parse_args()

for i, language in enumerate(args.to_langs):
    from_lang = args.from_lang if i == 0 else args.to_langs[i - 1]
    translation = translator.translate(args.text, src=from_lang, dest=language)
    args.text = translation.text

    # src and dest sometimes come back empty.
    if len(translation.src) > 1:
        from_lang = translation.src
    if len(translation.dest) > 1:
        language = translation.dest

    print('[{} -> {}]'.format(CODE_TO_LANG[from_lang.lower()].title(),
                              CODE_TO_LANG[language.lower()].title()))
    print(args.text)
