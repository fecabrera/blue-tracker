# blue-tracker

Small CLI that looks up [Blue](https://www.blue.cl) order tracking and prints the active macrostate (title and message) in a table.

## Setup

Requires Python 3.14+ and [Pipenv](https://pipenv.pypa.io/).

```bash
pipenv install
pipenv shell
```

## Usage

Pass one or more order IDs (OS numbers):

```bash
python app.py <order_id> [<order_id> ...]
```

Example:

```bash
python app.py 123456789
```

Output columns: **ID**, **Estado**, **Mensaje**.

Errors go to stderr and that order is skipped:

- API returned a non-success payload (message from the server).
- No active macrostate in the trace for that order.

## How it works

The app POSTs to `https://www.blue.cl/api/tracking` with the order ID (`os` in the JSON body), parses the response when `status` is `ok`, walks the macrostate trace, and shows the entry marked active.
