
#==================================================================================

import matplotlib.pyplot as plt

def Plot_2D(Data_X, Data_Y, Label_X, Label_Y):

    if len(Data_X) != len(Data_Y):
        raise ValueError("Los datasets deben tener la misma longitud")

    plt.figure(figsize=(8, 6))
    plt.plot(Data_X, Data_Y, color='blue')
    plt.xlabel(Label_X)
    plt.ylabel(Label_Y)
    plt.grid(True)
    plt.show()



def Plot_3D(Data_X, Data_Y, Data_Z, Label_X, Label_Y):

    if len(Data_X) != len(Data_Y) or len(Data_X) != len(Data_Z):
        raise ValueError("Los datasets deben tener la misma longitud")

    plt.figure(figsize=(8, 6))
    plt.subplot(111, projection='3d')
    plt.plot(Data_X, Data_Y, Data_Z, color='blue')
    plt.xlabel(Label_X)
    plt.ylabel(Label_Y)
   
