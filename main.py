import streamlit as st

from main_summarizer import Summarizer
from syntax_summarizer import get_text

if __name__ == '__main__':
	cnn_summarizer = Summarizer()

	st.set_page_config(layout='centered', page_icon='📝', page_title='Summary generator')

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
			result = cnn_summarizer.summarize(raw_result, sizes[grade])

			st.write('Result (summary of web site content)')
			st.info(result)
		else:
			st.text('Invalid URL! Try again')
