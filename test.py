def get_content_data(file):
    with open(file, 'r') as myfile:
        data = myfile.read()
        return data
