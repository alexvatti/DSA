"""
============================================================
 6. ChainMap  —  Combine many dicts into ONE view
============================================================
 (This is a slightly advanced tool — nice to know!)

WHAT IS IT?
-----------
`ChainMap` groups several dictionaries together and lets you
treat them as a SINGLE dictionary — without actually merging
or copying them.

HOW LOOKUP WORKS
----------------
When you look up a key, ChainMap checks each dict IN ORDER
and returns the FIRST match it finds. The first dict "wins".

WHY USE IT?
-----------
Great for settings/configuration where you have layers like:
  1. user settings   (highest priority)
  2. default settings (fallback)
"""

from collections import ChainMap


# ----------------------------------------------------------
# Example 1: Basic lookup order
# ----------------------------------------------------------
defaults = {"theme": "light", "language": "English", "font": "Arial"}
user_settings = {"theme": "dark"}   # user only overrides the theme

# user_settings comes FIRST, so it has higher priority.
settings = ChainMap(user_settings, defaults)

print("theme    =", settings["theme"])     # dark     (from user_settings)
print("language =", settings["language"])  # English  (fell back to defaults)
print("font     =", settings["font"])      # Arial    (fell back to defaults)


# ----------------------------------------------------------
# Example 2: Changes go to the FIRST dict only
# ----------------------------------------------------------
settings["theme"] = "blue"       # updates user_settings
settings["language"] = "Spanish" # ADDS to user_settings (not defaults)

print("\nAfter changes:")
print("user_settings is now:", user_settings)
# {'theme': 'blue', 'language': 'Spanish'}
print("defaults is untouched:", defaults)
# {'theme': 'light', 'language': 'English', 'font': 'Arial'}


# ----------------------------------------------------------
# Example 3: See all the dicts inside
# ----------------------------------------------------------
print("\nAll maps inside:", settings.maps)


# ----------------------------------------------------------
# 🧠 KEY IDEA:
#   ChainMap = look through several dicts as if they were one.
#   The first dict has top priority. Perfect for config layers.
#
#   Run with:  python3 collections/6_chainmap.py
# ----------------------------------------------------------
