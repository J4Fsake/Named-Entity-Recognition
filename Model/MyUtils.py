from collections import defaultdict

def analyze_sentence_lengths(file_path):
    sentence_lengths = defaultdict(int)
    current_length = 0
    total_sentences = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line == "":
                if current_length > 0:
                    sentence_lengths[current_length] += 1
                    total_sentences += 1
                    current_length = 0
            else:
                current_length += 1

        # Trường hợp file không kết thúc bằng dòng trắng
        if current_length > 0:
            sentence_lengths[current_length] += 1
            total_sentences += 1

    print(f"Tổng số câu: {total_sentences}")
    for length in sorted(sentence_lengths):
        if length > 128:
            print(f"Độ dài {length} có {sentence_lengths[length]} câu")
