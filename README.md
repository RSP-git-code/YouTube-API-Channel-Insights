
# YouTube Channel Analysis Using API

This project analyzes data from a specific YouTube channel using the YouTube Data API v3. The project retrieves statistics such as video views, likes, and more, for videos on a given channel. It then visualizes the data using various plots.

## Features
- Fetches channel statistics including subscriber count, total views, and video count.
- Retrieves a list of all video IDs from the channel's playlist.
- Collects detailed statistics (views, likes, etc.) for each video.
- Generates visualizations:
  - Top 10 most-viewed videos using a bar plot.
  - Boxplots of log-transformed views and likes for deeper analysis.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x
- Required libraries: 
  - `googleapiclient`
  - `numpy`
  - `pandas`
  - `seaborn`
  - `matplotlib`
  - `google-auth` (for credentials)

Install the required libraries using:
```bash
pip install google-api-python-client google-auth numpy pandas seaborn matplotlib
```

## Project Structure
- **API Key:** You need to use your YouTube Data API v3 key in the script to authenticate the requests.
- **Channel ID:** The script is designed to fetch data from a specific YouTube channel using its channel ID.
- **Functions:**
  - `get_channel_stats()`: Fetches channel-level statistics.
  - `get_video_id()`: Retrieves video IDs from the channel's upload playlist.
  - `get_video_details()`: Fetches detailed statistics for each video.

## Data Output
- The fetched video data is saved into an Excel file `videodata.xlsx`.
- Data is processed to convert views and likes to numeric values for analysis.
  
## Visualizations
1. **Top 10 Videos by Views**:
   - A bar plot shows the 10 most viewed videos on the channel.

   ![Top 10 Videos by Views] ![image](https://github.com/user-attachments/assets/7a150ba6-4f64-41bf-a10d-3f1ac75230f6)

   
2. **Boxplot of Log-Transformed Views and Likes**:
   - A boxplot displays the distribution of log-transformed views and likes to identify trends and outliers.

   ![Boxplot of Views and Likes](./images/boxplot_views_likes.png)

## How to Run this program:
1. Clone this repository:
   ```bash
   git clone <your-repo-link>
   ```
2. Insert your API key and channel ID into the script.
3. Visual Studio Code with python extension
 
## License
This project is licensed under the MIT License.

