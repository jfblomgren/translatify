#!/usr/bin/env python3

import argparse
from googletrans import Translator
from googletrans.constants import LANGUAGES, LANGCODES


CODE_TO_LANG = LANGUAGES
LANG_TO_CODE = LANGCODES


def get_language_code(lang):
    if lang in CODE_TO_LANG:
        return lang
    elif lang in LANG_TO_CODE:
        return LANG_TO_CODE[lang]
    return None

def language(string, allow_auto=True):
    lang = string.lower()
    lang_code = get_language_code(lang)
    if lang_code is not None:
        return lang_code
    elif allow_auto and lang == 'auto':
        return lang
    raise argparse.ArgumentTypeError(lang + ' is not a valid language')

def language_list(string):
    lang_list = []
    for lang in string.split(','):
        if lang.lower() == 'all':
            lang_list += sorted(CODE_TO_LANG.keys(), key=CODE_TO_LANG.get)
        else:
            lang_list.append(language(lang, allow_auto=False))
    return lang_list


translator = Translator()
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--brief', help='only show the final result',
                    action='store_true')
parser.add_argument('-s', '--source', metavar='LANGUAGE',
                    help='the language of the original text (default: auto)',
                    type=language, default='auto')
parser.add_argument('-t', '--targets', metavar='LANGUAGES',
                    help='an ordered, comma-separated list of languages to '
                         'translate the text to (default: all)',
                    type=language_list, default='all')
parser.add_argument('text', metavar='TEXT', help='the text to translate',
                    type=str)
args = parser.parse_args()

for i, target in enumerate(args.targets):
    source = args.source if i == 0 else args.targets[i - 1]
    translation = translator.translate(args.text, src=source, dest=target)
    args.text = translation.text

    if args.brief:
        continue

    # src and dest sometimes come back empty.
    if len(translation.src) > 1:
        source = translation.src.lower()
    if len(translation.dest) > 1:
        target = translation.dest.lower()

    print('[{} -> {}]'.format(CODE_TO_LANG[source].title(),
                              CODE_TO_LANG[target].title()))
    print(args.text)

if args.brief:
    print(args.text)
