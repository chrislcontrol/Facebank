from src.presentation.base.schema.data_output_schema import OutputSchema
from src.presentation.base.schema.output_field import OutputField
from src.presentation.schemas.client.client_output_schema import ClientOutputSchema


class AuthenticateClientOutputSchema(OutputSchema):
    access_token = OutputField(type=str, source='token')
    client = ClientOutputSchema()
