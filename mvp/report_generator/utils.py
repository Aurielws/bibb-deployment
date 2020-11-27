import csv


def handle_uploaded_file(f):
    decoded_file = f.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    data = []
    for row in reader:
        data.append({
            'thought': row['Thought (original)'],
            "star": row['Star score - overall'],
            "rank": row['Rank - overall']
        })
    return data


def handle_results(data):
    return data