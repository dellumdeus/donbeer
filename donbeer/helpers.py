from pkg_resources import resource_filename
from donbeer.text import Text


def build_text_objs(game, text_dict):
    """Add the text elements to the game object"""

    font = resource_filename(__name__, 'resources/fonts/MeathFLF.ttf')

    for basic_text in text_dict["basic"]:
        content = basic_text.capitalize() + ":"
        game.add_text(Text(basic_text, font, 60, content))

    for main_text in list(text_dict.items())[1:]:
        name = main_text[0]
        font_size = main_text[1][1]
        content = main_text[1][0]
        game.add_text(Text(name, font, font_size, content))


def set_text_coords(game, name, multipliers={}):
    """Set the coordinates(x,y) on the pane for the text elements"""

    window_width = game.config.window.get_width()
    window_height = game.config.window.get_height()
    text = game.get_text(name)

    label_middle_w = text.label.get_width() / 2
    label_middle_h = text.label.get_height() / 2

    standard_width = window_width / 10
    standard_heigth = window_height / 10

    updated_width = standard_width * multipliers.get('w', 2.5) - label_middle_w
    updated_height = standard_heigth * multipliers.get('h', 4) - label_middle_h

    text.set_coords(updated_width, updated_height)
