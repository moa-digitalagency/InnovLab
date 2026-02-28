import json
import os
from flask import request, session, current_app

_translations = {}

def load_translations():
    global _translations
    lang_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lang')
    if not os.path.exists(lang_dir):
        return
    for filename in os.listdir(lang_dir):
        if filename.endswith('.json'):
            lang_code = filename[:-5]
            filepath = os.path.join(lang_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    _translations[lang_code] = json.load(f)
            except Exception as e:
                print(f"Error loading translation file {filename}: {e}")

def get_locale():
    # URL parameter priority
    lang = request.args.get('lang')
    if lang and lang in current_app.config['LANGUAGES']:
        session['lang'] = lang
        return lang

    # Session priority
    lang = session.get('lang')
    if lang and lang in current_app.config['LANGUAGES']:
        return lang

    # Browser priority
    best_match = request.accept_languages.best_match(current_app.config['LANGUAGES'])
    if best_match:
        return best_match

    return 'fr'

def get_translation(key, **kwargs):
    lang = get_locale()

    # Try the requested language
    keys = key.split('.')
    val = _translations.get(lang)
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k)
        else:
            val = None
            break

    # Fallback to fr
    if val is None and lang != 'fr':
        val = _translations.get('fr')
        for k in keys:
            if isinstance(val, dict):
                val = val.get(k)
            else:
                val = None
                break

    # Fallback to the key itself
    if val is None:
        return key

    # Interpolate values
    if isinstance(val, str) and kwargs:
        try:
            return val.format(**kwargs)
        except KeyError:
            return val

    return val

def setup_i18n(app):
    load_translations()

    @app.context_processor
    def inject_i18n():
        return dict(
            get_locale=get_locale,
            _=get_translation,
            t=get_translation
        )
