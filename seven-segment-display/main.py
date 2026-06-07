import tkinter as tk

from seven_segment import SevenSegmentDisplay


class MASCO_GUI:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "7 Segment Display Test"
        )

        self.value_var = tk.StringVar()

        # ---------------------------------
        # Display
        # ---------------------------------

        self.display = SevenSegmentDisplay(
            root,
            digits=5,
            theme="Red",
            scale=1.0,
            textvariable=self.value_var
        )

        self.display.pack(
            pady=20
        )

        # ---------------------------------
        # Entry
        # ---------------------------------

        tk.Label(
            root,
            text="Value"
        ).pack()

        tk.Entry(
            root,
            textvariable=self.value_var,
            width=20
        ).pack(
            pady=10
        )

        # ---------------------------------
        # Scale Buttons
        # ---------------------------------

        scale_frame = tk.Frame(root)

        scale_frame.pack(
            pady=10
        )

        tk.Button(
            scale_frame,
            text="0.5x",
            command=lambda:
            self.display.configure(
                scale=0.5
            )
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            scale_frame,
            text="1x",
            command=lambda:
            self.display.configure(
                scale=1.0
            )
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            scale_frame,
            text="2x",
            command=lambda:
            self.display.configure(
                scale=2.0
            )
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            scale_frame,
            text="3x",
            command=lambda:
            self.display.configure(
                scale=3.0
            )
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        # ---------------------------------
        # Theme Buttons
        # ---------------------------------

        theme_frame = tk.Frame(root)

        theme_frame.pack(
            pady=10
        )

        tk.Button(
            theme_frame,
            text="Red",
            command=lambda:
            self.display.configure(
                theme="Red"
            )
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            theme_frame,
            text="Green",
            command=lambda:
            self.display.configure(
                theme="Green"
            )
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            theme_frame,
            text="Blue",
            command=lambda:
            self.display.configure(
                theme="Blue"
            )
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        self.value_var.set(
            "12.34"
        )


if __name__ == "__main__":

    root = tk.Tk()

    app = MASCO_GUI(root)

    root.mainloop()