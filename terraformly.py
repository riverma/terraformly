import argparse
import time

# define a function to simulate the terraforming process
def terraform_planet(label, planet_type, surface_area, surface_area_units):
    print(f"Starting terraforming process for {label}...")

    # simulate different checks based on the planet type
    if planet_type.lower() == "moon":
        print("Sorry. Not enough water present for terraforming.")
        return

    # calculate estimated time based on surface area
    if surface_area_units == "million-sq-miles":
        estimated_time = surface_area * 100 / 55.91  # normalize to Mars size
    elif surface_area_units == "million-sq-km":
        estimated_time = surface_area * 100 / 144.8  # convert to Mars surface area in sq km
    else:
        print("Unknown surface area units. Please use 'million-sq-miles' or 'million-sq-km'.")
        return

    print("Working...")
    time.sleep(2)  # simulate work with a short sleep

    # simulate the long terraforming process (we'll skip the actual 100 years wait)
    years_passed = int(estimated_time)
    print(f"({years_passed} years later)")

    print(f"Terraforming process for {label} completed successfully.")

# define the main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Terraform a planet.")
    parser.add_argument('--label', type=str, required=True, help='The label/name of the planet.')
    parser.add_argument('--planet-type', type=str, required=True, choices=['terrestrial', 'moon'], help='Type of planet: terrestrial or moon.')
    parser.add_argument('--surface-area', type=float, required=True, help='Surface area of the planet.')
    parser.add_argument('--surface-area-units', type=str, required=True, choices=['million-sq-miles', 'million-sq-km'], help='Units for surface area.')

    args = parser.parse_args()

    # call the terraform function with parsed arguments
    terraform_planet(args.label, args.planet_type, args.surface_area, args.surface_area_units)

# entry point of the script
if __name__ == "__main__":
    main()
