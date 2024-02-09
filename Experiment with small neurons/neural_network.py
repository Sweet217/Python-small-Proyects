from neuron import Neuron
import numpy as np

class NeuralNetwork:
     def __init__(self, num_layers, neurons_per_layer, vocab_size, model):
             self.layers = []
             self.vocab_size = vocab_size
             self.model = model
             
             for i in range(num_layers):
                if i == 0:  
                    neurons = []
                for j in range(vocab_size):
                    weight = np.random.randn(vocab_size) * np.sqrt(2 / vocab_size)
                    bias = np.random.randn()
                    neuron = Neuron(weight, bias, vocab_size, model)
                    neurons.append(neuron)
                else: 
                    neurons = []
                    for j in range(neurons_per_layer):
                        weight = np.random.randn(neurons_per_layer) * np.sqrt(2 / neurons_per_layer)
                        bias = np.random.randn()
                        neuron = Neuron(weight, bias, vocab_size, model)
                        neurons.append(neuron)
                self.layers.append(neurons)
        
     def calculate_embeddings(self, tokens):
                valid_tokens = [token for token in tokens if token in self.model] #Since im using a pretrained embedding from gensim "wort2vec" maybe theres some words that arent actually on the embedder, so im just gonna filter
        
                if len(valid_tokens) > 0:
                        embeddings = [self.model[token] for token in valid_tokens]
                        text_embedding = np.mean(embeddings, axis=0)
                else:
                        text_embedding = np.zeros_like(self.model.vector_size, dtype=np.float32)

                return text_embedding
     
     #this code its still on work =)