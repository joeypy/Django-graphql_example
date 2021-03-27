from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import ProductModel
import graphene


class Products(DjangoObjectType):
    class Meta:
        model = ProductModel
        filter_fields = ['id', 'segment', 'country', 'sales']
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    prod_info = relay.Node.Field(Products)
    all_prodinfo = DjangoFilterConnectionField(Products)

    def resolve_prod_info(self, info):
        return ProductModel.objects.all()


schema = graphene.Schema(query=Query)
