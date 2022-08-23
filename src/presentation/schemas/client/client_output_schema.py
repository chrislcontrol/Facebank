from src.presentation.base.schema.data_output_schema import OutputSchema
from src.presentation.base.schema.output_field import OutputField


class ClientOutputSchema(OutputSchema):
    username = OutputField(type=str)
    email = OutputField(type=str)
    id = OutputField(type=str)
