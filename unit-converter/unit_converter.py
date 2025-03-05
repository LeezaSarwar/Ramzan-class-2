# import streamlit as st  # type: ignore

# def convert_units(value, unit_from, unit_to):

#     conversions = {
#         "meters_kilometers": 0.001, # 1meter  = 0.001 kiolmeter
#         "kilometers_meters": 1000, # 1 kilometer =1000 meter
#         "grams_kilograms": 0.001, # 1 gram =0.001 kilogram
#         "kilograms_grams": 1000 # 1kilogram = 1000 gram
#     }
 
#     key  =f"{unit_from}_{unit_to}" # generate a key based on the input and output units
    
#     if key in conversions:
#         conversion = conversion[key]
#         return value * conversion
#     else:
#         return "conversion not supported"
    
# st.title("unit converter")

# value = st.number_input("enter the value:")
# unit_from = st.selectbox("convert from:", ["meters", "kilometers", "grams", "kilograms"])
# unit_to = st.selectbox("convert to:", ["meters", "kilometers", "grams", "kilograms"])

# if st.button("convert"):
#     result = convert_units(value, unit_from, unit_to)
#     st.write(f"converted value: {result}")




# gemini
import streamlit as st  # type: ignore

def convert_units(value, unit_from, unit_to):

    conversions = {
        "meters_kilometers": 0.001,  # 1meter  = 0.001 kiolmeter
        "kilometers_meters": 1000,  # 1 kilometer =1000 meter
        "grams_kilograms": 0.001,  # 1 gram =0.001 kilogram
        "kilograms_grams": 1000  # 1kilogram = 1000 gram
    }

    key = f"{unit_from}_{unit_to}"  # generate a key based on the input and output units

    if key in conversions:
        conversion = conversions[key] # corrected line
        return value * conversion
    else:
        return "conversion not supported"

st.title("unit converter")

value = st.number_input("enter the value:")
unit_from = st.selectbox("convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"converted value: {result}")