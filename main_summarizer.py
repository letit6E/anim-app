from transformers import pipeline

MAX_TOKEN_COUNT = 700
TEXT_LENGTH_INTERVAL = 100
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def summarize(text, min_size):
	size = len(text.split())
	strip_len = (size - MAX_TOKEN_COUNT + 1) // 2
	stripped_words = text.split()[strip_len:-strip_len]

	stripped_text = ""
	for word in stripped_words:
		stripped_text += word + ' '
	return str(
		summarizer(
			stripped_text, min_length=min_size, max_length=(min_size + TEXT_LENGTH_INTERVAL), do_sample=False
		)[0]['summary_text']
	)
