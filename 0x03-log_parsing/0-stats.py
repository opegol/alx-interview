#!/usr/bin/python3

"""script reads stdin line by line and computes metrics."""


def print_metrics(file_size, status_code):
    """Reads from stdin line by line and computes metrics.


        Args:
            file_size: .
            status_code: .
    """
    print(f'File size: {file_size}')
    for i in sorted(status_code.keys()):
        print(f'{i}: {status_code[i]}')


if __name__ == "__main__":

    import sys

    p_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0
    status_code = {}
    file_size = 0

    try:

        try:
            for line in sys.stdin:
                count += 1
                line_list = line.split()
                if line_list[-2] in p_code:
                    if line_list[-2] in status_code.keys():
                        status_code[line_list[-2]] += 1
                    else:
                        status_code[line_list[-2]] = 1
                    try:
                        file_size += int(line_list[-1])
                    except (TypeError, ValueError):
                        pass
                if count % 10 == 0:
                    print_metrics(file_size, status_code)
                # count += 1
        except EOFError:
            pass
        print_metrics(file_size, status_code)

    except KeyboardInterrupt:
        print_metrics(file_size, status_code)
        raise
