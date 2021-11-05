import numpy as np
import matplotlib.pyplot as plt

class data:
    def __init__(self):
        self.v, self.r, self.t = np.array([]), np.array([]), np.array([])
    
    def save_plots(self):
        print("Saving graphs...")
        plt.plot(self.t, self.r)        
        #fig2 = plt.plot(self.t, self.v)
        #plt.plot(self.t)
        plt.legend(['r(t)'])       
        plt.savefig("graph_r_t.png")
        print("Saved file" + "graph_r_t.png")
        
        plt.clf()        
        plt.plot(self.t, self.v)
        plt.legend(['v(t)'])
        plt.savefig("graph_v_t.png")
        print("Saved file" + "graph_v_t.png")
        
        plt.clf()        
        plt.plot(self.r, self.v)
        plt.legend(['v(r)'])
        plt.savefig("graph_v_r.png")
        
        print("Saved file" + "graph_v_r.png")
    
    def add_frame_data(self, r_new, v_new, t_new):
        self.v = np.append(self.v, v_new)
        self.r = np.append(self.r, r_new)
        self.t = np.append(self.t, t_new)
        
recorded_data = data()
