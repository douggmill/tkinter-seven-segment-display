# Doug Gammill
# Seven Segment Display Widget
# Python 3.12

import tkinter as tk
from PIL import Image, ImageTk
import os


class SevenSegmentDisplay(tk.Frame):

    CHARACTER_SET = "0123456789ABCDEF -=_"

    def __init__(
            self,
            parent,
            digits=4,
            theme="Red",
            value="0",
            textvariable=None,
            scale=1.0,
            **kwargs):

        super().__init__(parent, **kwargs)

        self.digits = digits
        self.theme = theme
        self.scale = scale
        self.value = str(value)

        self.textvariable = textvariable

        self.character_images = {}
        self.character_images_decimal = {}

        self.load_images()

        self.labels = []

        for _ in range(self.digits):

            label = tk.Label(
                self,
                image=self.character_images["0"],
                borderwidth=0
            )

            label.pack(
                side=tk.LEFT,
                padx=0,
                pady=0
            )

            self.labels.append(label)

        if self.textvariable is not None:

            self.textvariable.trace_add(
                "write",
                self._variable_changed
            )

        self.set(self.value)

    # --------------------------------------------------
    # Public Methods
    # --------------------------------------------------

    def set(self, value):

        self.value = str(value)

        value_str = self.value.upper()

        decimal_index = value_str.find(".")

        characters_only = value_str.replace(".", "")

        original_length = len(characters_only)

        characters_only = characters_only.zfill(
            self.digits
        )

        characters_only = characters_only[
            -self.digits:
        ]

        if decimal_index != -1:

            decimal_digit = (
                decimal_index - 1
            )

            padding = (
                self.digits
                - original_length
            )

            decimal_digit += padding

        else:

            decimal_digit = None

        for idx, character in enumerate(
                characters_only):

            if character not in self.character_images:
                character = " "

            if idx == decimal_digit:

                self.labels[idx].configure(
                    image=self.character_images_decimal[
                        character
                    ]
                )

            else:

                self.labels[idx].configure(
                    image=self.character_images[
                        character
                    ]
                )

    def get(self):

        return self.value

    def set_hex(self, value):

        self.set(
            format(value, "X")
        )

    def set_theme(self, theme):

        self.theme = theme

        self.load_images()

        self.set(self.value)

    def set_scale(self, scale):

        self.scale = scale

        self.load_images()

        self.set(self.value)

    # --------------------------------------------------
    # Tkinter Style Configure
    # --------------------------------------------------

    def configure(self, cnf=None, **kwargs):

        if "theme" in kwargs:

            self.set_theme(
                kwargs.pop("theme")
            )

        if "scale" in kwargs:

            self.set_scale(
                kwargs.pop("scale")
            )

        super().configure(
            cnf,
            **kwargs
        )

    config = configure

    # --------------------------------------------------
    # Variable Support
    # --------------------------------------------------

    def _variable_changed(
            self,
            *args):

        self.set(
            self.textvariable.get()
        )

    # --------------------------------------------------
    # Image Loader
    # --------------------------------------------------

    def load_images(self):

        self.character_images.clear()
        self.character_images_decimal.clear()

        sprite_folder = os.path.join(
            os.path.dirname(__file__),
            "sprites"
        )

        standard_filename = os.path.join(
            sprite_folder,
            f"{self.theme}_Seven_segment_display.png"
        )

        decimal_filename = os.path.join(
            sprite_folder,
            f"{self.theme}_Seven_segment_display_decimal.png"
        )

        standard_image = Image.open(
            standard_filename
        )

        decimal_image = Image.open(
            decimal_filename
        )

        img_width, img_height = (
            standard_image.size
        )

        base_width = img_width // 8
        base_height = img_height // 8

        scaled_width = int(
            base_width * self.scale
        )

        scaled_height = int(
            base_height * self.scale
        )

        standard_image = standard_image.resize(
            (
                scaled_width,
                scaled_height
            ),
            Image.LANCZOS
        )

        decimal_image = decimal_image.resize(
            (
                scaled_width,
                scaled_height
            ),
            Image.LANCZOS
        )

        cols = 4
        rows = 5

        tile_width = (
            scaled_width // cols
        )

        tile_height = (
            scaled_height // rows
        )

        for index, character in enumerate(
                self.CHARACTER_SET):

            col = index % cols
            row = index // cols

            left = col * tile_width
            upper = row * tile_height

            right = left + tile_width
            lower = upper + tile_height

            cropped_std = standard_image.crop(
                (
                    left,
                    upper,
                    right,
                    lower
                )
            )

            cropped_dec = decimal_image.crop(
                (
                    left,
                    upper,
                    right,
                    lower
                )
            )

            self.character_images[
                character
            ] = ImageTk.PhotoImage(
                cropped_std
            )

            self.character_images_decimal[
                character
            ] = ImageTk.PhotoImage(
                cropped_dec
            )