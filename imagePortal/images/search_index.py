from haystack import indexes
from images.models import Image

class ImageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Image

    def index_queryset(self):
        return self.get_model().objects.all()
