def before_scenario(context, scenario):
    if 'roman_setup' in scenario.feature.tags:
        print("Before running roman scenario")

def after_scenario(context, scenario):
    if 'roman_setup' in scenario.feature.tags:
        print("After running roman scenario")

