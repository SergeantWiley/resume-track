import streamlit as st
from PIL import Image

def show_art():
    st.title("My Artwork")
    st.subheader("A collection of my greatest pieces")

    # First Artwork
    st.header("Venator Star Destroyer")
    st.write("A Venator Class Star Destroyer from the iconic Star Wars The Clone Wars series")
    
    sculpture_image = Image.open("VenatorClass.png")  # Replace with your actual file path
    st.image(sculpture_image, caption="Venator Class Destroyer", width=500)

    # Second Artwork (Video Example)
    st.header("F-35 Perfect Loop Animation")
    st.write("A lone F-35 on a cloudless night in search for her prey.")
    
    st.video("f-35.mp4")  # Replace with your actual file path

    # Third Artwork
    st.header("Jett and her Mclaren")
    st.write("Jett from the iconic game VALORANT by Riot Games on a late night drive near the ocean")
    
    architecture_image = Image.open("Jett.png")  # Replace with your actual file path
    st.image(architecture_image, caption="Jett in her Mclaren", width=500)

    # Fourth Artwork (Another Video Example)
    st.header("Spike Planted")
    st.write("The Spike is a dangourse high grade explosive designed by Kingdom in the VALORANT Lore.")
    
    st.video("spike.mp4")  # Replace with your actual file path
