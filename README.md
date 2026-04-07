# blue-tracker

Small CLI that looks up [Blue](https://www.blue.cl) order tracking and prints a summary table for each order ID.

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

Output columns:

| Column               | Meaning                                 |
| -------------------- | --------------------------------------- |
| **ID**               | Order ID you passed                     |
| **Sender**           | Carrier / service name (`coreOs`)       |
| **Estado**           | Title of the active macrostate          |
| **Fecha y hora**     | Last movement timestamp (`generalInfo`) |
| **Entrega estimada** | Estimated delivery date (`generalInfo`) |

If something goes wrong for an order, a line is printed to **stderr** and that order is skipped. Failures include: HTTP or invalid JSON from the API, API payload with `status` ≠ `ok`, or no active macrostate in the trace.

## How it works

The app POSTs to `https://www.blue.cl/api/tracking` with the order ID in the JSON body as `os`, parses the response when `status` is `ok`, and reads macrostate, general info, and core OS from the `data` object.
