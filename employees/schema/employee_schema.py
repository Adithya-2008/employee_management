from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

get_employees_schema = extend_schema(
    parameters=[
        OpenApiParameter(
            name='emp_ids',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description='Comma-separated employee IDs. Example: 1,2,3',
            required=True
        )
    ]
)