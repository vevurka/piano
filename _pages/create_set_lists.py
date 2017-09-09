from collections import OrderedDict


def parse_file(file_content):
    composer_pieces_dict = OrderedDict()
    current_composer = "None"
    for line in file_content:
        if not line:
            continue
        split_line = line.split()
        if '###' in split_line[0]:
            composer_pieces_dict[split_line[1]] = []
            current_composer = split_line[1]
        elif '*' in split_line[0]:
            composer_pieces_dict[current_composer].append(' '.join(split_line[1:]))
    return composer_pieces_dict


def generate_set_list(composer_pieces_dict, set_name):
    with open(set_name + '.md', 'w') as f:
        start_str = '---\n' \
            'layout: single\n' \
            'permalink: {}\n' \
            'title: "{}"\n' \
            'author_profile: true\n' \
            '---\n\n'.format(set_name, set_name.title())
        f.write(start_str)
        for composer, pieces in composer_pieces_dict.items():
            pieces_in_set = [piece for piece in pieces if set_name in piece]
            if pieces_in_set:
                f.write('### ' + composer + '\n \n')
                for piece in pieces_in_set:
                    f.write('* ' + ' '.join(piece.split()[:-1]) + '\n')
                f.write('\n')

if __name__ == "__main__":
    number_of_sets = 5
    set_list = ['set' + str(i) for i in range(1, number_of_sets + 1)]
    with open('classic_stream_repertoire.md', 'r') as f:
        composer_pieces_dict = parse_file(f.read().split('\n'))
        for set in set_list:
            generate_set_list(composer_pieces_dict, set)