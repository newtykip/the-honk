from enum import Enum

class UPCResult(Enum):
    """Possible outputs of the validate_upc function."""
    Invalid = 0
    Valid = 1
    NotNumeric = 2
    InvalidLength = 3

def validate_upc(upc: str) -> UPCResult:
    """
    Validate a universal product code.

    Outputs
    --------
    UPCResult.Invalid -> if the inputted UPC is not valid
    
    UPCResult.Valid -> if the inputted UPC is valid

    Errors
    -------
    UPCResult.NotNumeric -> if the inputted UPC has non-numeric characters (other than dashes)
    
    UPCResult.InvalidLength -> if the inputted UPC is not 12 characters long
    """
    upc = upc.replace('-', '') # remove any dashes

    # catch errors described above
    if not upc.isnumeric():
        return UPCResult.NotNumeric
    elif len(upc) != 12:
        return UPCResult.InvalidLength

    # split the product code from the check digit
    product_code = [int(x) for x in upc]
    check_digit = product_code.pop()

    # work out the odd and even components of the sum
    odd = 3 * sum(product_code[i] for i in range(len(product_code)) if i % 2 == 0)
    even = sum(product_code[i] for i in range(len(product_code)) if i % 2 == 1)

    # sum of the components modulo 10
    modulo = (even + odd) % 10

    # 10 - modulo should equal the check digit if the UPC is valid
    return UPCResult.Valid if check_digit == 10 - modulo else UPCResult.Invalid

print(validate_upc("0-3600029145-2"))