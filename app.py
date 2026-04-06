import sys
from terminaltables import AsciiTable
from src.order_status import OrderStatus

def fetch_order_status(id: int | str) -> OrderStatus:
    order_status = OrderStatus.from_order_id(id)
    active_macrostate = order_status.get_active_macrostate()

    title = active_macrostate.title
    message = active_macrostate.message

    return title, message

if __name__ == "__main__":
    ids = sys.argv[1:]

    table = [
        ["ID", "Estado", "Mensaje"],
    ]

    for id in ids:
        print(f"Fetching order {id}...")
        
        try:
            data = fetch_order_status(id)
        except OrderStatus.Error as e:
            print(f"Error fetching order {id}: {e}", file=sys.stderr)
            continue
        except OrderStatus.NoActiveMacrostateError:
            print(f"No active macrostate found for order {id}", file=sys.stderr)
            continue
        
        table.append([id, *data])

    table = AsciiTable(table)
    print(table.table)
