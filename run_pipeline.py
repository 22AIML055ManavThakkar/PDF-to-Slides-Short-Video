import argparse, os
from src.pdf_reader import extract_text
from src.summarizer import get_key_points, make_slide_content
from src.slide_builder import build_slides
from src.video_builder import build_video

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--outdir", required=True)
args = parser.parse_args()

os.makedirs(args.outdir, exist_ok=True)

text = extract_text(args.input)

sections = get_key_points(text)
slides_data = [make_slide_content(t, c) for t, c in sections]

build_slides(slides_data, "assets/placeholder.png",
             os.path.join(args.outdir, "slides.pptx"))

build_video(slides_data,
            os.path.join(args.outdir, "video.mp4"))

print("DONE")
