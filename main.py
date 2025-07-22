# main.py
from sql.conn import get_db_connection
from sql.partner_type import determine_partner_type
from sql.queries import user_queries
from xml_parser.ext_khost_key import extract_key
from xml_parser.schedule_params import get_params

from xml_builder import dict_to_xml, save_xml

def extract_application_data(account_name, external_xml_paths):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Step 1: Determine user type
        user_type = determine_partner_type(account_name, cursor)
        if not user_type:
            print(f"No user type found for account: {account_name}")
            return

        print(f"User type: {user_type}")

        # Step 2: Fetch DB data
        users_data = user_queries.fetch_user_details(account_name, cursor)

        # Step 3: Parse external XML files
        external_data = {}
        for path in external_xml_paths:
            parsed_xml = parse_form_xml(path)
            external_data.update(parsed_xml)  # Merge

        # Step 4: Combine DB + XML data
        combined_data = {
            "Account": account_name,
            "UserType": user_type,
            "Users": users_data,
            "ExternalForms": external_data
        }

        # Step 5: Convert to XML
        xml_root = dict_to_xml("ApplicationData", combined_data)
        save_xml(xml_root, f"{account_name}_data.xml")
        print(f"XML file created: {account_name}_data.xml")

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    account_name = input("Enter account name: ")
    xml_files = [
        "data/form1.xml",
        "data/metadata.xml"
    ]
    extract_application_data(account_name, xml_files)
