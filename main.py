import matplotlib.pyplot as plt
import numpy as np


def main():

    # Generate random data
    x = np.random.randn(100)
    y = np.random.randn(100)

    # Create scatter plot
    plt.scatter(x, y)

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Random Scatter Plot')

    # Display plot
    plt.show()




if __name__=='__main__':
    main()
    #exit()