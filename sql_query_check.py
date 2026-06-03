# sql_query = '''
# SELECT * FROM metatable where salary >= 50 and total_effeciency = 78
# '''

sql_query = input("Enter your query:")
sql_query = sql_query.lower().strip()
print(f"The query is: {sql_query}")

def validate_query(sql_query=sql_query):
    sql_query = sql_query.lower()
    if "delete" in sql_query or "update" in sql_query or "alter" in sql_query:
        print("Invalid SQL query Cannot be executed")
        return 
    print("Valid SQL query U can proceed")

# validate_query(sql_query)

## Relevant function to work with - learned how any can be used 
# SQL Guardrail / Query Guardrail (AI & GenAI Context)
def valid_query(sql_query):
    unvalid_words = ["delete","update","truncate","alter","drop","merge","create"]
    if any(keyword in sql_query for keyword in unvalid_words):
        print("Invalid SQL query. Cannot be executed. It's a threat")
        return False
    print("Valid SQL Query. You can proceed")
    return True

# print(valid_query(sql_query=sql_query))
print("Valid Query. Procedding..." if valid_query(sql_query) else "Not Procedding")

## Query should always start with a with or a select 
def check_query_start(sql_query):
    sql_start_keywords = ("select","with")
    if sql_query.startswith(sql_start_keywords):
        print("Correct Start Checked")
        return True
    print("Wrong start Checked")
    return False
print("Correct start for query" if check_query_start(sql_query) else "Not Procedding")


## check for table names considered 
def allowed_table_check(sql_query):
    sql_table_check = ("employee","sales","customers")
    table_multiple = False
    ## check for single table or multiple tables 
    if "join" in sql_query:
        print("Multiple tables detected due to join")
        table_multiple = True 

    # Case 1: Only one table is used no joints and some where or no where are there
    if not table_multiple:
        from_index = sql_query.find("from") + 4
        table_query_extractor = sql_query[from_index:].strip()
        print(table_query_extractor)
        if table_query_extractor.startswith(sql_table_check):
            print("Correct tables used")
            return True
    print("Not correct table names used. invalid Tables")
    return False 
allowed_table_check(sql_query)
    # Case 2: Joints are used multiple and we can have multiple tables to check
    
