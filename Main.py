import time
import streamlit as st
import numpy as np 
import pandas as pd 
import pymysql
import sqlalchemy
from sqlalchemy import create_engine

# "st.session_state :" ,st.session_state

st.set_page_config(
    page_title="自定義網頁標題",
    page_icon="random",
    # layout="centered",
    layout = "wide",
    # initial_sidebar_state="collapsed"
    )

st.markdown("<h1 style='text-align: center; color: darkblue; margin-top:-70px'>用Markdown做的標題</h1>", unsafe_allow_html=True)
st.title("資訊管理系統")
# st.header("員山醫院")
# st.subheader("Subheader")
# st.write("This is some text 222")

st.sidebar.title("MENU")
st.sidebar.header("Header")
st.sidebar.subheader("Subheader")
st.sidebar.write("This is some text 111")    

# =========================================================

# 用sqlalchemy构建数据库链接engine
db_info = {
    'user':'hch', 
    'password':'OOxx5440', 
    'host':'192.168.2.55', 
    'database':'sakila' # 这里我们事先指定了数据库，后续操作只需要表即可
} 

#这里直接使用pymysql连接,echo=True，会显示在加载数据库所执行的SQL语句。
engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s/%(database)s?charset=utf8' % db_info,echo=False,encoding='utf-8') 

district = st.sidebar.selectbox('Your district',['','Abu Dhabi', 'Andhra Pradesh', 'Bihar', 'Buenos Aires'])
# st.write('你的答案：' + district)

# sql 命令
if district == '':
    sql_cmd = f"SELECT * FROM address"
else:
    sql_cmd = f"SELECT * FROM address where district like '{district}'"
    # sql_cmd = "show tables"

df = pd.read_sql(sql=sql_cmd, con=engine)
# df.to_csv('test.csv')

# pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
# DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None,method=None)



def a_to_b():
    st.session_state.a = st.session_state.b +1
def b_to_a():
    st.session_state.b = st.session_state.a -1

aa,buff,bb = st.columns([2,1,2])
with aa:
    X1 = st.number_input('GG:',key="a",on_change=b_to_a)
with bb:
    X2 = st.number_input('YY:',key="b",on_change=a_to_b)



# col1,col3 = st.columns(2) # 均分成兩分
col1, buff, col3 = st.columns([2,1,15]) #按比例分成兩分
with col1:
    col1.write("left==============")
    left_input = st.number_input("條件過濾",key='LI')
with col3:
    col3.write("Right===============================")
    st.write("This is some text")

    # st.write(df)
    # col3.write(df)
    st.dataframe(df)
    # st.table(df)
