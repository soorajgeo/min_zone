from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import html
from pyvista.trame.ui import plotter_ui

import pyvista as pv

# Offscreen plotting is mandatory for server deployment
pv.OFF_SCREEN = True

server = get_server()
state, ctrl = server.state, server.controller

# Example scene ---------------------------------------------------
mesh = pv.Sphere(radius=2)
plotter = pv.Plotter()
plotter.add_mesh(mesh, color="steelblue")

# UI --------------------------------------------------------------
with SinglePageLayout(server) as layout:
    layout.title.set_text("Borehole Viewer (Trame + Render)")

    with layout.toolbar:
        html.Div("3D Borehole Viewer")

    with layout.content:
        view = plotter_ui(plotter)

# Run -------------------------------------------------------------
if __name__ == "__main__":
    # Bind to 0.0.0.0 so Render can access it
    server.start(port=int(server.cli_args.port), address="0.0.0.0")
