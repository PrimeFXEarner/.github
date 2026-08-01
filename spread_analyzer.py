import pandas as pd
import matplotlib.pyplot as plt

def analyze_spreads(file_path):
    """Analyzes historical spread data from a CSV file."""
    df = pd.read_csv(file_path)
    stats = {"Avg": df['spread'].mean(), "Min": df['spread'].min(), "Max": df['spread'].max()}
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['time'], df['spread'], color='#ffd700', label='Spread (Pips)')
    plt.title('PrimeFXEarner Historical Spread Analysis')
    plt.xlabel('Time')
    plt.ylabel('Spread (Pips)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('spread_analysis.png')
    return stats