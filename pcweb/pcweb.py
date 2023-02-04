"""The main Pynecone website."""

import pynecone as pc

from pcweb import styles
from pcweb.base_state import State
from pcweb.component_list import component_list
from pcweb.middleware import CloseSidebarMiddleware
from pcweb.pages import routes

# Create the app.
app = pc.App(
    state=State,
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
)

# Add the pages to the app.
for route in routes:
    app.add_page(
        route.component,
        route.path,
        route.title,
        description="Write web apps in pure Python. Deploy in minutes.",
        image="preview.png",
    )

# Add the middleware.
app.add_middleware(CloseSidebarMiddleware(), index=0)

# Run the app.
app.compile()
