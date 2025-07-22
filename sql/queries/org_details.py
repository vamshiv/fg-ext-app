from sql.queries.generic_get import fetch_table_details

table_name = "YFS_ORGANIZATION"
where_clause = "OBJECT_ID = ?"
params = ("entity_id",)  

# Fetch details
organization_details = fetch_table_details(conn, table_name, where_clause, params)

if organization_details:
    print("Organization Details:")
    for row in organization_details:
        print(row)
else:
    print("No data found for the organization.")
