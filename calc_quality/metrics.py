from vectorization.search import query, init_model
import csv

def requests(markup):
    unique_requests = []
    for item in markup.values():
        for request in item.split(':'):
            unique_requests.append(request)
    return list(set(unique_requests))

def estimate_search_quality(markup_file_path):
    init_model()
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    mrr = 0
    with open(markup_file_path) as markup_file:
        markup = dict(csv.reader(markup_file, delimiter ='\t'))
        requests_list = requests(markup)
        print("in progress->")
        for i, actual_query in enumerate(requests_list):   
            print('Done ' + str(round(100*i/len(requests_list),2)) + '%')                
            actual_results = query(actual_query)
            updated_mrr = False
            for index, w in enumerate(sorted(actual_results, key=actual_results.get, reverse=True)):
                # print("->")
                try:
                    related_searches = markup[w].split(':')
                    ### Setting search limit to 30 ###
                    if not index < 30:
                        if(actual_query not in related_searches):
                            TN += 1
                        else: 
                            if not updated_mrr:
                                mrr += 1 / (index + 1)
                                updated_mrr = True
                            FN += 1
                    if(actual_query in related_searches):
                        if not updated_mrr:
                            mrr += 1 / (index + 1)
                            updated_mrr = True
                        TP += 1
                    else: 
                        FP += 1
                except Exception:
                    continue
        mrr /= len(requests_list)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = (2 * recall * precision) / (recall + precision)
    return {'precision': precision, 'recall': recall, 'f1': f1, 'mrr': mrr}
