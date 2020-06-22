import streamlit as st

import numpy as np
import pandas as pd

page = st.selectbox("Select a page", options=["Page 1", "Page 2"], index=0) 

st.header(f"{page}")


if page == "Page 1":
    
    b = st.sidebar.slider("b", value=10.0, min_value=1.0, max_value=20.0, step=0.1)

    @st.cache
    def a_function(a):
        return a

    st.write(f"{a_function}")

    ax = plt.axes()
    if st.sidebar.checkbox("c", value=True):
        ax.plot()

    plt.xlabel("label")
    plt.legend()

    plt.axhline(y=0, color="black", linewidth=1)
    ax.set_xlim([0, 15])
    ax.set_ylim([-5, 26])

    st.pyplot()