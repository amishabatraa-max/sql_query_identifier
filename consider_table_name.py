from sql_query_check import valid_query,sql_query
# sql_query = '''
# SELECT * FROM employee where salary >= 50 and total_effeciency = 78
# '''
# # sql_query = input("Enter your query:")
# # sql_query = sql_query.lower().strip()
# # print(f"The query is: {sql_query}")
# ## check for table names considered 

# def allowed_table_check(sql_query):
#     if not valid_query:
#         return False
#     # Check for multiple selects or CTE's or single select
#     select_count = sql_query.count("select")
#     print(f"Total Number of select statements: {select_count}")
#     if select_count > 1:
#         print("Multiple Select statements detected")
#     else:
#         print("Not detected multiple statements")
#     # Case 1: Only one table is used no joints and some where or no where are there
 
#     # Case 2: Joints are used multiple and we can have multiple tables to check
    
# def check_select_count(sql_query):
#     if not valid_query(sql_query):
#         return None
#     cte_flag = False
#     subquery_flag = False
#     single_select_flag = False
#     query_modified = sql_query.replace("(","").replace(")","")
#     query_list = query_modified.split()
#     query_list = [q for q in query_list if q.strip()]
#     print(query_list)
#     if sql_query.count("select") > 1:
#         print("Multiple selects detected")
#         if sql_query.startswith("with"):
#             cte_flag = True
#             print("cte detected")
#         subquery_keywords = ["where","from","having"]
#         if sql_query[sql_query.find("where") + 1] == "select" or \
#         sql_query[sql_query.find("from") + 1] == "select" or \
#         sql_query[sql_query.find("having") + 1] == "select":
#             print("subquery detected")
#             subquery_flag = True
#     else:
#         single_select_flag = True
#     return [sql_query.count("select"),cte_flag,subquery_flag,single_select_flag]  
# print(check_select_count(sql_query))

def check_query_type(sql_query):
    if not valid_query(sql_query):
        return None 
    # Creating flags to check types 
    cte_flag = False
    subquery_flag = False
    simple_statement = False 
    dervied_table_flag = False 
    count_cte_start = 0
    count_subquery_start = 0
    count_derived_table = 0
    sql_query_list = sql_query.replace(")","").replace("(","").split()
    sql_query_list = [q for q in sql_query_list if q.strip()]
    before_select_indexes = [i-1 for i,word in enumerate(sql_query_list) if word == "select"]
    print(sql_query_list)
    if sql_query.count("select") > 1:
        print("Multiple select statements detected")
        ## Case 1: It is a CTE 
        if sql_query.startswith("with"):
            print("CTE detected")
            cte_flag = True
            print(before_select_indexes)
            ## check how many select starts after AS - and consider it as CTE 
            for x in before_select_indexes:
                print(sql_query_list[x])
                if sql_query_list[x] == "as":
                    count_cte_start += 1
            ## Case 1.1: It is a multiple CTE 
            if count_cte_start > 1:
                print("Multiple CTE detected")
                multiple_cte_flag = True
            ## Case 1.2: It is a single CTE
            else:
                print("Single CTE detected")
        ## Case 2: subquery Subquery after in |  = | exist 
        for x in before_select_indexes:
            subquery_exist_checklist = ["in","=","!=",">=",">","<=","<","exist"]
            if any(keywords for keywords in subquery_exist_checklist if keywords == sql_query_list[x]):
                    count_subquery_start += 1
            if count_subquery_start > 0:
                 subquery_flag = True
        ## Case 3: Dervied Table 
            ## Case 3.1: exists query after from () as table_alias
        for x in before_select_indexes:
            if sql_query_list[x] == "from":
                    count_derived_table += 1
            if count_derived_table > 0:
                 dervied_table_flag = True
    else:
        print("Single Select Detected")
        simple_statement = True
    return {
            "CTE": cte_flag,
            "count of CTE": count_cte_start,
            "subquery": subquery_flag,
            "count of subqueries": count_subquery_start,
            "single select": simple_statement,
            "derived table": dervied_table_flag,
            "count of dervied table": count_derived_table
        }
print(check_query_type(sql_query))