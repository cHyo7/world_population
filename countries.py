
from pygal_maps_world import i18n

i = i18n

for country_code in sorted(i.COUNTRIES.keys()):
    print(country_code, i.COUNTRIES[country_code])