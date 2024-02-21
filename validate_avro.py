import click
from avro_validator.schema import Schema

@click.command()
@click.option('--type', default='schema', help='[schema|data]')
@click.option('--schema-file', default='schema.avsc', help='File for the AVRO schema')
@click.option('--data-file', default='data.avro', help='Avro file being validated')
def run(type: str = "schema", schema_file: str = "", data_file: str = ""):
    schema = validate_schema(schema_file)
    if type == 'data':
        schema.validate(data_file)
    
def validate_schema(schema_file):
    with open(schema_file) as fo:
        scema_data = fo.read()
        schema = Schema(scema_data)
        parsed_schema = schema.parse()
        return parsed_schema
    
if __name__ == '__main__':
    run()