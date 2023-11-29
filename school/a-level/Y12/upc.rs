#![no_std]

extern crate alloc;
use alloc::vec::Vec;

#[derive(Debug)]
enum UPCError {
    NotNumeric,
    InvalidLength,
}

fn parse(value: char) -> Option<u16> {
    match value {
        '1' => Some(1),
        '2' => Some(2),
        '3' => Some(3),
        '4' => Some(4),
        '5' => Some(5),
        '6' => Some(6),
        '7' => Some(7),
        '8' => Some(8),
        '9' => Some(9),
        '0' => Some(0),
        _ => None
    }
}

/// Validates a universal product code. 
fn validate_upc(upc: &str) -> Result<bool, UPCError> {
    let upc = upc.replace('-', ""); // remove any dashes

    if !upc.chars().all(char::is_numeric) { // if the upc is not numeric
        Err(UPCError::NotNumeric)
    } else if upc.len() != 12 { // if the upc is not 12 characters long
        Err(UPCError::InvalidLength)
    } else {
        // split the product code from the check digit
        let mut product_code = upc
            .chars()
            .map(|c| parse(c).unwrap())
            .collect::<Vec<_>>();
        let check_digit = product_code.pop().unwrap();

        // work out the modulo value
        let odd = 3 * product_code.iter().step_by(2).sum::<u16>();
        let even = product_code.iter().step_by(3).sum::<u16>();
        let modulo = (even + odd) % 10;

        // 10 - modulo should equal the check digit if the UPC is valid
        Ok(check_digit == 10 - modulo)
    }
}
