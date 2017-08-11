translatify
===========

``translatify`` is a fun command line tool for translating text through
different languages using Google Translate, usually for some amusing results.

Installation
============

``translatify`` can be installed from PyPI using
`pip <https://pip.pypa.io/en/latest/>`__:

.. code:: bash

    $ pip install translatify

Usage
=====

Autodetect the language of the original text and run it through all languages
on Google Translate:

.. code:: bash

    $ translatify "Google Translate is not always accurate"
    [English -> Afrikaans]
    Google Translate is nie altyd akkuraat nie
    [Afrikaans -> Albanian]
    Google Translate nuk është gjithmonë i saktë

    [....]

    [Yiddish -> Yoruba]
    Fun apẹẹrẹ, nigbati isedale.
    [Yoruba -> Zulu]
    Ngokwesibonelo, lapho biology.

Alternatively, you can specify the source and target languages yourself:

.. code:: bash

    $ translatify -s en -t da,zh-cn,de,en "Google Translate is not always accurate"
    [English -> Danish]
    Google Translate er ikke altid korrekt
    [Danish -> Chinese (Simplified)]
    谷歌翻译并不总是正确的
    [Chinese (Simplified) -> German]
    Google-Übersetzung ist nicht immer richtig
    [German -> English]
    Google translation is not always correct

You can specify ``all`` as a target language to include all the languages in
alphabetical order:

.. code:: bash

    $ translatify -t de,all,de,en "Google Translate is not always accurate"
    [English -> German]
    Google Translate ist nicht immer richtig
    [German -> Afrikaans]
    Google Translate is nie altyd reg nie

    [....]

    [Zulu -> German]
    Google
    [German -> English]
    Google
