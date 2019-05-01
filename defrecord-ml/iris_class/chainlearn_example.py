import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

iris = sns.load_dataset('iris').drop('species', axis=1)

pca = PCA(n_components=3)
tsne = TSNE(n_components=2)

kmeans = KMeans(n_clusters=2)

cluster_labels = kmeans.fit_predict(iris)

transformed = tsne.fit_transform(pca.fit_transform(iris))

plt.scatter(transformed[:, 0], transformed[:, 1], c=cluster_labels)


import seaborn as sns
import chainlearn
from matplotlib import pyplot as plt

iris = sns.load_dataset('iris')

(iris
 .drop('species', axis=1)
 .PCA(n_components=3)
 .TSNE(n_components=2)
 .assign(
     cluster=lambda df: df.KMeans(n_clusters=2)
 )
 .plot
 .scatter(
     x=0,
     y=1,
     c='cluster',
     cmap=plt.get_cmap('viridis')
 )
);
