from django_elasticsearch_dsl import DocType, Index
from diary_app.models import Entry

entries = Index('entries')

@entries.doc_type
class EntryDoc(DocType):
    class Meta:
        model = Entry

        fields = [
            'title',
        ]