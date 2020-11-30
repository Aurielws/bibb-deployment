import csv


def handle_uploaded_file(f):
    decoded_file = f.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    data = []
    for row in reader:
        data.append({
            'prompt': row['Exchange question'],
            'thought': row['Thought (original)'],
            "star": row['Star score - overall'],
            "rank": row['Rank - overall']
        })
    return data


def handle_results(form):
    selected = form.cleaned_data['thoughts']
    choices = dict(form.fields['thoughts'].choices)
    thoughts = [choices[int(item)] for item in selected]
    data = form.cleaned_data
    data['thoughts'] = thoughts
    return data