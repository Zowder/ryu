
from pprint import pprint
from graphql.type.definition import GraphQLArgument, GraphQLField, GraphQLNonNull, GraphQLObjectType
from graphql.type.scalars import GraphQLString
from resolvers import version



QueryRootType = GraphQLObjectType(
    name='QueryRoot',
    fields={      
        'version': GraphQLField(
            type=GraphQLString,
            resolver=lambda obj, info, version=version._RyuVersionResolver(): version
        )
    }
)