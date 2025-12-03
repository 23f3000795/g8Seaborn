import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. Generate Synthetic Data
# -----------------------------
np.random.seed(42)

# Example dimensions for engagement patterns
hours = [f"{h}:00" for h in range(24)]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Synthetic engagement values (e.g., clicks, visit counts, activity levels)
engagement_data = np.random.randint(10, 100, size=(len(days), len(hours)))

# Create DataFrame for heatmap
df_engagement = pd.DataFrame(engagement_data, index=days, columns=hours)

# -----------------------------
# 2. Style with Seaborn Best Practices
# -----------------------------
sns.set_style("whitegrid")           # Professional style
sns.set_context("talk")              # Larger text for clarity
palette = "viridis"                  # Good perceptual color palette

# -----------------------------
# 3. Create the Heatmap
# -----------------------------
plt.figure(figsize=(8, 8))  # 512x512 at dpi=64

sns.heatmap(
    df_engagement,
    cmap=palette,
    linewidths=0.5,
    annot=False,
    cbar=True
)

# -----------------------------
# 4. Titles and Labels
# -----------------------------
plt.title("Customer Engagement Heatmap (Synthetic Data)", fontsize=18, pad=20)
plt.xlabel("Hour of Day", fontsize=14)
plt.ylabel("Day of Week", fontsize=14)

# -----------------------------
# 5. Save Output
# -----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()

print("Heatmap saved as chart.png")
