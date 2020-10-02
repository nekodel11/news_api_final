from flask_wtf import FlaskForm
from wtforms import SelectField
from NEWS_FLASK import newsGenerator

class country_info(FlaskForm):

    country = SelectField('country', choices=[("ar","Argentina"),
                                               ("br", "Brazil"),
                                               ("cn","China"),
                                              ("co", "Colombia"),
                                              ("cu", "Cuba"),
                                              ("fr", "France"),
                                              ("de", "Germany"),
                                              ("hk", "Hong Kong"),
                                              ("it", "Italy"),
                                              ("jp", "Japan"),
                                              ("mx", "Mexico"),
                                              ("ng", "Nigeria"),
                                              ("kr", "Korea"),
                                              ("uk", "United Kingdom"),
                                              ("ve", "Venezuela")
                                              ])

    def country_name(self):
        country = {
            "ar": "Argentina",
            "br": "Brazil",
            "cn": "China",
            "co": "Colombia",
            "cu": "Cuba",
            "fr": "France",
            "de": "Germany",
            "hk": "Hong Kong",
            "it": "Italy",
            "jp": "Japan",
            "mx": "Mexico",
            "ng": "Nigeria",
            "kr": "Korea",
            "uk": "United Kingdom",
            "ve": "Venezuela"
        }
    print(country_name("ar"))