# -*- coding: utf-8 -*-
"""keyword-exraction-webservice (kews)"""

import collections
from pprint import pprint

from flask import Flask, jsonify, render_template, request
from MeCab import Tagger
from termextract import core, mecab


DEFAULT_TEXT = ''

APP = Flask(__name__)


@APP.route('/', methods=['GET', 'POST'])
def index():
    """Return index page."""
    response = {}
    response['text'] = request.form.get('text', DEFAULT_TEXT)
    response['keyphrases'] = extract(response['text'])

    try:
        result_type = request.form.get('type')
    except KeyError:
        if request.headers['Content-Type'] == 'application/json':
            result_type = 'json'
        else:
            result_type = 'html'

    if result_type == 'json':
        return jsonify(response)

    return render_template('index.html', response=response)


def extract(text):
    """Extract keywords from text."""
    print('[TEXT]')
    print(text)

    mecab_tagger = Tagger('mecabrc')
    tagged_text = mecab_tagger.parse(text)
    print('[TaggedText(Mecab)]')
    print(tagged_text)

    frequency = mecab.cmp_noun_dict(tagged_text)
    print('[Frequency]')
    pprint(frequency)

    score_lr = core.score_lr(frequency, ignore_words=mecab.IGNORE_WORDS,
                             lr_mode=1, average_rate=1)
    print('[LR]')
    pprint(score_lr)

    term_imp = core.term_importance(frequency, score_lr)
    print('[Frequency+LR]')
    data_collection = collections.Counter(term_imp)
    for cmp_noun, value in data_collection.most_common():
        print(core.modify_agglutinative_lang(cmp_noun), value, sep="\t")

    return data_collection.most_common()


if __name__ == '__main__':
    APP.debug = True
    APP.run(host='0.0.0.0')
