import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def make_chart():
    plt.plot([1,2,3], [110,130,120])
    plt.savefig('static//img//chart1.png')

    plt.clf()
    plt.plot([1,2,3,4],[3,9,27,81])
    plt.savefig('static//img//chart2.png')