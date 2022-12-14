import streamlit as st

from main_summarizer import summarize
from syntax_summarizer import get_text

st.set_page_config(layout="centered", page_icon="📝", page_title="Summary generator")

st.title('📝 Web page summary application')

st.write('This application can generate a summary of the main information of a web page')

st.write('Enter required data')
form = st.form('url_form')
input_url = form.text_input('URL of web site (only English)')
sizes = {'Small': 30, 'Medium': 200, 'Big': 350}
grade = form.select_slider('Summary size', sizes.keys())
submit = form.form_submit_button('Generate summary')


if submit:
	raw_result = get_text(input_url)

	if raw_result:
		st.write('Result (summary of web site content)')
		st.info(summarize(raw_result, sizes[grade]))
	else:
		st.text('Invalid URL! Try again')
