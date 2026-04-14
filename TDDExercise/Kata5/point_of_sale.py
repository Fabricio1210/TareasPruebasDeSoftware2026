class App:

    def __init__(self):
        self.codes = {
                "12345": "$7.25",
                "23456": "$12.50",
                "99999": "Error: barcode not found",
                "": "Error: empty barcode",
                }

    def scan(self, barcode: str):
        if not isinstance(barcode, str):
            return "undefined behavior"
        return self.codes.get(barcode, "undefined behavior")


