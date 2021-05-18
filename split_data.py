
import json

# Dataset has 533581 reviews

TRAIN_SIZE = round(533581 * 0.7)

with open("yelp_review_training_dataset.jsonl", "r") as f:

	count = 0

	reviews_train = []
	ratings_train = []
	reviews_test = []
	ratings_test = []

	for count, line in enumerate(f):

		review = json.loads(line)['text']
		rating = json.loads(line)['stars']

		if count <= TRAIN_SIZE:

			reviews_train.append(review)
			ratings_train.append(rating)

		else:

			reviews_test.append(review)
			ratings_test.append(rating)

	print(len(ratings_train))
	##print(ratings)
