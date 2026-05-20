import pickle

with open("Data.pkl",'rb') as file:
    loaded_data=pickle.load(file)
    print(loaded_data)