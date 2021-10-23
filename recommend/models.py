from django.db import models

# Create your models neo4j

from django_neomodel import DjangoNode
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, DateProperty


class Country(StructuredNode):
    country_id = UniqueIdProperty()
    code = StringProperty(unique_index=True, required=True)


class Person(StructuredNode):
    person_id = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    country = RelationshipTo(Country, 'IS_FORM')


class Book(DjangoNode):
    book_id = UniqueIdProperty()
    title = StringProperty(unique_index=True)
    published = DateProperty()

    class Meta:
        app_label = 'recommend'
