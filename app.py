import sys
from terminaltables import AsciiTable

from src.order_status import OrderStatus
from src.errors import BlueTrackerError

def fetch_order_status(id: int | str) -> OrderStatus:
    order_status = OrderStatus.from_order_id(id)

    active_macrostate = order_status.macrostate_info.get_active_macrostate()

    title = active_macrostate.title
    sender = order_status.core_os.display_name
    movement_date = order_status.general_info.last_date_movement
    promise_date = order_status.general_info.promise_date

    return sender, title, movement_date, promise_date

if __name__ == "__main__":
    ids = sys.argv[1:]

    table = [
        ["ID", "Sender", "Estado", "Fecha y hora", "Entrega estimada"],
    ]

    for id in ids:
        print(f"Fetching order {id}...")
        
        try:
            data = fetch_order_status(id)
        except BlueTrackerError as e:
            print(f"Failed to fetch order {id}: {e}", file=sys.stderr)
            continue
        
        table.append([id, *data])

    table = AsciiTable(table)
    print(table.table)
