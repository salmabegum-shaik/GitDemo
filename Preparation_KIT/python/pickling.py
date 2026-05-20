import pickle


data ={"name":"salma","skills":["python","selenium","API"]}
with open("data.pkl",'wb') as file:

    pickle.dump(data,file)