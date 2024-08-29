import logging
import azure.functions as func
from PIL import Image
import io

def main(myblob: func.InputStream, outputblob: func.Out[bytes]):
    try:
        logging.info(f"Processing blob: {myblob.name}, Size: {myblob.length} bytes")
        
        # Load the image
        try:
            input_image = Image.open(myblob)
            logging.info("Image successfully loaded.")
        except Exception as e:
            logging.error(f"Error loading image: {e}")
            raise e

        # Resize the image
        try:
            output_size = (200, 200)
            resized_image = input_image.resize(output_size)
            logging.info("Image resized successfully.")
        except Exception as e:
            logging.error(f"Error resizing image: {e}")
            raise e

        # Save the resized image to a byte stream
        try:
            output_stream = io.BytesIO()
            resized_image.save(output_stream, format='PNG')
            output_stream.seek(0)
            logging.info("Image saved to byte stream.")
        except Exception as e:
            logging.error(f"Error saving image to stream: {e}")
            raise e

        # Upload the resized image to the output container
        try:
            outputblob.set(output_stream.read())
            logging.info("Resized image successfully saved to output container.")
        except Exception as e:
            logging.error(f"Error uploading image to output container: {e}")
            raise e

    except Exception as final_exception:
        logging.error(f"Failed to process blob: {final_exception}")
        raise final_exception
