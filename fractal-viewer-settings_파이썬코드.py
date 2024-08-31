import tkinter as tk
from tkinter import ttk

class FractalViewerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Fractal Viewer Settings")

        # Create notebook for tabs
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Settings tab
        self.settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_frame, text="Settings")

        # Instructions tab
        self.instructions_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.instructions_frame, text="Instructions")

        self.create_settings_tab()
        self.create_instructions_tab()

    def create_settings_tab(self):
        # General Settings
        ttk.Label(self.settings_frame, text="General Settings").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        settings = ["Brightness", "Gamma", "Saturation", "Speed", "Sun Size"]
        for i, setting in enumerate(settings):
            ttk.Label(self.settings_frame, text=setting).grid(row=i+1, column=0, sticky="w", padx=5)
            ttk.Scale(self.settings_frame, from_=0, to=100, orient=tk.HORIZONTAL).grid(row=i+1, column=1, padx=5, pady=2)

        # Checkboxes
        ttk.Checkbutton(self.settings_frame, text="Show Only Edges").grid(row=6, column=0, columnspan=2, sticky="w", padx=5)
        ttk.Checkbutton(self.settings_frame, text="Enable Nyan Cat").grid(row=7, column=0, columnspan=2, sticky="w", padx=5)
        ttk.Checkbutton(self.settings_frame, text="Enable Waves").grid(row=8, column=0, columnspan=2, sticky="w", padx=5)

        # Color Settings
        ttk.Label(self.settings_frame, text="Color Settings").grid(row=9, column=0, sticky="w", padx=5, pady=5)
        colors = ["Sun Color", "Sky Color", "Fractal Color"]
        for i, color in enumerate(colors):
            ttk.Label(self.settings_frame, text=color).grid(row=i+10, column=0, sticky="w", padx=5)
            ttk.Button(self.settings_frame, text="Choose Color").grid(row=i+10, column=1, padx=5, pady=2)

        # Fractal Settings
        ttk.Label(self.settings_frame, text="Fractal Settings").grid(row=13, column=0, sticky="w", padx=5, pady=5)
        ttk.Label(self.settings_frame, text="Fractal Algorithm").grid(row=14, column=0, sticky="w", padx=5)
        ttk.Combobox(self.settings_frame, values=["Amazing Surface", "Mandelbox", "Mandelbulb"]).grid(row=14, column=1, padx=5, pady=2)

        fractal_settings = ["Fractal Scale", "Fractal Offset X", "Fractal Offset Y", "Fractal Rotation"]
        for i, setting in enumerate(fractal_settings):
            ttk.Label(self.settings_frame, text=setting).grid(row=i+15, column=0, sticky="w", padx=5)
            ttk.Scale(self.settings_frame, from_=0, to=100, orient=tk.HORIZONTAL).grid(row=i+15, column=1, padx=5, pady=2)

        # Randomizer Settings
        ttk.Label(self.settings_frame, text="Randomizer Settings").grid(row=19, column=0, sticky="w", padx=5, pady=5)
        ttk.Checkbutton(self.settings_frame, text="Enable Randomizer").grid(row=20, column=0, columnspan=2, sticky="w", padx=5)
        ttk.Label(self.settings_frame, text="Randomize Interval").grid(row=21, column=0, sticky="w", padx=5)
        ttk.Scale(self.settings_frame, from_=1, to=60, orient=tk.HORIZONTAL).grid(row=21, column=1, padx=5, pady=2)
        ttk.Label(self.settings_frame, text="Transition Duration").grid(row=22, column=0, sticky="w", padx=5)
        ttk.Scale(self.settings_frame, from_=0, to=10, orient=tk.HORIZONTAL).grid(row=22, column=1, padx=5, pady=2)

    def create_instructions_tab(self):
        instructions = """
        Mouse Control: Click and drag to rotate the view.
        Zoom: Use mouse wheel to zoom in and out.

        Settings:
        - Brightness: Adjusts overall scene brightness
        - Gamma: Controls color intensity and contrast
        - Saturation: Adjusts color vividness
        - Speed: Controls animation speed
        - Sun Size: Adjusts the size of the sun
        - Show Only Edges: Displays wireframe version
        - Enable Nyan Cat: Toggles Nyan Cat appearance
        - Enable Waves: Toggles wave animation
        - Color Settings: Change colors of sun, sky, and fractal
        - Fractal Settings: Choose algorithm and adjust scale, offset, and rotation of fractals
        - Randomizer Settings: Enable automatic randomization of settings

        Use the tabs to switch between Settings and Instructions panels.
        """
        ttk.Label(self.instructions_frame, text=instructions, wraplength=400, justify=tk.LEFT).pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    gui = FractalViewerGUI(root)
    root.mainloop()
