from pygal_maps_world import i18n

i = i18n

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""

    for code, name in i.COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't founde, return None
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))