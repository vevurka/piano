from collections import OrderedDict


def parse_file(file_content):
    composer_pieces_dict = OrderedDict()
    current_composer = "None"
    for line in file_content:
        if not line:
            continue
        split_line = line.split()
        if not split_line:
            continue
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

        pieces_in_set = []
        for composer, pieces in composer_pieces_dict.items():
            pieces_per_composer_in_set = [piece for piece in pieces if set_name in piece]

            if pieces_per_composer_in_set:
                pieces_in_set += pieces_per_composer_in_set
                f.write('### ' + composer + '\n \n')
                for piece in pieces_per_composer_in_set:
                    f.write('* ' + ' '.join(piece.split()[:-1]) + '\n')
                f.write('\n')
        print("set ", set_name, " has ", len(pieces_in_set))

if __name__ == "__main__":
    repertoire_page = 'classic_stream_repertoire.md'
    number_of_sets = 5
    set_list = ['set' + str(i) for i in range(1, number_of_sets + 1)] + ['can-play', 'learning']
    with open(repertoire_page, 'r') as f:
        composer_pieces_dict = parse_file(f.read().split('\n'))
        for set in set_list:
            generate_set_list(composer_pieces_dict, set)