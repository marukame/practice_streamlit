import streamlit as st
import time

st.title('Streamlit　超入門')


# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4],
#     '2列目':[10, 20, 30, 40],
#     '3列目':[20, 21, 22, 23]
# })

# st.table(df.style.highlight_min(axis=0))

# df2 = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['x','y','z']
# )

# data = np.random.rand(100, 2) / np.array([50, 50]) + np.array([35.69, 139.70])
# map = pd.DataFrame(data, columns=['lat', 'lon'])

# st.dataframe(df2)

# st.map(map)

# st.write("Display Image")


# if st.checkbox('Show Image'):
#     img = Image.open('cat_kotatsu_neko.png')
#     st.image(img)

# option = st.selectbox(
#     '好きな数字',
#     list(range(1,11))
#     )

# st.write('あなたの好きな数字は', option, 'です。')



# expander1 = st.expander('Q1')
# expander1.write('Q1の答え')

st.title('プレグレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0) 

for i in range(100):
    latest_iteration.text(f'現在{i+1}%...')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'

st.write('インタラクティブなウィジェット')

left_column, rghit_column = st.columns(2)
button_left = left_column.button('右側に文字を表示する')

if button_left:
    rghit_column.write('文字を表示します')
    

option = st.text_input('あなたの趣味を教えてください。')
st.write('あなたの趣味：', option)

satisfaction = st.slider('満足度',0,100,50)
st.write('あなたの満足度：', satisfaction)