import re

def tokenize_html_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        input_str = file.read()
        for symbol in input_str:
            if (symbol == '\n'):
                print("nl")
            else:
                print(symbol)
        return tokenize_html(input_str)

def tokenize_html(input_str):
    tag_pattern = re.compile(r'<\s*(\w+)\s*')  # to read the tag
    attribute_pattern = re.compile(r'(\w+)\s*=\s*("[^"]*")')
    
    closetag_pattern = re.compile(r'</\s*(\w+)\s*>')
    # void_close = re.compile(r'/>')

    closebracket = re.compile(r'>')
    newline = re.compile(r'\n')
    comment = re.compile(r'<!--.*?-->')
    blank = re.compile(r'\s+')

    tokens = []
    row_count = 1  # Initialize row counter

    while input_str:
        tag_match = tag_pattern.match(input_str)
        if tag_match:
            tag = tag_match.group(1)
            tokens.append(tag)
            input_str = input_str[tag_match.end():]
        elif attribute_pattern.match(input_str):
            attribute_match = attribute_pattern.match(input_str)
            key = attribute_match.group(1)
            value = attribute_match.group(2)
            if key == "method":
                method_value = value.strip('"').strip()
                tokens.append("method" + method_value)
            elif key == "action":
                action_value = value.strip('"').strip()
                tokens.append("action" + action_value)
            elif key == "type":
                type_value = value.strip('"').strip()
                tokens.append("type" + type_value)
            else:
                tokens.append(key)
            input_str = input_str[attribute_match.end():]
        elif closetag_pattern.match(input_str):
            closetag_match = closetag_pattern.match(input_str)
            tokens.append("c" + closetag_match.group(1))
            input_str = input_str[closetag_match.end():]
        elif comment.match(input_str):
            comment_match = comment.match(input_str)
            input_str = input_str[comment_match.end():]
        elif closebracket.match(input_str):
            tokens.append(">")
            input_str = input_str[1:]
        elif newline.match(input_str):
            tokens.append("nl")
            row_count += 1  # Increment row counter for each newline
            input_str = input_str[1:]
        elif blank.match(input_str):
            input_str = input_str[1:]
        else:
            string_match = re.match(r'([^<>]+|\s+)', input_str)
            if string_match:
                tokens.append("string")
                input_str = input_str[string_match.end():]
            else:
                if input_str[0] == '<' or input_str[0] == '>':
                    tokens.append("invalid")
                if input_str[0] == '\n':
                    tokens.append("nl")
                    row_count += 1  # Increment row counter for each newline
                input_str = input_str[1:]
    return tokens

tokenize_html_from_file("Test/table.html")