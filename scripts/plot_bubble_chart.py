import matplotlib.pyplot as plt

def plot_bubble_chart(df, x_col, y_col, size_col, color_col, title):
    plt.figure(figsize=(10, 8))
    
    # Scatter plot with bubble size
    plt.scatter(df[x_col], df[y_col], s=df[size_col] * 10, c=df[color_col], cmap='viridis', alpha=0.6, edgecolors='w', linewidth=0.5)
    
    # Add color bar for reference
    plt.colorbar(label=color_col)
    
    # Add labels and title
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.grid(True)
    
    plt.show()
