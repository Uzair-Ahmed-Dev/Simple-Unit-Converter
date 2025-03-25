import streamlit as st # type: ignore # import sreamlit for creating the web-based UI

# function to convert unit based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers" : 0.001, # 1 meter = 0.001 kilometers
        "kilometers_meters" : 1000, # 1 kilometer = 1000 meters
        "grams_kilograms" : 0.001, # 1 gram = 0.001 kilograms
        "kilograms_grams" : 1000, # 1 kilogram = 1000 grams
        "centimeters_millimeter": 10, # 1 centimeter = 10 millimeters
        "millimeters_centimeters": 0.1, # 1 millimeter = 0.1 centimeters
    }

    key = f"{unit_from}_{unit_to}" # Generated a key based on input and oput units
    if key in conversions:
        conversion = conversions[key]
        # If the conversion is a function (e.g, temperature comversion) , call it
        return (
            conversion(value) if callable(conversion) else value * conversion
            # otherwise , multiply by the conversion factor
        )

    else:
        return "Conversion not supported " # return message if conversion is not defined

# Streamlit UI setup
st.title("Simple Unit Converter") # set title for the web app

# User input: numical value to convert
value = st.number_input("Enter Value:", min_value=1.0, step=1.0) # set title for the web app


# Dropdown to selet unit to convert from
unit_from = st.selectbox(
    "Convert From:", ["meters" , "kilometers" , "centimeters", "millimeters", "grams" , "kilograms"]

)

# Drop to selete unit to convert to
unit_to = st.selectbox(
    "Convert To:", ["meters", "kilometers","centimeters", "millimeters", "grams", "kilograms"]

)

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to) # call the conversion function
    st.write(f"Converted Value: {result}") # Display the result