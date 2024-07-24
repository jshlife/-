import streamlit as st

st.title('지금 파일을 사용한 코드를 만들 수 없는 이유')

if st.button('ChatGPT') :
    st.write(f'ChatGPT plus로 업그레이드하라는 한 마디로 돈 쓰라는 뜻')
if st.button('Gemini'):
    st.write(f'파일 첨부 기능을 지원하지 않음')
if st.button('wrtn'):
    st.write(f'SCV 형식 파일 첨부를 지원하지 않음')


