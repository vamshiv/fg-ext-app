# main.py
from sql.conn import get_db_connection
from sql.partner_type import determine_partner_type
from sql.queries import user_queries
from xml_parser.ext_khost_key import extract_key
from xml_parser.schedule_params import get_params

from xml_builder import dict_to_xml, save_xml

conn = get_db_connection()

# Define SQLs
producer_sql = """

"""

consumer_sql = """

"""

# Fetch nested dict
nested_data = get_producer_with_consumers(conn, producer_sql, consumer_sql)

# Build XML
xml_string = smart_dict_to_xml(nested_data, root_name="ProducerDetails")

# Save to file
with open("producer_output.xml", "w", encoding="utf-8") as f:
    f.write(xml_string)

print("XML generated successfully!")