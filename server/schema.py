from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializers import ChannelSerializer, ServerSerializer

server_list_docs = extend_schema(
    responses=ServerSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.STR,
            description="Category of servers to retrieve",
            location=OpenApiParameter.QUERY,
        ),
        OpenApiParameter(
            name="qty",
            type=OpenApiTypes.INT,
            description="Number of servers to retrieve",
            location=OpenApiParameter.QUERY,
        ),
        OpenApiParameter(
            name="by_user",
            type=OpenApiTypes.BOOL,
            description="Filter servers by the current authenticated user (True/False)",
            location=OpenApiParameter.QUERY,
        ),
        OpenApiParameter(
            name="with_num_members",
            type=OpenApiTypes.BOOL,
            description="CInclude the number of members for each server in the response",
            location=OpenApiParameter.QUERY,
        ),
        OpenApiParameter(
            name="by_serverid",
            type=OpenApiTypes.INT,
            description="Include server by id",
            location=OpenApiParameter.QUERY,
        ),
    ]
)