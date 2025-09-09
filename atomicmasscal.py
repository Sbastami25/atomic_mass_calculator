# atomic_mass_calculator.py
from mendeleev import element # type: ignore # Import the element module

def calculate_atomic_mass(element_symbol):
    """
    Calculates the atomic mass of an element based on the masses and
    natural abundances of its isotopes using data from the mendeleev library.
    """
    print(f"--- Atomic Mass Calculator ---")

    try:
        element_data = element(element_symbol) # Access the element function from the imported module
        isotopes = element_data.isotopes
        element_name = element_data.name # Get the element name
        element_symbol_upper = element_data.symbol # Get the element symbol (ensuring it's uppercase)

    except Exception as e:
        print(f"Error retrieving data for element {element_symbol}: {e}")
        return None # Or handle the error appropriately

    if not isotopes:
        print(f"No isotope data found for {element_symbol_upper} ({element_name}).")
        return None # Or handle the case with no isotopes

    total_abundance = 0
    weighted_mass_sum = 0

    # Iterate through the list of isotopes retrieved from the mendeleev library.
    for isotope in isotopes:
        # For each isotope, check if its natural abundance (isotope.abundance) is not None and is greater than 0.
        if isotope.abundance is not None and isotope.abundance > 0:
            # If the abundance is valid, add the abundance to total_abundance.
            total_abundance += isotope.abundance
            # Calculate the contribution of the isotope to the total atomic mass by multiplying the isotope's mass (isotope.mass) by its abundance (divided by 100) and add this value to weighted_mass_sum.
            weighted_mass_sum += isotope.mass * (isotope.abundance / 100.0)


    # Check if the total abundance is close to 100%
    # Adjusting the tolerance slightly as mendeleev data might not sum exactly to 100
    if not (99.5 <= total_abundance <= 100.5):
        print(f"\nWarning: The sum of the abundances for stable isotopes of {element_name} ({element_symbol_upper}) is {total_abundance:.2f}%, which is not close to 100%.")
        print("The calculated atomic mass may not be accurate.")

    # Print the final calculated atomic mass
    print("\n-----------------------------------------")
    print(f"The calculated atomic mass of {element_name} ({element_symbol_upper}) is: {weighted_mass_sum:.4f} amu")
    print("-----------------------------------------")

    return weighted_mass_sum


# --- Example Usage ---
if __name__ == "__main__":
    user_element = input("Enter the element symbol: ")
    calculate_atomic_mass(user_element)