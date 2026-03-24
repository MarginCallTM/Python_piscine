from .elements import (
    create_air,
    create_earth,
    create_fire,
    create_water,
    mega_potion
)


def healing_potion():
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strenght_potion():
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisbility_potion():
    return (
        f"Invisibility potion brewed with {create_air()} and {create_water()}"
    )


def wisdom_potion():
    return f"Wisdom potion brewed with all elements: {mega_potion()}"
