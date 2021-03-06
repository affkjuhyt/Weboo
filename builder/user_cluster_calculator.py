import numpy as np
from django.db.models import Count

from scipy.sparse import dok_matrix
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from analytics.models import Rating, Cluster


def plot(user_ratings, kmeans, k):
    print("reduce dimensionality of data")
    h = 0.2
    reduced_data = PCA(n_components=2).fit_transform(user_ratings)
    print("cluster reduced data")

    if not kmeans:
        kmeans = KMeans(init='k-means++', n_clusters=k, n_init=10)
        kmeans.fit(reduced_data)

    print("plot clustered reduced data")
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)

    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')

    centroids = kmeans.cluster_centers_
    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=169, linewidths=3,
                color='w', zorder=10)
    plt.title('K-means clustering of the user')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

    plt.savefig('cluster.png')


class UserClusterCalculator(object):
    def calculate(self, k = 23):
        print("training k-means clustering")

        user_ids, user_ratings = self.load_data()

        kmeans = KMeans(n_clusters=k)
        clusters = kmeans.fit(user_ratings.tocsr())

        self.save_cluster(clusters, user_ids)

        return clusters


    @staticmethod
    def load_data(self):
        print('loading data')
        user_ids = list(
            Rating.objects.values('user_id').annotate(book_count=Count('book_id'))
                .order_by('-book_count'))
        content_ids = list(Rating.objects.values('book_id').distinct())
        content_map = {content_ids[i]['book_id']: i for i in range(len(content_ids))}
        num_users = len(user_ids)
        user_ratings = dok_matrix((num_users, len(content_ids)), dtype=np.float32)

        for i in range(num_users):
            # each user corresponds to a row, in the order of all_user_names
            ratings = Rating.objects.filter(user_id=user_ids[i]['user_id'])
            for user_rating in ratings:
                user_ratings[i, content_map[user_rating.book_id]] = user_rating.rating
        print('data loaded')

        return user_ids, user_ratings

    @staticmethod
    def save_cluster(self, clusters, user_ids):
        print("saving clusters")
        Cluster.objects.all().delete()
        for i, clusters_label in enumerate(clusters.labels_):
            Cluster(
                cluster_id=clusters_label,
                user_id=user_ids[i]['user_id']
            ).save()


if __name__ == '__main__':
    print("Calculating user clusters...")
    cluster = UserClusterCalculator()
    cluster.calculate(23)
