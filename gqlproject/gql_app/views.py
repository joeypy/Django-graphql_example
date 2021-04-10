from django.shortcuts import render
import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)
