import xml.etree.ElementTree as ET


def parse_netguard_xml(xml_file_path, output_txt_path):
    try:
        # Load and parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        with open(output_txt_path, "w", encoding="utf-8") as out_file:
            out_file.write("=== NETGUARD SETTINGS BACKUP REPORT ===\n\n")

            # Look for the <application> section
            application = root.find("application")

            if application is not None:
                out_file.write(f"{'SETTING KEY':<30} | {'TYPE':<10} | VALUE\n")
                out_file.write("-" * 60 + "\n")

                # Iterate through all <setting> tags
                for setting in application.findall("setting"):
                    key = setting.get("key", "N/A")
                    val_type = setting.get("type", "N/A")
                    value = setting.get("value", "N/A")

                    # Handle case where the value might be empty (like wifi_homes)
                    if value == "":
                        value = "(empty)"

                    # Write formatted line to text file
                    out_file.write(f"{key:<30} | {val_type:<10} | {value}\n")
            else:
                out_file.write("No <application> settings block found.\n")

            # Extra: Quick check for other empty sections (wifi, mobile, lockdown etc.)
            out_file.write("\n\n=== OTHER SECTIONS AVAILABLE IN BACKUP ===\n")
            for child in root:
                if child.tag != "application":
                    # Check if the section has sub-elements
                    has_data = "Contains data" if len(child) > 0 else "Empty"
                    out_file.write(f"- {child.tag}: {has_data}\n")

        print(f"Success! NetGuard backup successfully saved to: {output_txt_path}")

    except ET.ParseError:
        print("Error: The file is not a valid XML file.")
    except FileNotFoundError:
        print(f"Error: The file '{xml_file_path}' could not be found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the script
if __name__ == "__main__":
    # Change these filenames if your files have different names
    input_xml = "netguard-full.xml"
    output_txt = "netguard_settings.txt"

    parse_netguard_xml(input_xml, output_txt)
