
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Sigmoid Activation Function",
    page_icon="📈",
    layout="wide"
)

# Application title
st.title("Sigmoid Activation Function")
st.write(
    "Explore how the Sigmoid activation function transforms "
    "input values into outputs between 0 and 1."
)

# Mathematical formula
st.subheader("Mathematical Formula")
st.latex(r"f(x) = \frac{1}{1+e^{-x}}")

st.write(
    "The Sigmoid function maps any input value into a range "
    "between 0 and 1, producing an S-shaped curve."
)

# Interactive input
st.subheader("Interactive Input")

x_value = st.slider(
    "Select an input value (x)",
    min_value=-10.0,
    max_value=10.0,
    value=0.0,
    step=0.5
)

# Calculate Sigmoid output
sigmoid_output = 1 / (1 + np.exp(-x_value))

# Display input and output
col1, col2 = st.columns(2)

with col1:
    st.metric("Input Value (x)", x_value)

with col2:
    st.metric("Sigmoid Output f(x)", f"{sigmoid_output:.4f}")

# Generate values for graph
x = np.linspace(-10, 10, 400)
y = 1 / (1 + np.exp(-x))

# Create graph
st.subheader("Sigmoid Activation Function Graph")

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y, label="Sigmoid Function", linewidth=2)

ax.scatter(
    x_value,
    sigmoid_output,
    color="red",
    s=100,
    label="Selected Input"
)

ax.axhline(0, color="black", linewidth=0.8)
ax.axhline(1, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

ax.set_xlabel("Input (x)")
ax.set_ylabel("Output f(x)")
ax.set_title("Sigmoid Activation Function")
ax.set_ylim(-0.1, 1.1)
ax.legend()
ax.grid(True)

st.pyplot(fig)

# Result interpretation
st.subheader("Result Interpretation")

if x_value < 0:
    st.info(
        "The input is negative. The Sigmoid function produces "
        "an output between 0 and 0.5."
    )
elif x_value == 0:
    st.info(
        "The input is zero. The Sigmoid function produces "
        "an output of 0.5."
    )
else:
    st.success(
        "The input is positive. The Sigmoid function produces "
        "an output between 0.5 and 1."
    )
