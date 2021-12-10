from pkg_resources import resource_filename
from donbeer.text import Text
import pdb


class SetupHelper:
    def __init__(self, game, text_infos):
        self.game = game
        self.text_infos = text_infos
        self.text_font = resource_filename(__name__, text_infos["font"])

    def build_text_object(self, name, font_size, content, location_data):
        self.game.add_text(Text(name, self.text_font, font_size, content))
        self.set_text_coordinates(name, location_data)

    def build_text_objects(self):
        """Add the text elements to the game object"""

        for name, multipliers in self.text_infos["basic"].items():
            content = name.capitalize() + ":"
            self.build_text_object(name, 60, content, multipliers)

        for name, info in self.text_infos["main"].items():
            self.build_text_object(name, info[1], info[0], info[2])

    def set_text_coordinates(self, name, multipliers):
        """Set the coordinates(x,y) on the pane for the text elements"""

        text = self.game.get_text(name)

        window_dimensions = self.game.config.window.get_size()
        label_dimensions = text.label.get_size()

        def updated_dimension(index, multiplier):
            return (
                window_dimensions[index] / 10 
                * multipliers.get(*multiplier) 
                - label_dimensions[index] / 2
            )

        text.set_coords(
            updated_dimension(0, ('w', 2.5)),
            updated_dimension(1, ('h', 4)),
        )
