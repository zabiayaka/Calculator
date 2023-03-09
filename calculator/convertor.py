from calculator.evaluation import evaluate
def convert(result_format, result_1):
    converted_result = None
    if result_format == 1:
        converted_result = result_1
    if result_format == 2:
        converted_result = bin(result_1)
    return converted_result
