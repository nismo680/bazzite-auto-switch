from bazzite_auto_switch.drm import find_connectors, find_drm_cards

for card in find_drm_cards():
    print(card)

    for connector in find_connectors(card):
        print("   ", connector)
