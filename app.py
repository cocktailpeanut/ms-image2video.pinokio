import gradio as gr

from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys

pipe = pipeline(task='image-to-video', model='damo/Image-to-Video', model_revision='v1.1.0')

def infer (image_in):
    
    # IMG_PATH: your image path (url or local file)
    IMG_PATH = image_in
    output_video_path = pipe(IMG_PATH, output_video='output.mp4')[OutputKeys.OUTPUT_VIDEO]
    print(output_video_path)
    
    return output_video_path

css="""

#col-container {
    max-width: 580px; 
    margin-left: auto; 
    margin-right: auto;
}
.animate-spin {
  animation: spin 1s linear infinite;
}
@keyframes spin {
  from {
      transform: rotate(0deg);
  }
  to {
      transform: rotate(360deg);
  }
}
#share-btn-container {
  display: flex; 
  padding-left: 0.5rem !important; 
  padding-right: 0.5rem !important; 
  background-color: #000000; 
  justify-content: center; 
  align-items: center; 
  border-radius: 9999px !important; 
  max-width: 13rem;
}
div#share-btn-container > div {
    flex-direction: row;
    background: black;
    align-items: center;
}
#share-btn-container:hover {
  background-color: #060606;
}
#share-btn {
  all: initial; 
  color: #ffffff;
  font-weight: 600; 
  cursor:pointer; 
  font-family: 'IBM Plex Sans', sans-serif; 
  margin-left: 0.5rem !important; 
  padding-top: 0.5rem !important; 
  padding-bottom: 0.5rem !important;
  right:0;
}
#share-btn * {
  all: unset;
}
#share-btn-container div:nth-child(-n+2){
  width: auto !important;
  min-height: 0px !important;
}
#share-btn-container .wrap {
  display: none !important;
}
#share-btn-container.hidden {
  display: none!important;
}
img[src*='#center'] { 
    display: block;
    margin: auto;
}
.footer {
    margin-bottom: 45px;
    margin-top: 10px;
    text-align: center;
    border-bottom: 1px solid #e5e5e5;
}
.footer > p {
    font-size: .8rem;
    display: inline-block;
    padding: 0 10px;
    transform: translateY(10px);
    background: white;
}
.dark .footer {
    border-color: #303030;
}
.dark .footer > p {
    background: #0b0f19;
}

"""

with gr.Blocks(css=css) as demo:
    with gr.Column(elem_id="col-container"):
        gr.Markdown("""
        
            <h1 style="text-align: center;">
                MS Image2Video
            </h1>

            <p style="text-align: center;">
                Turn any image into a video ! <br />
                To use this demo, simply upload an image and hit the Submit button. <br />
                Don't forget to share your results with the <a href="https://huggingface.co/spaces/fffiloni/MS-Image2Video/discussions">Community</a> ;)
            </p>

            [![Duplicate this Space](https://huggingface.co/datasets/huggingface/badges/raw/main/duplicate-this-space-sm.svg#center)](https://huggingface.co/spaces/fffiloni/MS-Image2Video-cloning?duplicate=true)

        
        """)

        image_in = gr.Image(
            label = "Source Image",
            source = "upload", 
            type = "filepath",
            elem_id = "image-in"
        )

        submit_btn = gr.Button(
            "Submit"
        )

        video_out = gr.Video(
            label = "Video Result",
            elem_id = "video-out"
        )


        gr.HTML("""
        
            <div class="footer">
                <p>
                MS-Image2Video Demo by 🤗 <a href="https://twitter.com/fffiloni" target="_blank">Sylvain Filoni</a>
                </p>
            </div>

        """)


    submit_btn.click(
        fn = infer,
        inputs = [
            image_in
        ],
        outputs = [
            video_out
        ]
    )


demo.queue(max_size=20).launch()

