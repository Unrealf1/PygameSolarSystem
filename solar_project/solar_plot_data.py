import numpy as np
import matplotlib.pyplot as plt

class data:
    def __init__(self):
        self.v, self.r, self.t = np.array([]), np.array([]), np.array([])
    
    def save_plots(self):
        plt.plot(self.t, self.r)        
        #plt.plot(self.v)
        #plt.plot(self.t)
        plt.legend(['r', 'v', 't'])
        
        print("Saving graphs...")
        plt.savefig("graph.png")
        
        print("Saved file" + "graph.png")
    
    def add_frame_data(self, r_new, v_new, t_new):
        self.v = np.append(self.v, v_new)
        self.r = np.append(self.r, r_new)
        self.t = np.append(self.t, t_new)
        
recorded_data = data()
