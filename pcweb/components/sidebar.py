"""Logic for the sidebar component."""

from __future__ import annotations

import inspect

import pynecone as pc
from pynecone.base import Base

from pcweb import styles
from pcweb.component_list import component_list
from pcweb.route import Route

# Sidebar styles.
heading_style = {
    "color": styles.DOC_REG_TEXT_COLOR,
    "font_weight": "500",
}
heading_style2 = {
    "font_size": styles.TEXT_FONT_SIZE,
    "color": styles.DOC_REG_TEXT_COLOR,
    "font_weight": "500",
}
heading_style3 = {
    "font_weight": styles.DOC_SECTION_FONT_WEIGHT,
    "font_size": styles.H3_FONT_SIZE,
    "color": styles.DOC_HEADER_COLOR,
    "margin_bottom": "0.5em",
    "margin_left": "1.1em",
}


class SidebarItem(Base):
    """A single item in the sidebar."""

    # The name to display in the sidebar.
    names: str = ""

    # The link to navigate to when the item is clicked.
    link: str = ""

    # The children items.
    children: list[SidebarItem] = []


def create_item(route: Route, children=None):
    """Create a sidebar item from a route."""
    if children is None:
        name = route.title.split(" | Pynecone")[0]
        if name.endswith("Overview"):
            name = "Overview"
        name = name.replace("Api", "API")
        return SidebarItem(names=name, link=route.path)
    return SidebarItem(
        names=inspect.getmodule(route)
        .__name__.split(".")[-1]
        .replace("_", " ")
        .title(),
        children=list(map(create_item, children)),
    )


def get_sidebar_items_learn():
    return None


def get_sidebar_items_examples():
    pass


@pc.component
def sidebar_leaf(
    item: pc.Var[SidebarItem],
    url: pc.Var[str],
):
    """Get the leaf node of the sidebar."""
    return None


@pc.component
def sidebar_item_comp(
    item: pc.Var[SidebarItem],
    index: pc.Var[int],
    url: pc.Var[str],
    first: pc.Var[bool],
):
    return pc.fragment(
        pc.cond(
            item.children.length() == 0,
            sidebar_leaf(item=item, url=url),
            pc.accordion_item(
                pc.cond(
                    first,
                    pc.accordion_button(
                        pc.accordion_icon(),
                        pc.text(
                            item.names,
                            font_family="Inter",
                            font_size="1em",
                        ),
                        padding_y="0.5em",
                        _hover={
                            "color": styles.ACCENT_COLOR,
                        },
                    ),
                    pc.accordion_button(
                        pc.accordion_icon(),
                        pc.text(
                            item.names,
                            font_family="Inter",
                            font_size="1em",
                        ),
                        padding_y="0.2em",
                        _hover={
                            "color": styles.ACCENT_COLOR,
                        },
                    ),
                ),
                pc.accordion_panel(
                    pc.accordion(
                        pc.vstack(
                            pc.foreach(
                                item.children,
                                lambda child: sidebar_item_comp(
                                    item=child,
                                    index=index,
                                    url=url,
                                    first=False,
                                ),
                            ),
                            align_items="start",
                            border_left="1px solid #e0e0e0",
                        ),
                        allow_toggle=True,
                        allow_multiple=True,
                        # default_index=index,
                    ),
                    margin_left="1em",
                ),
                border="none",
            ),
        )
    )


def calculate_index(sidebar_items, url):
    return None


learn = get_sidebar_items_learn()
examples = get_sidebar_items_examples()


def get_prev_next(url):
    """Get the previous and next links in the sidebar."""
    sidebar_items = learn + examples
    # Flatten the list of sidebar items
    flat_items = []

    def append_to_items(items):
        for item in items:
            if len(item.children) == 0:
                flat_items.append(item)
            append_to_items(item.children)

    append_to_items(sidebar_items)
    for i, item in enumerate(flat_items):
        if item.link == url:
            if i == 0:
                return None, flat_items[i + 1]
            elif i == len(flat_items) - 1:
                return flat_items[i - 1], None
            else:
                return flat_items[i - 1], flat_items[i + 1]
    return None, None


@pc.component
def sidebar_comp(
    url: pc.Var[str],
    learn_index: pc.Var[list[int]],
    examples_index: pc.Var[list[int]],
):

    return pc.box(
        pc.heading("Learn", style=heading_style3),
        pc.divider(
            margin_bottom="1em",
            margin_top="0.5em",
        ),
        pc.heading("Reference", style=heading_style3),
        pc.vstack(
            pc.link(
                pc.hstack(
                    pc.icon(tag="MinusIcon", height=".75rem", style=heading_style),
                    pc.text(
                        "Gallery",
                        style={
                            "color": styles.DOC_REG_TEXT_COLOR,
                            "_hover": {"color": styles.ACCENT_COLOR},
                        },
                        font_family="Inter",
                    ),
                ),
                href="",
            ),
            align_items="left",
            margin_left="1.3em",
            margin_top="0.5em",
        ),
        align_items="start",
        overflow_y="scroll",
        max_height="90%",
        padding_bottom="6em",
        padding_right="4em",
        position="fixed",
        scroll_padding="4em",
    )


def sidebar(url=None) -> pc.Component:
    """Render the sidebar."""
    learn_index = calculate_index(learn, url)
    examples_index = calculate_index(examples, url)
    return pc.box(
        sidebar_comp(
            url=url,
            learn_index=learn_index,
            examples_index=examples_index,
        ),
    )
