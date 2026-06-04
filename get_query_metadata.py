## This file is used to get the metadata of the query like whether it has CTE, subquery, derived table or single select statement.
## This is the new base file to work with.

sql_query = input("Enter your query:")
sql_query = sql_query.lower().strip()
print(f"The query is: {sql_query}")

sql_query_list = sql_query.split()

def check_query_complexity(sql_query):
    # if not valid_query(sql_query):
    #     return None 
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
            subquery_exist_checklist = ["in","=","!=",">=",">","<=","<","exists"]
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

def get_query_type(sql_query:str) -> dict:
    ## Type can be: CREATE, SELECT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, MERGE, INSERT, WITH CTE etc.
    sql_query_type_set = {"create","select","update","delete","drop","alter","truncate","merge","insert","with"}
    if sql_query_list[0] in sql_query_type_set:
        print("Valid SQL Start")
        return {
            "query_type": sql_query_list[0].upper()
        }
    return {
        "query_type": None 
    }

def get_type_of_cte(sql_query:str) -> dict:
    query_type_check = get_query_type(sql_query)
    query_complexity = check_query_complexity(sql_query)
    if query_type_check["query_type"] == "WITH":
        # returns With statement 
        cte_count = 0
        sql_query_cte_start_posibility = {"SELECT","INSERT","UPDATE","DELETE","MERGE","CREATE"}
        keyword_indexes = [keywords for keywords in sql_query_list if keywords.upper() in sql_query_cte_start_posibility]
        print(keyword_indexes)
        last_index = keyword_indexes[len(keyword_indexes) - 1]
        return {
            "query_type": query_type_check["query_type"],
            "query_complexity": query_complexity,
            "cte_type": last_index
        }
    else:
        return{
            "query_type": query_type_check["query_type"],
            "query_complexity": query_complexity,
            "cte_type": None
        }
print(get_type_of_cte(sql_query))