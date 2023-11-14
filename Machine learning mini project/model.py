import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#inputs
inputs = [
    'Text: The Amazon rainforest is the largest tropical rainforest in the world.',
    'Q: Which rainforest is the largest tropical rainforest?',
    'A: The Amazon rainforest is the largest tropical rainforest in the world.',
]
# Separate the inputs into T , Q AND A, text question awnser
texts = []
questions = []
answers = []
for input_str in inputs:
    if input_str.startswith('Text:'):
        texts.append(input_str.replace('Text:', '').strip())
    elif input_str.startswith('Q:'):
        questions.append(input_str.replace('Q:', '').strip())
    elif input_str.startswith('A:'):
        answers.append(input_str.replace('A:', '').strip())

# Tokenize TQA
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts + questions + answers)
num_words = len(tokenizer.word_index) + 1

# Encode TQA into sequences
text_sequences = tokenizer.texts_to_sequences(texts)
question_sequences = tokenizer.texts_to_sequences(questions)
answer_sequences = tokenizer.texts_to_sequences(answers)

# Pad the sequences to a fixed length
max_length = max(max(len(seq) for seq in text_sequences),
                 max(len(seq) for seq in question_sequences),
                 max(len(seq) for seq in answer_sequences))
text_sequences = pad_sequences(text_sequences, maxlen=max_length, padding='post')
question_sequences = pad_sequences(question_sequences, maxlen=max_length, padding='post')
answer_sequences = pad_sequences(answer_sequences, maxlen=max_length, padding='post')

# Define the model architecture
input_text = keras.Input(shape=(max_length,))
input_question = keras.Input(shape=(max_length,))
embedding = keras.layers.Embedding(num_words, 100)
embedded_text = embedding(input_text)
embedded_question = embedding(input_question)
concatenated = keras.layers.Concatenate()([embedded_text, embedded_question])
dense = keras.layers.Dense(128, activation='relu')
output = dense(concatenated)
output = keras.layers.Dense(num_words, activation='softmax')(output)
model = keras.Model([input_text, input_question], output)

# Compiling and training the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit([text_sequences, question_sequences], answer_sequences, epochs=300, verbose=2)

# Testing the model
test_text = 'Cats are wonderfull'
test_question = 'Are cats wonderfull?'
test_text_sequence = tokenizer.texts_to_sequences([test_text])
test_question_sequence = tokenizer.texts_to_sequences([test_question])
test_text_sequence = pad_sequences(test_text_sequence, maxlen=max_length, padding='post')
test_question_sequence = pad_sequences(test_question_sequence, maxlen=max_length, padding='post')
predicted_answer_sequence = model.predict([test_text_sequence, test_question_sequence])
predicted_answer = ' '.join(tokenizer.index_word[index] for index in tf.argmax(predicted_answer_sequence, axis=2).numpy()[0] if index != 0)
predicted_answer = predicted_answer.replace(' <pad>', '')
print('Predicted answer:', predicted_answer)