import streamlit as st
from PIL import Image

def show_art():

    st.title("My Artwork")
    st.subheader("A collection of my greatest pieces")

    st.header("Killjoy Patent")
    st.write("Front page of the theoretical patent")
    
    patent = Image.open("KJ Turrent Patent Front Page.png")
    st.image(patent, caption="Model data mined from VALORANT", width=500)

    st.header("Radainite Core")
    st.write("Engineering Schematic")
    
    patent = Image.open("Core Engineering Schematic.png")
    st.image(patent, caption="Kingdom first engineering concept designf", width=500)

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
    st.write("The Spike is a dangourse high grade explosive designed by Kingdom Industries in the VALORANT Lore.")
    
    st.video("spike.mp4")  # Replace with your actual file path
