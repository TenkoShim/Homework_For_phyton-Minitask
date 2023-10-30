from tabulate import tabulate

def format_table(benchmarks, algos, results):
    table = []
    for i in range(len(benchmarks)):
        row = [benchmarks[i]] + [result[i] for result in results]
        table.append(row)

    headers = ["Benchmark"] + algos
    table_str = tabulate(table, headers=headers, tablefmt="grid")

    print(table_str)

benchmarks = ["best case", "worst case"]
algos = ["quick sort", "merge sort", "bubble sort"]
results = [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]

format_table(benchmarks, algos, results)