"""Script to visualize the results of the 3-image experiment and scale them to 200 images."""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Function to convert seconds to hours, minutes, and seconds
def format_seconds(seconds):
    """Converts seconds to hours, minutes, and seconds."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    return f"{int(hours)}h {int(minutes)}m {int(sec)}s" if hours > 0 else f"{int(minutes)}m {int(sec)}s"


# Data for 3-image experiment
data = {
    'Model': ['OpenAI', 'Anthropic', 'Google'],
    'Time Taken (s)': [186.66, 434.76, 77.7],
    'Input Tokens': [4068, 5361, 1491],
    'Output Tokens': [13297, 12288, 19726],
    'Cost per M Input T ($)': [2.5, 3.0, 1.25],
    'Cost per M Output T ($)': [10, 15, 5]
}

# Create a DataFrame for the 3-image experiment
df = pd.DataFrame(data)

# Scaling results for 200 images (multiply tokens and costs by 200 / 3)
scale_factor = 200 / 3
df_scaled = df.copy()
df_scaled['Time Taken (s)'] *= scale_factor
df_scaled['Input Tokens'] *= scale_factor
df_scaled['Output Tokens'] *= scale_factor

# Format the time in both the original and scaled DataFrames
df['Time Taken (formatted)'] = df['Time Taken (s)'].apply(format_seconds)
df_scaled['Time Taken (formatted)'] = df_scaled['Time Taken (s)'].apply(format_seconds)

# Plotting the results for 3 images
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Time taken plot
axes[0, 0].bar(df['Model'], df['Time Taken (s)'], color=['blue', 'green', 'red'])
axes[0, 0].set_title('Time Taken for 3 Images')
axes[0, 0].set_ylabel('Time (s)')
for i, v in enumerate(df['Time Taken (s)']):
    axes[0, 0].text(i, v + 10, format_seconds(v), ha='center')

# Merged input and output tokens plot
width = 0.35  # width of bars
x = np.arange(len(df['Model']))

axes[0, 1].bar(x - width/2, df['Input Tokens'], width, label='Input Tokens', color='blue')
axes[0, 1].bar(x + width/2, df['Output Tokens'], width, label='Output Tokens', color='orange')
axes[0, 1].set_title('Input and Output Tokens for 3 Images')
axes[0, 1].set_ylabel('Tokens')
axes[0, 1].set_xticks(x)
axes[0, 1].set_xticklabels(df['Model'])
axes[0, 1].legend()

# Plotting for 200 images (Time Taken)
axes[1, 0].bar(df_scaled['Model'], df_scaled['Time Taken (s)'], color=['blue', 'green', 'red'])
axes[1, 0].set_title('Estimated Time Taken for 200 Images')
axes[1, 0].set_ylabel('Time (s)')
for i, v in enumerate(df_scaled['Time Taken (s)']):
    axes[1, 0].text(i, v + 1000, format_seconds(v), ha='center')

# Cost plot
axes[1, 1].bar(x - width/2, df['Cost per M Input T ($)'], width, label='Cost per M Input T', color='purple')
axes[1, 1].bar(x + width/2, df['Cost per M Output T ($)'], width, label='Cost per M Output T', color='green')
axes[1, 1].set_title('Cost for 200 Images (Input & Output)')
axes[1, 1].set_ylabel('Cost ($)')
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(df['Model'])
axes[1, 1].legend()

plt.tight_layout()
plt.show()
