from term_image.image import from_file

def plot_img_in_terminal(fpath):
    '''
    Renders an image file directly in the terminal.
    from_file() only builds the image object; draw() is what writes it to stdout.
    '''
    image = from_file(fpath)
    image.draw()
