from transformers import pipeline

MAX_TOKEN_COUNT = 1024
TEXT_LENGTH_INTERVAL = 100


class Summarizer:
	pipe = pipeline("summarization", model="facebook/bart-large-cnn")

	def summarize(self, text, min_size):
		trimmed_text = text

		while len(self.pipe.tokenizer(trimmed_text).tokens()) > MAX_TOKEN_COUNT:
			trimmed_text = trimmed_text[TEXT_LENGTH_INTERVAL:-TEXT_LENGTH_INTERVAL]

		return str(
			self.pipe(
				trimmed_text, min_length=min_size, max_length=(min_size + TEXT_LENGTH_INTERVAL), do_sample=False
			)[0]['summary_text']
		)
