import sys
import bottle
import argparse
import random
import json
import bottle

quotes = None

# File parsing
def load_quotes(quote_filename):
    """Parses a quote file that consists of quotes separated by empty lines."""
    print(quote_filename)
    quotes = []
    with open(quote_filename) as quote_file:
        current_quote = []
        for line in quote_file:
            if line == '\n' and current_quote:
                quotes.append(''.join(current_quote))        
                current_quote = []
            else:
                current_quote.append(line)
    if current_quote:
        quotes.append(''.join(current_quote))

    return quotes


# Routes
@bottle.route('/<dataset>')
@bottle.route('/<dataset>/random')
def random_quote(dataset):
    """Returns a random quote from the global list of quotes."""
    global quotes
    return random.sample(quotes[dataset], 1)[0]


@bottle.route('/')
def default_random_quote():
    global quotes
    dataset = random.sample(quotes.keys(), 1)[0]
    return random_quote(dataset)


@bottle.route('/<dataset>/<index:int>')
def get_quote(dataset, index):
    """Returns a specific quote by its index."""
    global quotes
    return quotes[dataset][index]


def run_server(quote_table):
    """Starts the bottle server after loading the quotes from the specified
    file."""
    global quotes
    quotes = quote_table
    bottle.run(host='0.0.0.0', port=8080)


def main(argv = None):
    if not argv:
        argv = sys.argv[1:]

    with open('config.json', 'r') as config_file:
        file_map = json.load(config_file)
    
    quote_table = dict((k, load_quotes(v)) for k, v in file_map.iteritems())
    run_server(quote_table)

    run_server()    


if __name__ == "__main__":
    sys.exit(main())
