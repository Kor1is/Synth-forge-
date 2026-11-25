"""Infinity Workbench entry point: page config, layout and routing only."""
from __future__ import annotations

import streamlit as st
from PIL import Image

from core import db
from core.config import APP_ICON, APP_NAME
from core.theme import inject_css
from ui.layout import (init_state, render_right_rail, render_sidebar, render_statusbar,
                       render_topbar)
from ui.pages_construct import render_construct
from ui.pages_home import render_home
from ui.pages_module import render_module
from ui.pages_reports import render_reports
from ui.pages_settings import render_settings


def _page_icon():
    if APP_ICON.exists():
        try:
            with Image.open(APP_ICON) as image:
                return image.copy()
        except Exception:
            pass
    return "∞"


st.set_page_config(
    page_title=APP_NAME,
    page_icon=_page_icon(),
    layout="wide",
    initial_sidebar_state="expanded",
)


def _route(page: str) -> None:
    if page == "home":
        render_home()
    elif page == "module":
        render_module()
    elif page == "construct":
        render_construct()
    elif page == "reports":
        render_reports()
    elif page == "settings":
        render_settings()
    else:
        render_home()


def main() -> None:
    db.init_db()
    projects = db.list_projects()
    init_state(projects)
    inject_css()
    render_topbar(projects)
    render_sidebar()
    main_col, rail = st.columns([1, 0.33], gap="large")
    with main_col:
        _route(st.session_state.get("page", "home"))
    with rail:
        render_right_rail()
    render_statusbar()


if __name__ == "__main__":
    main()