def read_row_request(raw_request):
    with open(raw_request, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]

    try:
        empty_line_index = lines.index('')
    except ValueError:
        empty_line_index = len(lines)

    first_line = lines[0] if lines else ''
    headers = lines[1:empty_line_index]
    body = lines[empty_line_index+1:] if empty_line_index+1 < len(lines) else []

    # Parse headers into a dictionary
    headers_dict = {}
    for header in headers:
        if ':' in header:
            key, value = header.split(':', 1)
            headers_dict[key.strip()] = value.strip()

    return {
        'request_line': first_line,
        'headers': headers_dict,
        'body': '\n'.join(body)
    }
