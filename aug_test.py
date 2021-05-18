import json
import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas
import nlpaug.flow as nafc

from nlpaug.util import Action

MAX_LINES = 1
with open("yelp_review_training_dataset.jsonl", "r") as f:

	count = 0

	for line in f:

		if count >= MAX_LINES:

			break

		review = json.loads(line)

		text = review['text']

		aug = naw.ContextualWordEmbsAug(model_path='distilbert-base-uncased', action="substitute")
		augmented_text = aug.augment(text)
		print("Original:")
		print(text)
		print("Augmented Text:")
		print(augmented_text)


		aug = naw.SynonymAug(aug_src='wordnet')
		augmented_text = aug.augment(text)
		print("Augmented Text (Synonym):")
		print(augmented_text)

		count += 1