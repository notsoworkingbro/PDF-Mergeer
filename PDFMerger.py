import pdfkit
from PyPDF2 import PdfMerger
import os

urls = [
    # Links such doi
]

pdf_folder = "pdfs"

os.makedirs(pdf_folder, exist_ok=True)

print(" Converting URLs and merging into a single PDF\n")

failed_urls = []

merger = PdfMerger()

for i, url in enumerate(urls, start=1):

    output_path = os.path.join(pdf_folder, f"ref_{i}.pdf")

    try:

        pdfkit.from_url(url, output_path)
        print(f" Saved: {output_path}")
        merger.append(output_path)

    except Exception as e:

        print(f" Failed to convert {url}: {e}")
        failed_urls.append(url)


final_output = "Compiled_References.pdf"

merger.write(final_output)

merger.close()

print(f"\n Final compiled PDF saved as: {final_output}")

if failed_urls:

    print("\n The following URLs failed to convert:")

    for url in failed_urls:
        print(f" - {url}")

else:
    print("\n No failed conversions!")

print("\n Final merged file: Compiled_References.pdf")
