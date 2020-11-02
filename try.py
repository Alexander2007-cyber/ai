import os
import pickle
pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)
x = int(input("Enter first grade: "))
y = int(input("Enter second grade: "))
new_observation = [[ x, y]]
pr = linear.predict(new_observation)
print(pr)