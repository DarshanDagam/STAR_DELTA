import streamlit as st
st.title("2305A21L57-PS4")
st.write("calculate the resistance value(R12,R23,R31) of the Delta connection network for given STAR connection network having resistances R1,R2 and R3.")

def STAR_DELTA(R1, R2, R3):
    R12 = (R1 * R2 + R2 * R3 + R3 * R1) / R3
    R23 = (R1 * R2 + R2 * R3 + R3 * R1) / R1
    R31 = (R1 * R2 + R2 * R3 + R3 * R1) / R2
    return R12, R23, R31

col1,col2=st.columns(2)
with col1:
    R1 = st.number_input("R1:Ohms",value=100)
    R2 = st.number_input("R2:Ohms",value=100)
    R3 = st.number_input("R3:Ohms",value=100)
    compute=st.button("Compute")
with col2:
    if compute:
        R12, R23, R31 = STAR_DELTA(R1, R2, R3)
        st.write(f"R12: {R12:.2f} Ohms")
        st.write(f"R23: {R23:.2f} Ohms")
        st.write(f"R31: {R31:.2f} Ohms")




