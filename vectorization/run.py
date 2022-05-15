import sys
from vectorization.search import init_model as init_search, query

def main(): 
    search_str = sys.argv[1]
    max_results = 2
    init_search()
    results_dict = query(search_str)
    for index, w in enumerate(sorted(results_dict, key=results_dict.get, reverse=True)):
        if not index < max_results:
            break
        print(w, results_dict[w])
