import pandas as pd
import matplotlib.pyplot as plt

def analyze_spreads(file_path):
    df = pd.read_csv(file_path)
    stats = {"Avg": df['spread'].mean(), "Min": df['spread'].min(), "Max": df['spread'].max()}
    plt.plot(df['time'], df['spread'], color='#ffd700')
    plt.title('PrimeFXEarner Spread Analysis')
    plt.savefig('spread_analysis.png')
    return stats
