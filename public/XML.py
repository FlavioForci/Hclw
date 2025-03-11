import os
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom

# Base URL of your website
base_url = "https://tychara.com"

# The directory where your HTML files are located (replace with your actual folder path)
folder_path = r"C:\Users\flavi\Desktop\Hclw\public"


# Set default change frequency and priority for the URLs
changefreq = "weekly"
priority = "0.8"

# List to hold all the URLs
urls = []

# Scan the folder and subfolders recursively for .html files
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".html"):
            # Build the relative path from the root folder
            relative_path = os.path.relpath(os.path.join(root, file), folder_path)
            
            # Construct the URL based on the relative path
            # Replace backslashes with forward slashes for web URLs (important for Windows)
            url_path = relative_path.replace("\\", "/")
            
            # Remove 'index.html' from the URL, as it typically represents the root of a directory
            if url_path.endswith("index.html"):
                url_path = url_path[:-10]  # Strip off 'index.html'
            
            # Construct the full URL
            full_url = f"{base_url}/{url_path}"
            
            # Append to the URL list
            urls.append(full_url)

# Create the root of the sitemap
urlset = Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

# Loop through URLs to create each <url> element
for url in urls:
    url_element = SubElement(urlset, 'url')
    
    loc = SubElement(url_element, 'loc')
    loc.text = url

    freq = SubElement(url_element, 'changefreq')
    freq.text = changefreq

    prio = SubElement(url_element, 'priority')
    prio.text = priority

# Create a pretty-printed version of the XML
sitemap_xml = xml.dom.minidom.parseString(tostring(urlset)).toprettyxml()

# Write the XML to a file
with open("sitemap.xml", "w") as f:
    f.write(sitemap_xml)

print("Sitemap generated successfully!")
