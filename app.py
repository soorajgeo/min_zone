import os
from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import html
from pyvista.trame.ui import plotter_ui
import pyvista as pv

pv.OFF_SCREEN = True

server = get_server()
state, ctrl = server.state, server.controller

# Example PyVista scene
mesh = pv.Sphere(radius=2)
plotter = pv.Plotter()
plotter.add_mesh(mesh, color="steelblue")

with SinglePageLayout(server) as layout:
    layout.title.set_text("Borehole Viewer")

    with layout.toolbar:
        html.Div("3D Viewer Deployment Test")

    with layout.content:
        view = plotter_ui(plotter)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))   # Render uses PORT env
    server.start(address="0.0.0.0", port=port)

