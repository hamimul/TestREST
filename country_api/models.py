from django.db import models



class Country(models.Model):
    name_common = models.CharField(max_length=100)
    name_official = models.CharField(max_length=200)
    cca2 = models.CharField(max_length=2, unique=True)  # ISO 3166-1 alpha-2 code
    capital = models.JSONField(null=True, blank=True)  # Stored as array
    population = models.BigIntegerField(default=0)
    timezones = models.JSONField(null=True, blank=True)  # Stored as array
    region = models.CharField(max_length=100, null=True, blank=True)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    languages = models.JSONField(null=True, blank=True)  # Stored as object
    flag_png = models.URLField(max_length=500, null=True, blank=True)
    flag_svg = models.URLField(max_length=500, null=True, blank=True)
    flag_emoji = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name_common

    def get_capital_string(self):
        if not self.capital:
            return "N/A"
        return ', '.join(self.capital)

    def get_languages_list(self):
        if not self.languages:
            return []
        return list(self.languages.values())