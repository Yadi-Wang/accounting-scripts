"""Print out all the melons in our inventory."""


from melons import melons_track_info


# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])

def print_melon(melons_track_info):
    for name, attributions in melons_track_info.items():
        print(name.upper())
        for attribution, value in attributions.items():
            print(f"{attribution} {value}")
        print('===================================')


print_melon(melons_track_info)
