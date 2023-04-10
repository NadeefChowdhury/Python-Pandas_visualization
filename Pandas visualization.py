#import pandas and matplotlib
#read the csv file as a dataframe called songs(we willw work on only the first 100 values)
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
songs = pd.read_csv('H:\Machine learning\Spotify-2000.csv')
songs2 = songs.head(100)

#create a valence vs energy scatter plot. set the color to red
songs2.plot.scatter(x='Energy', y='Valence', c='red')

#create a histogram of Danceability
songs2['Danceability'].plot.hist()

#create a danceability vs energy histogram and set the style to ggplot.
#set the visibility to 0.5 and increase the number of bins to 20
plt.style.use('ggplot')
songs2.plot.hist(x='Energy', y='Danceability',alpha=0.5, bins=20)

#create a kde plot of liveness
songs2['Liveness'].plot.kde()


