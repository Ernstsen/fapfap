class ServerState:
    """Class for server state"""

    def __init__(self):
        self.history = set()
        self.requests = 0

    def register(self, pickup_line):
        self.requests += 1
        self.history.add(pickup_line)

    def get_status(self):
        return "<table>  " + \
               wrap_in_row("<b>Pickup lines delivered: </b>", str(self.requests)) + \
               wrap_in_row("<b>Unique pickup lines delivered: </b>", str(len(self.history))) + \
               "</table>" + \
               "<h3>Generated pickup lines:</h3>" + \
               ("<br/>".join(self.history))


def wrap_in_row(input1, input2):
    return "<tr>" \
           "<td>" + input1 + "</td>" + \
           "<td>" + input2 + "</td>" + \
           "</tr>"
