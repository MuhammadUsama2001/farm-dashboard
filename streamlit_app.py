import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload  # import your app modules here

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    # {"func": heatmap.app, "title": "Timelapse", "icon": "map"},
    {"func": upload.app, "title": "Raster Viz", "icon": "map"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web application is maintained by Asad Imtiaz. You can follow me on social media:
            [GitHub](https://github.com/asadimtiazmalik) | [LinkedIn](https://www.linkedin.com/in/asadimtiazmalik).
        
        Source code: <https://github.com/asadimtiazmalik/farm-dashboard>
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
