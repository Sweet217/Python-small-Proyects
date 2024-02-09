import numpy as np
from nltk.tokenize import word_tokenize
import gensim


class Neuron:
        def __init__ (self, weight, bias, vocab_size, model):
                self.weight = weight
                self.bias = bias
                self.vocab_size = vocab_size # if the text is 100 words, then the vocab size its gonna be 100
                self.model = model
        
        def activate(self, inputs):
                tokens = word_tokenize(inputs)

                text_embedding = self.calculate_embeddings(tokens)

                weighted_sum = np.dot(text_embedding, self.weight) + self.bias  
                activation_result = self.sigmoid(weighted_sum)

                return activation_result

        
        def sigmoid(self, x):
                return 1/ (1 + np.exp(-x)) #non lineal
        
        def calculate_embeddings(self, tokens):
                valid_tokens = [token for token in tokens if token in self.model] #Since im using a pretrained embedding from gensim "wort2vec" maybe theres some words that arent actually on the embedder, so im just gonna filter
        
                if len(valid_tokens) > 0:
                        embeddings = [self.model[token] for token in valid_tokens]
                        text_embedding = np.mean(embeddings, axis=0)
                else:
                        text_embedding = np.zeros_like(self.model.vector_size, dtype=np.float32)

                return text_embedding
                

# TEST 1#
vocab_size = 300
random_weight = np.random.randn(vocab_size) * np.sqrt(2 / vocab_size)
random_bias = np.random.randn()
model = gensim.models.KeyedVectors.load_word2vec_format('C:\\Users\\ARMADA\\Desktop\\Github folder Python proyects\\Python-small-Proyects\\Experiment with small neurons\\GoogleNews-vectors-negative300.bin', binary=True)
neuron = Neuron(random_weight, random_bias, vocab_size, model)

test_input = "This is a sample sentence for testing."

result = neuron.activate(test_input)

print(f"Input Sentence: {test_input}")
print(f"Activation Result: {result}")
