# Мини-задача #9

# Реализовать функцию:
#
# def format_table(benchmarks, algos, results)
#
# Функция должны выводить отформатированную таблицу с
# результатами сравнения алгоритмов на различных
# бенчмарках.
#
# При этом значения во всех столбцах должны
# отображаться на одном уровне (cм. пример)
def format_table(benchmarks, algos, results) -> str:
    table = []
    length_of_columns = []
    # It's for moments when Benchmark is longer than words from benchmarks
    benchmarks.append("Benchmark")
    length_of_columns.append(max(map(len, benchmarks)))  # max length of column
    benchmarks.remove("Benchmark")
    for i in range(len(algos)):
        alg = algos[i]
        column_info = [str(result[i]) for result in results]
        column = max(len(alg), len(max(column_info, key=len)))
        length_of_columns.append(column)
    # making title of table and bot of title
    title_table = f"| {"Benchmark":<{length_of_columns[0]}} |"
    bot_of_title = "|" + "-" * (length_of_columns[0] + 2)
    for i in range(len(algos)):
        alg = algos[i]
        title_table += f" {alg:^{length_of_columns[i + 1]}} |"
        bot_of_title += "-" * (length_of_columns[i + 1] + 3)
    table.append(title_table)
    table.append(bot_of_title + "|")
    # making rows with info
    for j, benchmark in enumerate(benchmarks):
        row = f"| {benchmark:<{length_of_columns[0]}} |"
        for i in range(len(results[j])):
            result = results[j][i]
            row += f" {result:<{length_of_columns[i + 1]}} |"
        table.append(row)
    # printing table
    for i in table:
        print(i)


benchmarks = ["best case", "worst case"]
algos = ["quick sort", "merge sort", "bubble sort"]
results = [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]
format_table(benchmarks, algos, results)
