import sys
import bottle
import argparse
import random
import bottle

quotes = None

# File parsing
def load_quotes(quote_filename):
    """Parses a quote file that consists of quotes separated by empty lines."""
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
@bottle.route('/')
def random_quote():
    """Returns a random quote from the global list of quotes."""
    global quotes
    return random.sample(quotes, 1)[0]


def run_server(quote_filename):
    """Starts the bottle server after loading the quotes from the specified
    file."""
    global quotes
    quotes = load_quotes(quote_filename)
    bottle.run(host='localhost', port=8080)


def main(argv = None):
    if not argv:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description=("Server that returns a "
            "random quote"))
    parser.add_argument('--quote-file', default='christmas_messages.txt')
    options = parser.parse_args(argv)
    run_server(options.quote_file)    


if __name__ == "__main__":
    sys.exit(main())
