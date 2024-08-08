
# import streamlit as st
# import pandas as pd
# import numpy as np

# st.write("Hello World")
# st.text("This is some text.")

# game = pd.read_csv('2023-08-16 Eas-Uni.csv')
# print(game.head())

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# st.line_chart(chart_data)

# __________________________________________________________________
# import streamlit as st 
# import time 
# import numpy as np 

# st.text("First Dinamic Line Chart. That I have no idea how to do it!")
# progress_bar = st.sidebar.progress(0) 
# status_text = st.sidebar.empty() 
# last_rows = np.random.randn(1, 1) 
# chart = st.line_chart(last_rows) 

# for i in range(1, 101): 
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0) 
#     status_text.text("%i%% Complete" % i) 
#     chart.add_rows(new_rows) 
#     progress_bar.progress(i) 
#     last_rows = new_rows 
#     time.sleep(0.05) 
# progress_bar.empty() 
# # Streamlit widgets automatically run the script from top to bottom. Since 
# # this button is not connected to any other logic, it just causes a plain 
# # rerun. 
# st.button("Re-run")

# ____________________________________________________________________

import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)