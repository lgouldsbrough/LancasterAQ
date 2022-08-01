import LancasterAQ as laq

if __name__ == '__main__':
    # converts to a string in json format
    json_string = laq.GraphObject().to_json()

    # can then be saved to disk
    with open('lancs_aq.json', 'w') as f:
        f.write(json_string)
