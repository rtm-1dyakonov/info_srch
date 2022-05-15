import sys
from calc_quality.metrics import estimate_search_quality

def main(): 
    search_quality_report = estimate_search_quality(sys.argv[1])
    print(f"mrr={search_quality_report['mrr']} and f1={search_quality_report['f1']} (when precision={search_quality_report['precision']} and recall={search_quality_report['recall']})")
